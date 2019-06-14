from fitch import config
from fitch.utils import restart_adb
import os

# 重启adb服务，这里只是为了清理一下遗留进程，正式环境可以不需要
restart_adb()

# 修改配置需要在导入设备之前
config.DEFAULT_PYTHON_EXECUTOR = 'python3'
config.DEFAULT_LOCAL_PIC_DIR = os.path.dirname(__file__)

# 在配置完成后就可以开始操作设备了
from fitch.device import FDevice

device = FDevice('3d33076e')

TARGET_PICTURE_PATH = 'pics/wechat_logo.png'

# 寻找目标，返回三维列表
target_list = device.find_target(TARGET_PICTURE_PATH)
# [[[88.0, 811.0]]]
# 即我的手机上的微信图标出现了一次，坐标位于 [88.0, 811.0]
print(target_list)

# 之所以返回三维列表的目的是：
# 你可以在一个屏幕上同时检测多个目标
# 同一个屏幕上同一个目标可能在不同地方重复出现
# 另一维就是点的x与y坐标了

# 我将我手机上的微信图标复制了一个，再次寻找，返回值变成了：
# [[[88.0, 811.0], [268.0, 811.0]]]
# 可以看到，它出现了两次

# 除此以外，你可以像这样，同时寻找多张图片：
target_list = device.find_target([TARGET_PICTURE_PATH, TARGET_PICTURE_PATH])
# [[[88.0, 811.0], [268.0, 811.0]], [[88.0, 811.0], [268.0, 811.0]]]
print(target_list)

# 寻找是最关键的部分，之后所有的API都是基于上述API来完成的
# 寻找并点击
operator_result = device.tap_target(TARGET_PICTURE_PATH)
# 操作成功与否 True or False
print(operator_result)

# 底层的API可通过 player 调用，基于minitouch实现，具备很高的灵活性
# 可以在此基础上自由构建更高级别的API
# 可参见 https://github.com/williamfzc/pyminitouch
device.player.fast_swipe([100, 100], [400, 400])

# 在完成后记得停止设备
device.stop()
