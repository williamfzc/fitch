import unittest

from fitch import config
from fitch.utils import restart_adb
import os
import time


# 修改配置需要在导入设备之前
config.DEFAULT_PYTHON_EXECUTOR = 'python3'
config.DEFAULT_LOCAL_PIC_DIR = os.path.join(os.path.dirname(__file__), 'pics')

DEVICE_ID = '3d33076e'

from fitch.device import FDevice


class BaseTestCase(unittest.TestCase):
    device: FDevice = None

    @classmethod
    def setUpClass(cls):
        # 重启adb服务，这里只是为了清理一下遗留进程，正式环境可以不需要
        restart_adb()
        cls.device = FDevice(DEVICE_ID)

    @classmethod
    def tearDownClass(cls):
        cls.device.stop()

    # 你可以在此处自定义一些业务相关的公共方法
    # ...


class TestStartWechat(BaseTestCase):
    WECHAT_LOGO_PATH = 'wechat_logo.png'

    def test_start_wechat(self):
        wechat_widget = self.device.get_widget(self.WECHAT_LOGO_PATH)
        self.assertTrue(wechat_widget)

        self.device.click(wechat_widget)
        time.sleep(1)

        wechat_widget = self.device.get_widget(self.WECHAT_LOGO_PATH)
        self.assertFalse(wechat_widget)

    def test_stop_wechat(self):
        self.device.adb_utils.keyevent(4)
        time.sleep(1)

        wechat_widget = self.device.get_widget(self.WECHAT_LOGO_PATH)
        self.assertTrue(wechat_widget)


if __name__ == '__main__':
    unittest.main()
