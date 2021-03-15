# redata_commons
Commons code used by ReDATA software

## Overview

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


code_path = '/path/to/repo'
gi = GitInfo(code_path)
```
