from fitch.screen import FDevice
from fitch import detector
from fitch.utils import restart_adb


restart_adb()

device_id = '4df189487c7b6fef'
template_path = 'target.png'

# get screen
device = FDevice(device_id)
pic_path = device.screen_shot()

# find point
result = detector.detect(template_path, pic_path)
target_point = detector.cal_location(result)

# tap it
device.player.tap(target_point)
device.stop()
