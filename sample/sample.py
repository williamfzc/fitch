from fitch import config
from fitch.utils import restart_adb
import os

restart_adb()

config.DEFAULT_LOCAL_PIC_DIR = os.path.dirname(__file__)

# load FDevice after config
from fitch.device import FDevice

device = FDevice('123456F')

TARGET_PICTURE_PATH = 'pics/wechat_logo.png'

target_list = device.find_target(TARGET_PICTURE_PATH)
print(target_list)

operator_result = device.tap_target(TARGET_PICTURE_PATH)
print(operator_result)

# stop your device
device.stop()
