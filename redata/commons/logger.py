import sys
import io
from os import path, uname, chmod, mkdir

from datetime import date
import pandas as pd

import logging

# User and hostname
from getpass import getuser
from socket import gethostname

from requests import get

from redata import __version__
from redata.commons.git_info import GitInfo

today = date.today()

formatter = logging.Formatter('%(asctime)s - %(levelname)8s: %(message)s', "%H:%M:%S")

file_formatter = logging.Formatter('%(asctime)s %(levelname)8s - %(module)20s %(funcName)30s : %(message)s',
                                   "%H:%M:%S")


class LogClass:
    """
    Main class to log information to stdout and ASCII logfile

    :param log_dir: Relative path for exported logfile directory
    :param logfile: Filename for exported log file

    :ivar LOG_FILENAME: Full path of log file
    :ivar file_log_level: File log level: DEBUG

    To use: ``log = LogClass(log_dir, logfile).get_logger()``
    """

    def __init__(self, log_dir: str, logfile: str):
        self.LOG_FILENAME: str = path.join(log_dir, logfile)
        self.file_log_level = logging.DEBUG  # For file logging

    def get_logger(self):
        """Primary method to retrieve stdout and ASCII file Logging object"""
        log = logging.getLogger("main_logger")
        if not log.handlers:
            log.setLevel(self.file_log_level)

            sh = logging.StreamHandler(sys.stdout)
            sh.setLevel(logging.INFO)  # Only at INFO level
            sh.setFormatter(formatter)
            log.addHandler(sh)

            fh = logging.FileHandler(self.LOG_FILENAME)
            fh.setLevel(self.file_log_level)
            fh.setFormatter(file_formatter)
            log.addHandler(fh)

            log.handler_set = True
            log.propagate = False
        return log


def log_stdout() -> logging.Logger:
    """
    Stdout logger

    :return: ``log``
    """
    log_level = logging.INFO
    log = logging.getLogger("stdout_logger")
    if not log.handlers:
        log.setLevel(log_level)
        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(formatter)
        log.addHandler(sh)

        log.handler_set = True
        log.propagate = False
    return log


def log_setup(log_dir: str, logfile_prefix: str) -> logging.Logger:
    """
    Create Logger object (``log``) for stdout and file logging

    :param log_dir: Directory for logs
    :param logfile_prefix: Log file prefix

    :return: Logger object
    """
    if not path.exists(log_dir):
        mkdir(log_dir)
    logfile = f'{logfile_prefix}.{today.strftime("%Y-%m-%d")}.log'

    log = LogClass(log_dir, logfile).get_logger()

    return log


def get_user_hostname() -> dict:
    """
    Retrieve user, hostname, IP, and OS configurations

    :return: ``sys_info``
    """

    sys_info = dict()

    sys_info['user'] = getuser()
    sys_info['hostname'] = gethostname()
    sys_info['ip'] = get('https://api.ipify.org').text

    os_name = uname()
    sys_info['os'] = f"{os_name[0]} {os_name[2]} {os_name[3]}"

    return sys_info


def get_log_file(log_handler) -> str:
    """
    Get log file

    :param log_handler: Logger object

    :return log_file: Full path of log file
    """
    log_file = ''
    if isinstance(log_handler, logging.FileHandler):
        log_file = log_handler.baseFilename
    return log_file


class LogCommons:
    """
    Common methods used when logging

    :param log: Logging object
    :param script_name: Name of script for log messages
    :param gi: Object containing git info
    :param code_name: Name of codebase/software (e.g., ReQUIAM, LD-Cool-P)
    :param version: Version of codebase/software. Default: Use ``redata``'s

    :ivar log: Logging object
    :ivar script_name: Name of script for log messages
    :ivar gi: Object containing git info
    :ivar code_name: Name of codebase/software (e.g., ReQUIAM, LD-Cool-P)
    :ivar version: Version of codebase/software.
    :ivar start_text: Text for script start
    :ivar asterisk: Parsing of start_text as asterisks
    :ivar sys_info: System info dict
    """

    def __init__(self, log: logging.Logger, script_name: str, gi: GitInfo,
                 code_name: str = '', version: str = __version__):
        self.log = log
        self.script_name = script_name
        self.gi = gi
        self.code_name = code_name
        self.version = version

        self.start_text: str = f"Started {script_name} script ... "
        self.asterisk: str = "*" * len(self.start_text)
        self.sys_info: dict = get_user_hostname()

    def script_start(self):
        """Log start of script"""
        self.log.info(self.asterisk)
        self.log.info(self.start_text)
        self.log.debug(f"{self.code_name} active branch: {self.gi.branch}")
        self.log.debug(f"{self.code_name} version: {self.version}"
                       f"({self.gi.short_commit})")
        self.log.debug(f"{self.code_name} commit hash: {self.gi.commit}")

    def script_sys_info(self):
        """Log system info"""
        self.log.debug(f"username : {self.sys_info['user']}")
        self.log.debug(f"hostname : {self.sys_info['hostname']}")
        self.log.debug(f"IP Addr  : {self.sys_info['ip']}")
        self.log.debug(f"Op. Sys. : {self.sys_info['os']}")

    def script_end(self):
        """Log end of script"""
        self.log.info(self.asterisk)
        self.log.info("Exit 0")

    def log_permission(self):
        """Change permission for file logs"""
        for handler in self.log.handlers:
            log_file = get_log_file(handler)
            if log_file:
                self.log.debug(f"Changing permissions for {log_file}")
                chmod(log_file, mode=0o666)


def pandas_write_buffer(df: pd.DataFrame, log_filename: str):
    """
    Write pandas content via to_markdown() to log_filename

    :param df: DataFrame to write to buffer
    :param log_filename: Full path for log file
    """

    buffer = io.StringIO()
    df.to_markdown(buffer)
    print(buffer.getvalue())  # This log to stdout

    with open(log_filename, mode='a') as f:
        print(buffer.getvalue(), file=f)
    buffer.close()


def log_settings(vargs: dict, config_dict: dict, protected_keys: list,
                 log: logging.Logger = log_stdout()) -> int:
    """
    Log parsed arguments settings for scripts

    :param vargs: Parsed arguments
    :param config_dict: Contains configuration settings. See commons.dict_load
    :param protected_keys: list of private arguments to print unset or set status
    :param log: LogClass

    :return: Number of errors with credentials
    """

    if log is None:
        log = log_stdout()

    cred_err = 0
    sections = config_dict.keys()
    for p in vargs.keys():
        value = ''
        for section in sections:
            if p in config_dict[section].keys():
                value = config_dict[section][p]

        if p in protected_keys:
            if value == '***override***' or value == '':
                log.info(f'   {p: >17} = (unset)')
                cred_err += 1
            else:
                log.info(f'   {p: >17} = (set)')
        else:
            log.info(f"   {p: >17} = {value}")

    return cred_err
