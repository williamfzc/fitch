""" work with unittest """
from fitch import FTestCase
import unittest


class DemoTestCase(FTestCase):
    f_device_id = '123456F'

    def test_hello(self):
        # check and load pic
        target_path = self.f_check_pic('./target.png')
        stop_path = self.f_check_pic('./stopflag.png')

        # find 'target.png' on screen
        target_point = self.f_find_target(target_path)
        # assert: existed?
        assert target_point, 'target not existed!'
        # and tap it
        self.f_device.player.tap(target_point)
        # use pyatool to operate something else
        self.f_device.toolkit.switch_airplane(True)
        # find 'stopflag.png' on screen
        flag_point = self.f_find_target(stop_path)
        # assert: existed?
        assert flag_point, 'stopflag not existed!'


if __name__ == '__main__':
    unittest.main()
