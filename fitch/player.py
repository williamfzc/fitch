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
from pyminitouch import MNTDevice
import time

from fitch.logger import logger


class ActionPlayer(object):
    def __init__(self, device_id):
        self.device_id = device_id
        self.mnt = MNTDevice(device_id)

    def stop(self):
        self.mnt.stop()

    def tap(self, point, duration=100):
        x, y = map(int, point)
        logger.info('tap point: ({}, {})'.format(x, y))
        self.mnt.tap([(x, y)], duration=duration)
        time.sleep(duration / 1000)


if __name__ == '__main__':
    ap = ActionPlayer('4df189487c7b6fef')
    ap.tap((500, 500))
    ap.stop()
