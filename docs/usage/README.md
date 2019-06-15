# 使用

## 完整的例子

这个例子应该可以解决大多数问题：[sample.py](https://github.com/williamfzc/fitch/blob/master/sample/sample.py)

## 结合unittest的例子

与unittest一同使用的示例：[sample4unittest.py](https://github.com/williamfzc/fitch/blob/master/sample/sample4unittest.py)

暂时不推荐使用 pytest：

- unittest可定制化更强，pytest相对更适合轻量化的场景
- 目前用pytest有偶现的奇怪bug

## 更真实的例子：动态生成用例并用于遍历app

有些情况下，我们可能需要对一些资源进行重复性较高的校验工作。

这个例子将告诉你，如何利用 fitch 动态进行用例的生成与校验：[sample4checkres.py](https://github.com/williamfzc/fitch/blob/master/sample/sample4checkres.py)

## 创建与销毁

FDevice的使用有两种方式。如果只是简单功能，你可以选择with。它会在使用结束后自动销毁设备：

```python
from fitch.device import safe_device

with safe_device('123456F') as device:
    print(device.device_id)
```

如果你希望自主控制设备：

```python
from fitch.device import FDevice

device = FDevice('123456F')

# do something
print(device.device_id)

# stop your device
device.stop()
```

## 远程模式

基于 [findit](https://github.com/williamfzc/findit)，你可以将目标图片配置到远程，之后直接使用，这样更有利于大量图片的管理。

把图片配置到远程（例子中放置在 `path/to/your/remote` 目录下）：

![](../pics/findit_server_management.png)

然后像调用本地图片一样调用它即可：

```python
from fitch import config

# 配置你的findit服务器
config.REMOTE_MODE = True
config.FINDIT_SERVER_IP = '172.17.12.34'
config.FINDIT_SERVER_PORT = 29412

# 直接使用你的远端图片
TARGET_PICTURE_PATH = 'path/to/your/remote/picture.png'
target_widget = device.get_widget(TARGET_PICTURE_PATH)
```

关于findit服务器配置可参考：https://williamfzc.github.io/findit/#/usage/client+server

## 界面无关的额外操作

除了ui操作外，我们可能需要一些类似adb的界面无关操作：

```python
device.adb_utils.switch_airplane(True)
```

可以通过 adb_utils 调用 [adbutils](https://github.com/openatx/adbutils) 中的功能。
