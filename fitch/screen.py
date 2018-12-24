import subprocess
import os

from fitch import config
from fitch.logger import logger
from fitch.utils import is_device_connected

_ADB = config.ADB_EXECUTOR


class FDevice(object):
    def __init__(self, device_id):
        assert is_device_connected(device_id), 'device {} not connected'.format(device_id)
        self.device_id = device_id
        self.ADB = [_ADB, '-s', device_id]

    def screen_shot(self):
        """ screen shot, get .png file and return its path """
        # TODO for further usage, replacing this function with minicap is a better option
        pic_android_path = '/sdcard/temp_screen.png'
        target_pc_path = os.path.join(config.PROJECT_PATH, 'temp_screen.png')
        if os.path.exists(target_pc_path):
            os.remove(target_pc_path)
        subprocess.check_call([*self.ADB, 'shell', 'screencap', '-p', pic_android_path])
        logger.info('screen shot finished')
        subprocess.check_call([*self.ADB, 'pull', pic_android_path, config.PROJECT_PATH])
        assert os.path.exists(target_pc_path), 'target screen shot file not found'
        logger.info('screen shot saved in {}'.format(target_pc_path))
        return target_pc_path


if __name__ == '__main__':
    d = FDevice('3d33076e')
    print(d.screen_shot())
