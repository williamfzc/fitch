from fitch import config
from fitch.utils import restart_adb
import os
import time

# 重启adb服务，这里只是为了清理一下遗留进程，正式环境可以不需要
restart_adb()

# 修改配置需要在导入设备之前
config.DEFAULT_PYTHON_EXECUTOR = 'python3'
config.DEFAULT_LOCAL_PIC_DIR = os.path.join(os.path.dirname(__file__), 'pics')

# 默认情况下会在本地启动临时的findit服务
# 你也可以选择连接到远程的findit服务
# config.REMOTE_MODE = True
# config.FINDIT_SERVER_IP = '127.0.0.1'
# config.FINDIT_SERVER_PORT = 9410

# 在配置完成后就可以开始操作设备了
from fitch.device import FDevice

device = FDevice('3d33076e')

TARGET_PICTURE_PATH = 'wechat_logo.png'

# 寻找目标，返回widget
wechat_widget = device.get_widget(TARGET_PICTURE_PATH)
print(wechat_widget)

# 当然，你的目标图片可能同时出现多次
# 你可以这样获取一个widget列表
wechat_widget_list = device.get_widget_list(TARGET_PICTURE_PATH)
print(wechat_widget_list)

# 在获取widget之后，你可以使用device中的方法操作他们
# FDevice中的方法的操作单元是 FWidget，而不是坐标
# 可参见 https://github.com/williamfzc/fitch/blob/master/fitch/device.py#L145
device.click(wechat_widget)

# 底层的API可通过 player 调用，基于minitouch实现，具备很高的灵活性
# 可以在此基础上自由构建更高级别的API
# player中所有的操作单元是坐标，不应该引入widget的概念
# 可参见 https://github.com/williamfzc/pyminitouch
device.player.fast_swipe([100, 100], [400, 400])

# 除了UI操作，你还可以利用 adbutils 进行方便的adb操作
# 可参见 https://github.com/openatx/adbutils
device.adb_utils.keyevent(3)
time.sleep(2)

# 在完成后记得停止设备
device.stop()
