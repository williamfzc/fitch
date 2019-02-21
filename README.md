<h1 align="center">FITCH</h1>
<p align="center">
    <em>Android UI automation based on opencv</em>
</p>

---

[![Maintainability](https://api.codeclimate.com/v1/badges/de3e2f35842f80a26ed3/maintainability)](https://codeclimate.com/github/williamfzc/fitch/maintainability)
[![PyPI version](https://badge.fury.io/py/fitch.svg)](https://badge.fury.io/py/fitch)
[![Documentation Status](https://readthedocs.org/projects/fitch/badge/?version=latest)](https://fitch.readthedocs.io/en/latest/?badge=latest)
[中文README](README_CN.md)

---

# Usage

> You can use some tools like [scrcpy](https://github.com/Genymobile/scrcpy) to monitor screen, and get screenshot conveniently.

## As `unittest.TestCase` (recommend)

- Use it as `unittest.TestCase`
- Manage it with `unittest.TestSuite` 
- Run it with `unittest.TestRunner`
- Or some other way you prefer

Need some sample code? 

- [API Documentation](https://fitch.readthedocs.io/en/latest/#)
- view [sample project](sample) for quick start :)
- view [sample_testcase.py](sample_testcase.py) for more detail.

## Docker Container (Linux only)

Try this:

```shell
git clone https://github.com/williamfzc/fitch.git
cd fitch
docker run --rm \
    --privileged \
    -v /dev/bus/usb:/dev/bus/usb \
    -v `pwd`/sample:/usr/src/app \
    williamfzc/fitch
```

For device management, you can use `--device`：

```shell
--device /dev/bus/usb/001:/dev/bus/usb/001:rwm
```

For further usage, view [doringland/ud4d](https://github.com/doringland/ud4d).

## As a normal package

Or, more flexible:

```python
from fitch import FDevice
from fitch.utils import restart_adb


# restart adb server (optional)
restart_adb()

device_id = '123456F'
template_path = 'target.png'

device = FDevice(device_id)
device.tap_target(template_path)

# must stop it after usage
device.stop()
```

View [screen.py](fitch/screen.py) for detail.

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
