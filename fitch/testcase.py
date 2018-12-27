import unittest

from fitch.screen import FDevice
from fitch import detector


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
    def f_init_device(cls, device_id):
        """ init device, and return it """
        assert cls.f_device_id, 'should set your device id first, likes `cls.f_device_id="1234F"`'
        assert not cls.f_device, 'device {} already existed, should not be re-init'.format(device_id)
        cls.f_device = FDevice(device_id)
        return cls.f_device

    @classmethod
    def f_find_target(cls, target_pic_path):
        """ find target, and get its position """
        assert cls.f_device, 'device not found, init it first, likes `cls.f_device_id="1234F"`'
        pic_path = cls.f_device.screen_shot()
        result = detector.detect(target_pic_path, pic_path)

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
