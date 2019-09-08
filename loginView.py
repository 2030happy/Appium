import logging
from Appium_test.page_object.common_fun import Common
from Appium_test.page_object.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

class LoginView(Common):

    loginBtn = (By.ID, 'btnLogin')

    # 登录账号
    def login_action(self, username, password):
        self.check_switchEnv()
        self.check_testEnv()
        self.check_confirmBtn()

        logging.info('=====login_action=====')
        logging.info('username is: %s' %username)
        sleep(5)
        self.driver.find_element_by_id("ivHomeChildAvatar").click()
        elem1 = self.driver.find_element_by_id("tilLoginCellphone")
        elems1 = elem1.find_elements_by_class_name("android.widget.FrameLayout")
        elems1[0].clear()
        # 输入账号
        elems1[0].send_keys(username)

        logging.info('password is: %s' %password)
        elem2 = self.driver.find_element_by_id("vcilTilValidateCode")
        elems2 = elem2.find_elements_by_class_name("android.widget.FrameLayout")
        elems2[0].clear()
        # 输入验证码
        elems2[0].send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished')

if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('15980898171', '010707')
