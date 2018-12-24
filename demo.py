from fitch.screen import FDevice
from fitch.detector import detect
from fitch.player import tap


device_id = '3d33076e'
template_path = 'target.png'

device = FDevice(device_id)
pic_path = device.screen_shot()
result = detect(template_path, pic_path)
target_point = result['data'][template_path]['max_loc']
tap(device_id, target_point)
