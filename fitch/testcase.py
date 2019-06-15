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
import unittest
import os

from fitch.device import FDevice, FDeviceManager
from fitch.logger import logger
from fitch import config
import warnings

warnings.warn('fitch.testcase already DEPRECATED!! and should not be used any more :(')

class FPic(object):
    def __init__(self, pic_path: str):
        # /path/to/pic/pic1.png
        self.path = pic_path
        assert self.is_existed(), '{} not existed'.format(pic_path)
        # pic1.png
        self.file_name = pic_path.split(os.sep)[-1]
        # pic1
        self.name = self.file_name.split('.')[0]

    def is_existed(self):
        return bool(os.path.isfile(self.path))


class FPicStore(object):
    """ load pictures from dir, and store them here """

    def __init__(self):
        self.f_pic_dict = dict()

    def __getattr__(self, item):
        if item in self.f_pic_dict:
            return self.f_pic_dict[item].path
        if config.REMOTE_MODE:
            return item
        raise FileNotFoundError('picture {} file not found'.format(item))

    def load(self, pic_dir_path):
        assert os.path.isdir(pic_dir_path), '{} not a dir'.format(pic_dir_path)

        for each_pic_path in [os.path.join(pic_dir_path, i) for i in os.listdir(pic_dir_path)]:
            each_f_pic = FPic(each_pic_path)
            each_pic_name = each_f_pic.name
            self.f_pic_dict[each_pic_name] = each_f_pic
            logger.debug('Load picture [{}] from [{}]'.format(each_pic_name, each_pic_path))


class FTestCase(unittest.TestCase):
    """
    Based on unittest.TestCase.
    Can be easily used by other modules, which supports unittest.
    """
    f_device_id: str = None
    f_device: FDevice = None

    # if it is False, device would not be killed at the end of test case
    f_device_kill_after_usage: bool = True

    # root path of pic store
    f_pic_store_root: str = None
    f_pic_store: FPicStore = FPicStore()

    # current screen shot will be saved here, if you already called f_save_pic.
    f_runtime_pic_dir_path: str = None

    @classmethod
    def setUpClass(cls):
        if not cls.f_device:
            cls.f_init_device(cls.f_device_id)
        cls.f_device_id = cls.f_device.device_id

        if cls.f_runtime_pic_dir_path is not None:
            cls.f_save_runtime_pic(cls.f_runtime_pic_dir_path)
        logger.debug('Case [{}] setup finished'.format(cls.__name__))

    @classmethod
    def tearDownClass(cls):
        if cls.f_device and cls.f_device_kill_after_usage:
            cls.f_stop_device()
            cls.f_device = None
        cls.f_device_id = None
        logger.debug('Case [{}] teardown finished'.format(cls.__name__))

    @classmethod
    def f_save_runtime_pic(cls, target_dir_path: str):
        """ will save current screen shot to target_dir_path after f_find_target, for checking after test """
        if not os.path.isdir(target_dir_path):
            os.makedirs(target_dir_path)
        cls.f_runtime_pic_dir_path = target_dir_path

    @classmethod
    def f_init_store(cls, pic_dir_path: str):
        """
        init pic store, and you can access them directly. it can be called multiple times.
        """
        root_path = cls.f_pic_store_root or os.getcwd()
        full_pic_dir_path = os.path.join(root_path, pic_dir_path)
        cls.f_pic_store.load(full_pic_dir_path)

    @classmethod
    def f_init_device(cls, device_id: str) -> FDevice:
        """ init device, and return it """
        assert cls.f_device_id, 'should set your device id first, likes `cls.f_device_id="1234F"`'
        assert not cls.f_device, 'device {} already existed, should not be re-init'.format(device_id)

        cls.f_device = FDeviceManager.add(device_id)
        logger.debug('Device [{}] init finished'.format(device_id))
        return cls.f_device

    @classmethod
    def f_stop_device(cls):
        """ stop device after usage """
        cls.f_device = None
        FDeviceManager.remove(cls.f_device_id)
        logger.debug('Device [{}] stopped'.format(cls.f_device_id))

    @classmethod
    def f_find_target(cls, target_pic_path: str) -> (list, tuple):
        """ find target, and get its position """
        target_pic_path = cls._format_pic_path(target_pic_path)
        assert cls.f_device, 'device not found, init it first, likes `cls.f_device_id="1234F"`'
        current_screen_target_path = cls._get_current_screen_target_path(target_pic_path)
        return cls.f_device._find_target(target_pic_path, save_pic=current_screen_target_path)

    @classmethod
    def f_tap_target(cls, target_pic_path: str, duration: int = 100):
        """ find target, get its position, and tap it """
        target_pic_path = cls._format_pic_path(target_pic_path)
        current_screen_target_path = cls._get_current_screen_target_path(target_pic_path)
        return cls.f_device.tap_target(target_pic_path, duration, save_pic=current_screen_target_path)

    @classmethod
    def f_snapshot(cls, name: str = None) -> str:
        """ take a screen shot and do nothing, for checking after test. """
        assert cls.f_runtime_pic_dir_path is not None, 'set f_runtime_pic_dir_path first'

        # specific name
        if name:
            # add suffix: '.png'
            pic_suffix = '.png'
            if not name.endswith(pic_suffix):
                name += pic_suffix
            pic_path = os.path.join(cls.f_runtime_pic_dir_path, name)
        # random name
        else:
            pic_path = cls.f_runtime_pic_dir_path

        logger.info('Snapshot saved in [{}]'.format(pic_path))
        cls.f_device.screen_shot(save_to=pic_path)
        return pic_path

    @classmethod
    def f_reset(cls):
        """
        (NOT IMPLEMENTED) back to home page, and clean up backstage
        """

        """
        How to clean up backstage using adb? I have no idea yet.
        You'd better implement it by yourself, eg:

            def clean_recent(self):
                self.f_reset()
                self.f_device.toolkit.input_key_event(187)
                time.sleep(1)

                self.f_init_store('pictures/global')
                self.f_tap_target('x')
                time.sleep(2)
        """
        logger.warning('FUNCTION f_reset NOT IMPLEMENTED NOW')

    @classmethod
    def _format_pic_path(cls, pic_path: str):
        """ try to load picture from pic_store, if pic_path is invalid """
        # support using name directly
        if not os.path.isfile(pic_path):
            if hasattr(cls, 'f_pic_store'):
                return getattr(cls.f_pic_store, pic_path)
            raise FileNotFoundError('PICTURE [{}] NOT FOUND'.format(pic_path))
        # do nothing if existed
        return pic_path

    @classmethod
    def _get_current_screen_target_path(cls, target_pic_path: str):
        """ get basename of target_pic_path, and generate target path of current screenshot """
        new_pic_name = '{}_{}'.format(cls.__name__, os.path.basename(target_pic_path))
        if cls.f_runtime_pic_dir_path:
            return os.path.join(cls.f_runtime_pic_dir_path, new_pic_name)
        return None
