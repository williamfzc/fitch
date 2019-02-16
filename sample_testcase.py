""" work with unittest """
from fitch import FTestCase, FDevice
import unittest


# SET YOUR DEVICE ID, AND USE OUR API DIRECTLY!
class DemoTestCase(FTestCase):
    f_device_id = '123456F'

    """
    you can also init your device outside
    and send it in, like this:

    OUTSIDE
        target_device = FDevice('123456F')
    
    INSIDE
        class DemoATestCase(FTestCase):
            f_device = target_device
            
    by doing this, you only need to init your device once
    """

    def setUp(self):
        # init picture store for easier usage (i think)
        self.f_init_store('Screenshots')

    def test_hello(self):
        # find 'target.png' on screen
        target_point = self.f_find_target(self.f_pic_store.quickapp_entry)

        # assert: existed?
        assert target_point, 'target not existed!'

        # and tap it
        self.f_device.player.tap(target_point)

        # use pyatool to operate something else
        # view https://github.com/williamfzc/pyatool for details
        self.f_device.toolkit.switch_airplane(True)

        # find 'stopflag.png' on screen
        flag_point = self.f_find_target(self.f_pic_store.quickapp_title)

        # assert: existed?
        assert flag_point, 'title not existed!'


# FOR FURTHER USAGE, YOU CAN INIT YOUR DEVICE OUTSIDE, AND THEN SEND IT IN CASE.
# YOU ONLY NEED TO INIT YOUR DEVICE ONCE.
target_device = FDevice('3d33076e')


class DemoATestCase(FTestCase):
    f_device = target_device

    def test_hello(self):
        assert self.f_device.device_id == self.f_device_id
        # do something else?


if __name__ == '__main__':
    unittest.main()
