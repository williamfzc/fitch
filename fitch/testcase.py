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

from fitch.screen import FDevice
from fitch import detector
from fitch.logger import logger


class FTestCase(unittest.TestCase):
    """
    FTestCase, based on unittest.TestCase.
    Can be easily used by other modules, which support unittest.
    """
    f_device_id = None
    f_device = None

    @classmethod
    def setUpClass(cls):
        cls.f_init_device(cls.f_device_id)

    @classmethod
    def tearDownClass(cls):
        cls.f_stop_device()

    @classmethod
    def f_check_pic(cls, pic_path):
        """ check pic path, and return its abspath """
        # TODO auto load and import pictures from json?
        assert os.path.isfile(pic_path), 'picture {} not found'.format(pic_path)
        pic_abs_path = os.path.abspath(pic_path)
        logger.info('LOAD PICTURE: {}'.format(pic_abs_path))
        return pic_abs_path

    @classmethod
    def f_init_device(cls, device_id):
        """ init device, and return it """
        assert cls.f_device_id, 'should set your device id first, likes `cls.f_device_id="1234F"`'
        assert not cls.f_device, 'device {} already existed, should not be re-init'.format(device_id)
        cls.f_device = FDevice(device_id)
        logger.info('DEVICE {} INIT FINISHED'.format(device_id))
        return cls.f_device

    @classmethod
    def f_find_target(cls, target_pic_path):
        """ find target, and get its position """
        assert cls.f_device, 'device not found, init it first, likes `cls.f_device_id="1234F"`'
        pic_path = cls.f_device.screen_shot()
        result = detector.detect(target_pic_path, pic_path)
        os.remove(pic_path)

        try:
            target_point = detector.cal_location(result)
        except AssertionError:
            # if not found, return None
            return None

        return target_point

    @classmethod
    def f_stop_device(cls):
        """ stop device after usage """
        cls.f_device and cls.f_device.stop()
        logger.info('DEVICE {} STOPPED'.format(cls.f_device_id))
