""" work with unittest """
from fitch import FTestCase, FDevice
import unittest


# SET YOUR DEVICE ID, AND USE OUR API DIRECTLY!
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
        # view https://github.com/williamfzc/pyatool for details
        self.f_device.toolkit.switch_airplane(True)

        # find 'stopflag.png' on screen
        flag_point = self.f_find_target(stop_path)

        # assert: existed?
        assert flag_point, 'stopflag not existed!'


# FOR FURTHER USAGE, YOU CAN INIT YOUR DEVICE OUTSIDE, AND THEN SEND IT IN CASE.
# YOU DON'T NEED TO INIT YOUR DEVICE EVERY TIME.
target_device = FDevice('3d33076e')


class DemoATestCase(FTestCase):
    f_device = target_device

    def test_hello(self):
        assert self.f_device.device_id == self.f_device_id
        # do something else?


if __name__ == '__main__':
    unittest.main()
