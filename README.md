# redata_commons

- [Overview](#overview)
- [Installation](#installation)
- [Execution](#execution)
    - [Using `git_info`](#using-git_info)
- [Authors](#authors)
- [License](#license)


## Overview

This repository contains commonly used codes by ReDATA software

The primary sub-package is `commons`. It includes a number of modules, such as:
1. `git_info`
2. `...`


## Installation

From PyPI:
```
(venv) $ pip install redata
```

From source:
```
(venv) $ git clone git@github.com:UAL-ODIS/redata_commons.git
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
[contributors](https://github.com/UAL-ODIS/redata_commons/contributors) who participated in this project.


## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.
