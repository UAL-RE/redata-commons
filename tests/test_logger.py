from redata.commons import logger, git_info
from os import getcwd

import logging
from datetime import date

import pandas as pd

today = date.today()
log_dir = ''
logfile = f'testlog.{today.strftime("%Y-%m-%d")}.log'

# CSV url
csv_url_prefix = "https://raw.githubusercontent.com/UAL-ODIS/ReQUIAM_csv"
csv_version    = "master"
csv_filename   = "requiam_csv/data/research_themes.csv"
csv_url        = f"{csv_url_prefix}/{csv_version}/{csv_filename}"


def test_LogClass():

    log0 = logger.LogClass(log_dir, logfile).get_logger()

    log0.info("Print INFO test")
    log0.debug("Print DEBUG test")
    log0.warning("Print WARNING test")

    assert isinstance(log0, logging.Logger)


def test_log_stdout():
    log0 = logger.log_stdout()

    log0.info("Print INFO test")
    log0.debug("Print DEBUG test")
    log0.warning("Print WARNING test")

    assert isinstance(log0, logging.Logger)


def test_get_hostname():

    sys_info = logger.get_user_hostname()

    assert isinstance(sys_info, dict)

    for key in ['user', 'hostname', 'ip', 'os']:
        assert key in sys_info.keys()


def test_log_setup_LogCommons():
    logfile_prefix = 'testlog'

    log0 = logger.log_setup(getcwd(), logfile_prefix)

    gi = git_info.GitInfo(input_path=getcwd())

    lc = logger.LogCommons(log0, 'test', gi)

    lc.script_start()
    lc.script_sys_info()
    lc.script_end()
    lc.log_permission()


def test_pandas_write_buffer():
    df = pd.read_csv(csv_url)

    logger.pandas_write_buffer(df, logfile)
