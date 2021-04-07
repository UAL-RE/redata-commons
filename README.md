# redata-commons

[![GitHub Actions Sphinx build status](https://img.shields.io/github/workflow/status/UAL-ODIS/redata-commons/Sphinx%20Docs%20Check?label=sphinx&color=blue)](https://github.com/UAL-ODIS/redata-commons/actions?query=workflow%3A%22Sphinx+Docs+Check%22)
[![RTDs build status](https://readthedocs.org/projects/redata-commons/badge/?version=latest&style=flat)](https://redata-commons.readthedocs.io/en/latest/)

## Table of contents

For our documentation, please click on the links below or visit [Read the Docs](https://redata-commons.readthedocs.io/en/latest/) directly.

- [Overview]([#overview](https://redata-commons.readthedocs.io/en/latest/#overview))
- [Installation](https://redata-commons.readthedocs.io/en/latest/installation.html#installation)
- [Execution](https://redata-commons.readthedocs.io/en/latest/execution.html#execution)
    - [Using `git_info`](https://redata-commons.readthedocs.io/en/latest/execution.html#using-git-info)
    - [Using `logger`](https://redata-commons.readthedocs.io/en/latest/execution.html#using-logger)
- [Authors](#authors)
- [License](#license)


## Overview

This repository contains commonly used codes by ReDATA software

The primary sub-package is `commons`. It includes a number of modules, such as:
1. `git_info`
2. `logger`


## Installation

From PyPI:
```
(venv) $ pip install redata
```

From source:
```
(venv) $ git clone git@github.com:UAL-ODIS/redata-commons.git
(venv) $ python setup.py install
```


## Execution

### Using `git_info`

To use, there are a number of ways to import it the main class, `GitInfo`.

```python3
import redata

code_path = "/path/to/repo"
gi = redata.commons.git_info.GitInfo(code_path)
```

or

```python3
from redata.commons.git_info import GitInfo

code_path = "/path/to/repo"
gi = GitInfo(code_path)
```


## Authors

* Chun Ly, Ph.D. ([@astrochun](http://www.github.com/astrochun)) - [University of Arizona Libraries](https://github.com/ualibraries), [Office of Digital Innovation and Stewardship](https://github.com/UAL-ODIS)

See also the list of
[contributors](https://github.com/UAL-ODIS/redata-commons/contributors) who participated in this project.


## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.
