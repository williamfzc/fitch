from fitch import FTestCase
import os
import time


class Case_Wechat(FTestCase):
    f_device_id = '3d33076e'

    def setUp(self):
        cwd = os.path.dirname(__file__)
        self.f_init_store(os.path.join(cwd, 'pictures'))
        self.f_reset()

    def test_enter_wechat(self):
        # find wechat logo, and tap it
        self.f_find_and_tap_target(self.f_pic_store.wechat_logo)
        # wait for starting up
        time.sleep(1)
        # check camera icon
        assert self.f_find_target(self.f_pic_store.wechat_camera_icon), \
            'wechat camera icon not found'

    def tearDown(self):
        self.f_reset()
