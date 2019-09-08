import unittest
import logging
from Appium_test.page_object.myunit import StartEnd
from Appium_test.page_object.loginView import LoginView

class TestLogin(StartEnd):

    def test_login_8171(self):
        logging.info('=====test_login_8171=====')
        l= LoginView(self.driver)
        l.login_action('15980898171', '010707')

    def test_login_8172(self):
        logging.info('=====test_login_8172=====')
        l = LoginView(self.driver)
        l.login_action('15980898172', '010707')

    def test_login_8173(self):
        logging.info('=====test_login_8173=====')
        l = LoginView(self.driver)
        l.login_action('15980898173', '010707')

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test_login_8171'))
    run = unittest.TextTestRunner
    run(suite)