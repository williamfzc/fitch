<h1 align="center">FITCH</h1>
<p align="center">
    <em>Android UI automation based on opencv</em>
</p>

---

[![Maintainability](https://api.codeclimate.com/v1/badges/de3e2f35842f80a26ed3/maintainability)](https://codeclimate.com/github/williamfzc/fitch/maintainability)
[![PyPI version](https://badge.fury.io/py/fitch.svg)](https://badge.fury.io/py/fitch)
[![Documentation Status](https://readthedocs.org/projects/fitch/badge/?version=latest)](https://fitch.readthedocs.io/en/latest/?badge=latest)
[中文README](README.md)

---

# Usage

We Offer a [sample project](https://github.com/williamfzc/fitch-sample) for quickly getting start :)

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

## From source code (Dev)

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
