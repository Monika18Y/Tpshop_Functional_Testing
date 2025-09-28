import unittest
import time
from script.tpshop_cart import TestTPShopCart
from script.tpshop_login import TestTPShopLogin
from script.tpshop_palce_order import TestTPShopPlaceOrder
from tools.HTMLTestRunnerCN import HTMLTestReportCN
from config import BASE_DIR
from utlis import DriverUtil

suite = unittest.TestSuite()

# suite.addTest(unittest.makeSuite(TestTPShopLogin))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTPShopLogin))
# suite.addTest(TestTPShopLogin('test_login'))  # 参数化不能单个调用方法名
# suite.addTest(unittest.makeSuite(TestTPShopCart))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTPShopCart))
# suite.addTest(unittest.makeSuite(TestTPShopPlaceOrder))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTPShopPlaceOrder))

DriverUtil.change_quit_status(False)

# unittest.TextTestRunner().run(suite)
report_name = BASE_DIR + '/report/test_report{}.html'.format(time.strftime('%Y%m%d_%H%M%S'))
with open(report_name, 'wb') as f:
    runner = HTMLTestReportCN(stream=f,
                              verbosity=2,
                              title='web自动化测试',
                              description='python & Edge & window',
                              tester='zhr')
    runner.run(suite)

DriverUtil().change_quit_status(True)
