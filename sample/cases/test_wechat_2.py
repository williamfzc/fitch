import time

from .base_case import SFTestCase
from . import target_device


class TestWechat2(SFTestCase):
    f_device = target_device
    f_device_kill_after_usage = False

    def setUp(self):
        # save screenshot after test
        self.f_save_pic('./cur_screen_shot')

        # load your picture store here (build and set your own path)
        self.f_init_store('pictures/wechat')
        # need another one?
        self.f_init_store('pictures/global')

        # back to home page and clean up
        self.clean_recent()
        time.sleep(1)

    def test_enter_wechat(self):
        # find wechat logo, and tap it
        self.f_tap_target('wechat_logo')
        # wait for starting up
        time.sleep(1)
        # check camera icon
        assert self.f_find_target('wechat_camera_icon'), 'wechat camera icon not found'

    def tearDown(self):
        # back to home page and clean up
        self.clean_recent()
