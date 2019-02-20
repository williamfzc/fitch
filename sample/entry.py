from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from cases.test_wechat import TestWechat


# load your cases
test_wechat = TestLoader().loadTestsFromTestCase(TestWechat)

# and add them in suite
suite = TestSuite([
    test_wechat,
])

runner = HTMLTestRunner(output='sample_suite')
runner.run(suite)
