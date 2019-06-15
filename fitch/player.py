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
from pyminitouch import MNTDevice, CommandBuilder


class ActionPlayer(object):
    """ base, low level API here """
    def __init__(self, device_id: str):
        self.device_id = device_id
        self.mnt = MNTDevice(device_id)
        self.cmd_builder = CommandBuilder()

    def stop(self):
        self.mnt.stop()

    def tap(self, point: (list, tuple), duration: int = 100, no_up: bool = None):
        self.mnt.tap([point], duration=duration, no_up=no_up)

    def short_tap(self, point: (list, tuple), *args, **kwargs):
        self.tap(point, duration=100, *args, **kwargs)

    def long_tap(self, point: (list, tuple), *args, **kwargs):
        self.tap(point, duration=1000, *args, **kwargs)

    def swipe(self,
              point1: (list, tuple),
              point2: (list, tuple),
              duration: int = None,
              part: int = None,
              no_down: bool=None,
              no_up: bool=None):

        if not duration:
            duration = 5
        if not part:
            part = 50

        self.mnt.ext_smooth_swipe(
            [point1, point2],
            duration=duration,
            part=part,
            no_down=no_down,
            no_up=no_up,
        )

    def fast_swipe(self,
                   point1: (list, tuple),
                   point2: (list, tuple),
                   *args, **kwargs):
        self.swipe(point1, point2, duration=5, part=100, *args, **kwargs)

    def slow_swipe(self,
                   point1: (list, tuple),
                   point2: (list, tuple),
                   *args, **kwargs):
        self.swipe(point1, point2, duration=50, part=100, *args, **kwargs)


if __name__ == '__main__':
    ap = ActionPlayer('4df189487c7b6fef')
    ap.tap((500, 500))
    ap.stop()
