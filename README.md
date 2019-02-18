<h1 align="center">FITCH</h1>
<p align="center">
    <em>Android UI automation based on opencv</em>
</p>

---

[![Maintainability](https://api.codeclimate.com/v1/badges/de3e2f35842f80a26ed3/maintainability)](https://codeclimate.com/github/williamfzc/fitch/maintainability)
[![PyPI version](https://badge.fury.io/py/fitch.svg)](https://badge.fury.io/py/fitch)

---

# Usage

## As `unittest.TestCase` (recommend)

- Use it as `unittest.TestCase`
- Manage it with `unittest.TestSuite` 
- Run it with `unittest.TestRunner`
- Or some other way you prefer

Need some sample code? 

- view [sample project](sample) for quick start :)
- view [sample_testcase.py](sample_testcase.py) for more detail.

## Freestyle

- Or, you can use it directly, as your wish.
- It can be easily merged into other framework.

view [sample_standalone.py](sample_standalone.py) for detail.

# What it will do

- get screen shot
- detect target picture, and get its location
- check it or operate it

# Installation

Please use python3.

## From pypi (Standard)

```shell
pip install fitch
```

## From source code (dev)

```shell
git clone https://github.com/williamfzc/fitch.git
cd fitch
pip install -e .
```

# Dependencies

- [pyminitouch](https://github.com/williamfzc/pyminitouch): ui operator
- [findit](https://github.com/williamfzc/findit): detect target picture on screen
- [fastcap](https://github.com/williamfzc/fastcap): screen shot
- [pyatool](https://github.com/williamfzc/pyatool): adb operator

# License

[MIT](LICENSE)
