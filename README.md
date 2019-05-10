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

我们提供了一个[实例项目](https://github.com/williamfzc/fitch-sample)用于让开发者快速了解熟悉 fitch :)

它非常简单！

# 如何运作

![structure](./docs/structure.svg)

得益于 [minitouch](https://github.com/openstf/minitouch) / [minicap](https://github.com/openstf/minicap) / [opencv](https://github.com/skvark/opencv-python) 的存在，让 fitch 能够维持高效地运转，即便它是用python写的。

- 获得手机屏幕截图（[fastcap](https://github.com/williamfzc/fastcap)）
- 在截图上寻找目标模板，并确定它的位置（[findit](https://github.com/williamfzc/findit)）
- 进行检查或操作（[pyminitouch](https://github.com/williamfzc/pyminitouch) & [pyatool](https://github.com/williamfzc/pyatool)）

# 安装

Python 3.6 +

## 从 pypi 安装

```shell
pip install fitch
```

## 从 github源码 安装

如果你希望获取一些还未release的新特性，你可以直接通过源码安装。

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
