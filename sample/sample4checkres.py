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


def build_test_func(case_config):
    def test_func(test_case):
        device: FDevice = test_case.device

        package_name = case_config['package_name']
        activity_name = case_config['activity_name']
        pic_name = case_config['pic_name']

        device.adb_utils.app_start(package_name, activity_name)
        time.sleep(2)

        assert not device.get_widget(pic_name)
        device.adb_utils.keyevent(3)
        device.adb_utils.keyevent(4)

    return test_func


case_list = [
    {
        'case_name': 'wechat',
        'package_name': 'com.tencent.mm',
        'activity_name': 'com.tencent.mm.ui.LauncherUI',
        'pic_name': 'wechat_logo.png'
        # 还可以添加一些别的参数
        # 例如终点图片
        # ...
    },
    {
        'case_name': 'settings',
        'package_name': 'com.android.settings',
        'activity_name': None,
        'pic_name': 'wechat_logo.png'
    },
    # ...
]

for index, each_case in enumerate(case_list):
    each_func_name = f'test_{each_case}'
    setattr(BaseTestCase, each_func_name, build_test_func(each_case))

# now, test cases are already in BaseTestCase !
if __name__ == '__main__':
    unittest.main()
