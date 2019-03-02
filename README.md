<h1 align="center">FITCH</h1>
<p align="center">
    <em>基于 opencv 的 Android UI自动化解决方案</em>
</p>

---

[![Maintainability](https://api.codeclimate.com/v1/badges/de3e2f35842f80a26ed3/maintainability)](https://codeclimate.com/github/williamfzc/fitch/maintainability)
[![PyPI version](https://badge.fury.io/py/fitch.svg)](https://badge.fury.io/py/fitch)
[![Documentation Status](https://readthedocs.org/projects/fitch/badge/?version=latest)](https://fitch.readthedocs.io/en/latest/?badge=latest)
[English README](README_en.md)

---

# 使用

> 推荐使用类似 [scrcpy](https://github.com/Genymobile/scrcpy) 的工具用于在PC端方便地截图。

## 将它当作 `unittest.TestCase`（推荐）

`fitch.testcase.FTestCase` 继承自原生的 `unittest.TestCase`，使其能够无缝替换到后者被使用的场景中，与其他已有的测试框架结合。

需要一些例子? 通过一个 [简单项目](sample) 来快速入门 :)

## Docker镜像 （只支持linux）

fitch提供了docker镜像，你只需要直接使用它:

```shell
git clone https://github.com/williamfzc/fitch.git
cd fitch
docker run --rm \
    --privileged \
    -v /dev/bus/usb:/dev/bus/usb \
    -v `pwd`/sample:/usr/src/app \
    williamfzc/fitch
```

如果你需要更加细致的设备管理，可以通过 `--device`：

```shell
--device /dev/bus/usb/001:/dev/bus/usb/001:rwm
```

在实际项目中的应用可以参照 [doringland/ud4d](https://github.com/doringland/ud4d)。

## 像普通的python库一样使用它

如果上面的方式不能满足你的需要，你可以直接调用API以构建自己的程序，或将fitch应用到你自己的库中:

```python
from fitch import FDevice
from fitch.utils import restart_adb


# 重启adb（可选，这里只是为了让环境更干净）
restart_adb()

device_id = '123456F'
template_path = 'target.png'

device = FDevice(device_id)
device.tap_target(template_path)

# 在使用后需要主动停止
device.stop()
```

可以直接浏览 [screen.py](fitch/screen.py)或阅读 [API文档](https://fitch.readthedocs.io/en/latest/#) 进行更加详细的了解。

# 如何运作

得益于 [minitouch](https://github.com/openstf/minitouch) / [minicap](https://github.com/openstf/minicap) / [opencv](https://github.com/skvark/opencv-python) 的存在，让 fitch 能够维持高效地运转，即便它是用python写的。

- 获得手机屏幕截图（[fastcap](https://github.com/williamfzc/fastcap)）
- 在截图上寻找目标模板，并确定它的位置（[findit](https://github.com/williamfzc/findit)）
- 进行检查或操作（[pyminitouch](https://github.com/williamfzc/pyminitouch) & [pyatool](https://github.com/williamfzc/pyatool)）

# 安装

请使用python3。

## 从 pypi 安装

```shell
pip install fitch
```

## 从 github源码 安装

```shell
git clone https://github.com/williamfzc/fitch.git
cd fitch
pip install -e .
```

# 依赖库

- [pyminitouch](https://github.com/williamfzc/pyminitouch): ui操作
- [findit](https://github.com/williamfzc/findit): 目标检测
- [fastcap](https://github.com/williamfzc/fastcap): 快速获取截图
- [pyatool](https://github.com/williamfzc/pyatool): 非ui操作

# 协议

[MIT](LICENSE)
