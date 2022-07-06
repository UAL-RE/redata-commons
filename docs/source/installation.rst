Installation
------------
The Python Package Index (PyPI) is a repository of software. 

From :pypi:`PyPI <>`:

::

   (venv) $ pip install redata

From :repo:`source <>`:

::

   (venv) $ git clone git@github.com:UAL-RE/redata-commons.git
   (venv) $ python setup.py install


Update ``redata-commons`` 
-------------------------

``redata-commons`` has a typical Python repository structrure. A good reading can be found on The Hitchhiker's Guide to Python: Best Practices for Development 
at https://docs.python-guide.org/writing/structure/

There are a few files to updated for a new version. 
1. ``requirements.txt`` : redata-common required dependencies
2. ``setup.py`` :  Package and distribution management 
3. ``CHANGELOG.md``: 
4. ``README.md" : README file.  
5. ``/docs/requirements.text``: Sphinx required packages
6. ``/docs/source/conf.py``: Configuration file for Sphinx RTD
7. ``/docs/source/*.rst`` : RTD source files. These might need to be updated
8. ``.github/workflows/pypi-publish.yml``: workflow publishs to pypi.org


Directories ``build/``,  ``dist/``, the egg file ``redata.egg-info`` and so on (see .gitignore) are generated when running on building the package. Use the following first command 
to see the available parameters. The 2nd command is to build the package.
 
:: 
    (venv) $ python setup.py --help-commands
    (venv) $ python setup.py sdist bdist_wheel
 
After creating a pull request, workflow actions will be run/compile/test to check the updated code. One of the workflows automatically publish ``redata-commons`` in pypi.org, using its workflows at ``.github/workflows/pypi-publish.yml``. 

Best Practices for using a Python ``requirements.txt`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- use pip freeze to generate a list of Python modules and packages installed in the virtual env.
- ONLY list the modules and packages needed. Do NOT include unneccssary packages, as this makes upgrade extra efforts. It is also a waste of resources.
- Keep requirements.txt file up to date and accurate. This ensure the project always use the latest version of of the Python modules and packages.



