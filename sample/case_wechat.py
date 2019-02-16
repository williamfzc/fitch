from fitch import FTestCase
import os
import time


class Case_Wechat(FTestCase):
    f_device_id = '123456F'

    def setUp(self):
        # load your picture store here (build and set your own path)
        cwd = os.path.dirname(__file__)
        self.f_init_store(os.path.join(cwd, 'pictures'))

        # back to home page and clean up
        self.f_reset()

    def test_enter_wechat(self):
        # find wechat logo, and tap it
        self.f_tap_target('wechat_logo')
        # wait for starting up
        time.sleep(1)
        # check camera icon
        assert self.f_find_target('wechat_camera_icon'), \
            'wechat camera icon not found'

    def tearDown(self):
        # back to home page and clean up
        self.f_reset()
