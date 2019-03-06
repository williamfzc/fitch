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
    def __init__(self, device_id: str):
        self.device_id = device_id
        self.mnt = MNTDevice(device_id)

    def stop(self):
        self.mnt.stop()

    def tap(self, point: (list, tuple), duration=100):
        x, y = map(int, point)
        logger.info('Tap point: ({}, {})'.format(x, y))
        self.mnt.tap([(x, y)], duration=duration)

        # add 50ms for syncing status
        time.sleep((duration + 50) / 1000)

    def long_tap(self, point: (list, tuple), duration: int=1000):
        self.tap(point, duration)

    def swipe(self, point1: (list, tuple), point2: (list, tuple), duration: int = 1, part: int = 10):
        self.mnt.ext_smooth_swipe([point1, point2], duration=duration, part=part)
        time.sleep((duration + 50) / 1000)


if __name__ == '__main__':
    ap = ActionPlayer('4df189487c7b6fef')
    ap.tap((500, 500))
    ap.stop()
