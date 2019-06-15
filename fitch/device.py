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
import os
import shutil
import uuid
import atexit
import contextlib
import typing
import collections

from fitch.utils import is_device_connected
from fitch.player import ActionPlayer
from fitch import detector, config

from loguru import logger
from fastcap import MNCDevice
from pyatool import PYAToolkit
from adbutils import adb, AdbDevice


class FWidget(object):
    Point = collections.namedtuple('Point', ['x', 'y'])

    def __init__(self, name: str, position: typing.Union[tuple, list]):
        self.name = name
        self.position = self.Point(*position)

    def __str__(self):
        return f'<fitch.device.FWidget object name={self.name} position={self.position}>'


class FDevice(object):
    """ device object, and high level API """

    def __init__(self, device_id: str):
        assert is_device_connected(device_id), 'device {} not connected'.format(device_id)
        self.device_id: str = device_id

        self.mnc: MNCDevice = None
        self.player: ActionPlayer = None
        self.toolkit: PYAToolkit = None
        self.adb_utils: AdbDevice = None

        self.start()

    def start(self):
        """ start device """
        self.mnc = MNCDevice(self.device_id)
        self.player = ActionPlayer(self.device_id)
        self.toolkit = PYAToolkit(self.device_id)
        self.adb_utils = adb.device(serial=self.device_id)

        logger.debug('FDevice [{}] started'.format(self.device_id))

    def stop(self):
        """ stop device, and clean up """
        self.player and self.player.stop()

        self.mnc = None
        self.player = None
        self.toolkit = None

        logger.debug('FDevice [{}] stopped'.format(self.device_id))

    def reset(self):
        """ stop and restart device """
        self.stop()
        self.start()

    def screen_shot(self, save_to=None) -> str:
        """ screen shot and return its path (YOU SHOULD REMOVE IT BY YOURSELF!) """
        self.mnc.screen_shot()

        # save to specific place
        if save_to:
            if os.path.isdir(save_to):
                pic_name = '{}.png'.format(uuid.uuid1())
                final_path = os.path.join(save_to, pic_name)
            else:
                final_path = save_to
        # use tempfile
        else:
            temp_pic = tempfile.NamedTemporaryFile('w+', delete=False, suffix='.png')
            temp_pic_name = temp_pic.name
            final_path = temp_pic_name

        self.mnc.export_screen(final_path)
        logger.debug('Screenshot saved in [{}]'.format(final_path))
        return final_path

    def _find_target(self,
                     target_path: typing.Union[list, tuple],
                     save_pic: str = None) -> typing.Union[list, None]:
        """ base API, should not be directly used I think. find target pic in screen, and get widget list (or None) """
        pic_path = self.screen_shot()

        try:
            result_dict = detector.detect(target_path, pic_path)
            logger.info(f'detector result: {result_dict}')
            assert result_dict.values()

            result_list = list()
            for each_target_name, each_target_result in result_dict.items():
                # each target result may contains multi points
                for each_point in each_target_result:
                    each_target = FWidget(each_target_name, each_point)
                    result_list.append(each_target)

        except AssertionError as e:
            if config.STRICT_MODE:
                raise e

            # if not found, return None
            return None
        else:
            return result_list
        finally:
            # always clean temp pictures
            if save_pic:
                shutil.copy(pic_path, save_pic)
            os.remove(pic_path)

    # --- user API below ---
    def get_screen_size(self) -> tuple:
        """ (width, height) """
        return self.adb_utils.window_size()

    def get_widget_list(self, target_path: str, *args, **kwargs) -> typing.Union[list, None]:
        target_path = [target_path]

        target_result_list = self._find_target(target_path, *args, **kwargs)
        if not target_result_list:
            return None
        return target_result_list

    def get_widget(self, target_path: str, *args, **kwargs) -> typing.Union[FWidget, None]:
        return self.get_widget_list(target_path, *args, **kwargs)[0]

    def click(self, target_widget: FWidget):
        self.player.short_tap(target_widget.position)

    def long_click(self, target_widget: FWidget):
        self.player.long_tap(target_widget.position)

    def drag_and_drop(self, widget_1: FWidget, widget_2: FWidget):
        self.player.long_tap(widget_1.position, no_up=True)
        self.player.fast_swipe(widget_1.position, widget_2.position, no_down=True)

    def swipe_screen(self, start: str, end: str):
        """ use 'w', 's', 'a', 'd' and 'c' (center) to set the src and dst """
        width, height = self.get_screen_size()
        point_dict = {
            'w': (width / 2, 0),
            's': (width / 2, height),
            'a': (0, height / 2),
            'd': (width, height / 2),
            'c': (width / 2, height / 2),
        }
        assert (start in point_dict) and (end in point_dict), 'start and end should be selected from: [w, s, a, d, c]'
        self.player.fast_swipe(point_dict[start], point_dict[end])


@contextlib.contextmanager
def safe_device(device_id: str) -> FDevice:
    """ support 'with' """
    new_device = FDevice(device_id)
    try:
        yield new_device
    finally:
        new_device.stop()


class FDeviceManager(object):
    _device_dict = dict()

    @classmethod
    def add(cls, target_device_id: str) -> FDevice:
        if not cls.is_device_available(target_device_id):
            new_device = FDevice(target_device_id)
            cls._device_dict[target_device_id] = new_device
            logger.debug('Device [{}] register finished'.format(target_device_id))
            return new_device

        # or, reuse old device
        logger.debug('Device [{}] already registered, reuse'.format(target_device_id))
        return cls._device_dict[target_device_id]

    @classmethod
    def remove(cls, target_device_id: str):
        if not cls.is_device_available(target_device_id):
            logger.warning('DEVICE [{}] NOT EXISTED')
            return
        target_device = cls._device_dict[target_device_id]
        target_device.stop()
        del cls._device_dict[target_device_id]

    @classmethod
    def is_device_available(cls, device_id: str) -> bool:
        return device_id in cls._device_dict

    @classmethod
    def clean(cls):
        device_id_list = list(cls._device_dict.keys())
        for each_device_id in device_id_list:
            cls.remove(each_device_id)


# TODO auto-kill or managed by developer?
atexit.register(FDeviceManager.clean)

if __name__ == '__main__':
    with safe_device('3d33076e') as d:
        d.screen_shot('../docs')

    # normal way
    # d = FDevice('3d33076e')
    # d.screen_shot('../docs')
    # d.stop()
