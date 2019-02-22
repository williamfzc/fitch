from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from cases.test_wechat import TestWechat
from cases.test_wechat_2 import TestWechat2
from cases import target_device


# and add them in suite
suite = TestSuite([
    TestLoader().loadTestsFromTestCase(TestWechat),
    TestLoader().loadTestsFromTestCase(TestWechat2),
])

runner = HTMLTestRunner(output='sample_suite')
runner.run(suite)
target_device.stop()
