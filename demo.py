from fitch.screen import FDevice
from fitch.detector import detect
from fitch.player import tap
from fitch import config


device_id = '3d33076e'
template_path = 'target.png'

# get screen
device = FDevice(device_id)
pic_path = device.screen_shot()

# find point
result = detect(template_path, pic_path)
sim = result['data'][template_path]['max_val']
assert sim > config.CV_THRESHOLD, 'target point not found'
target_point = result['data'][template_path]['max_loc']

# tap it
tap(device_id, target_point)
