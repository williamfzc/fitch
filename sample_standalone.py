""" work standalone """
from fitch import FDevice, detector
from fitch.utils import restart_adb


# restart adb server (optional)
restart_adb()

device_id = '123456F'
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
