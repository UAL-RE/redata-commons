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