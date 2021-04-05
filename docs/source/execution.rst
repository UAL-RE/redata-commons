Execution
---------

Using ``git_info``
~~~~~~~~~~~~~~~~~~

To use, there are a number of ways to import it the main class,
``GitInfo``.

.. code:: python3

   import redata

   code_path = "/path/to/repo"
   gi = redata.commons.git_info.GitInfo(code_path)

or

.. code:: python3

   from redata.commons.git_info import GitInfo

   code_path = "/path/to/repo"
   gi = GitInfo(code_path)


Using ``logger``
~~~~~~~~~~~~~~~~

There are a number of functions and classes available with ``logger``:

  1. ``LogClass``: The main ``Logger`` object for stdout and file logging
  2. ``LogCommons``: Object that has methods to simplify repetitive logging
  3. ``log_stdout``: Function for stdout logging
  4. ``log_setup``: Function to set-up stdout and file logging. Call
     ``LogClass.get_logger()``
  5. ``get_user_hostname``: Function to retrieve system information
     (user, host, IP, OS)
  6. ``get_log_file``: Function to retrieve filenames for file logging
  7. ``log_settings``: Function to log configuration settings. Only arguments
     specified through CLI arguments are shown
  8. ``pandas_write_buffer``: Function to write a prettified (i.e., Markdown)
     version of the table to log handler(s)

First you can either import ``logger`` via:

.. code:: python3

   import redata

or

.. code:: python3

   from redata.commons import logger

To construct a stdout and file logging object, the simplest approach is to use ``log_setup()``:

.. code:: python3

   from redata.commons import logger

   log_dir = '/mnt/curation'
   logfile_prefix = 'mylog'
   log = logger.log_setup(log_dir, logfile_prefix)
   log.info("print log message")


To only log to stdout, use ``log_stdout()``:

.. code:: python3

   from redata.commons import logger

   log_std = logger.log_stdout()
   log_std.info("print log message")


For simplicity, ``LogCommons`` simplifies many of the calls in various scripts
and modules:

.. code:: python3

   from redata.commons import logger, git_info

   log_dir = '/mnt/curation'
   logfile_prefix = 'mylog'
   log = logger.log_setup(log_dir, logfile_prefix)

   code_path = "/path/to/repo"
   gi = git_info.GitInfo(code_path)

   lc = LogCommons(log, 'script_run', gi)
   lc.script_start()  # Starting log message
   lc.script_sys_info()  # Retrieves user and hostname metadata and write to log
   lc.script_end()  # End of script
   lc.log_permission()  # Change permission of log file to read and write for creator and group

To retrieve the full path of the file log, use ``get_log_file()``:

.. code:: python3

   from redata.commons import logger

   log_dir = '/mnt/curation'
   logfile_prefix = 'mylog'
   log = logger.log_setup(log_dir, logfile_prefix)
   for handler in log.handlers:
       log_file = logger.get_log_file(handler)



To retrieve system (OS, IP) and user information, use ``get_user_hostname()``:

.. code:: python3

   from redata.commons import logger

   sys_info_dict = logger.get_user_hostname()


The ``log_settings`` allows for explicit logging of input arguments to
command-line scripts. The below example uses inputs specific to `ReQUIAM`_.

.. code:: python3

   from redata.commons import logger

   log_dir = '/mnt/curation'
   logfile_prefix = 'mylog'
   log = logger.log_setup(log_dir, logfile_prefix)

   config_dict = {
       'ldap_host': 'eds.iam.arizona.edu',
       'ldap_base_dn': 'dc=eds,dc=arizona,dc=edu',
       'ldap_user': 'figshare',
       'ldap_password': '***override***'
   }
   vargs = {'ldap_password': 'abcdef123456'}
   protected_keys = ['ldap_password']
   logger.log_settings(vargs, config_dict, protected_keys, log=log)


Finally, ``pandas_write_buffer`` is often used to provide ``pandas`` DataFrame
in logs:

.. code:: python3

   from redata.commons import logger
   import pandas as pd

   log_dir = '/mnt/curation'
   logfile_prefix = 'mylog'
   log = logger.log_setup(log_dir, logfile_prefix)
   for handler in log.handlers:
       log_filename = logger.get_log_file(handler)

   df = pd.read_csv('data.csv')  # This is a dummy filename
   logger.pandas_write_buffer(df, log_filename)

.. _`ReQUIAM`: https://github.com/UAL-ODIS/ReQUIAM
