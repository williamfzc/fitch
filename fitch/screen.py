"""
MIT License

Copyright (c) 2018 williamfzc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import tempfile

from fitch.logger import logger
from fitch.utils import is_device_connected
from fitch.player import ActionPlayer

from fastcap import MNCDevice
from pyatool import PYAToolkit


class FDevice(object):
    def __init__(self, device_id: str):
        assert is_device_connected(device_id), 'device {} not connected'.format(device_id)
        self.device_id = device_id
        self.mnc = MNCDevice(device_id)
        self.player = ActionPlayer(device_id)
        self.toolkit = PYAToolkit(device_id)

    def screen_shot(self) -> str:
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
