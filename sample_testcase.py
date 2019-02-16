""" work with unittest """
from fitch import FTestCase, config
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

        # you can set target threshold by doing this
        # 0 ~ 1.0, default to 0.8
        config.CV_THRESHOLD = 0.85

    def test_hello(self):
        # find 'target.png' on screen
        target_point = self.f_find_target(self.f_pic_store.quickapp_entry)

        # if you want to use some special pictures, you can:
        # target_point = self.f_find_target('/abspath/to/your/pic')

        # assert: existed?
        assert target_point, 'target not existed!'

        # and tap it
        self.f_device.player.tap(target_point)

        # use pyatool to operate something else
        # view https://github.com/williamfzc/pyatool for details
        self.f_device.toolkit.switch_airplane(True)
        self.f_device.toolkit.switch_airplane(False)

        # find 'stopflag.png' on screen
        flag_point = self.f_find_target(self.f_pic_store.quickapp_title)

        # assert: existed?
        assert flag_point, 'title not existed!'


if __name__ == '__main__':
    unittest.main()
