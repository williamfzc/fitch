import tempfile

from fitch.logger import logger
from fitch.utils import is_device_connected
from fitch.player import ActionPlayer

from fastcap import MNCDevice


class FDevice(object):
    def __init__(self, device_id):
        assert is_device_connected(device_id), 'device {} not connected'.format(device_id)
        self.device_id = device_id
        self.mnc = MNCDevice(device_id)
        self.player = ActionPlayer(device_id)

    def screen_shot(self):
        """ screen shot and return its path """
        temp_pic = tempfile.NamedTemporaryFile('w+', delete=False, suffix='.png')
        temp_pic_name = temp_pic.name
        self.mnc.screen_shot()
        self.mnc.export_screen(temp_pic_name)
        logger.info('screen shot saved in {}'.format(temp_pic_name))
        return temp_pic_name

    def stop(self):
        self.player.stop()
        logger.info('fDevice {} stopped'.format(self.device_id))


if __name__ == '__main__':
    d = FDevice('3d33076e')
    d.screen_shot()
    d.stop()
