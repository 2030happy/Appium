import logging
from time import sleep
from Appium_test.page_object.baseView import  BaseView
from Appium_test.page_object.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class Common(BaseView):
    switchBtn = (By.XPATH, "//android.widget.Button[@text='切换环境']")
    testEnv = (
        By.XPATH, "//android.widget.CheckedTextView[@text='测试' and @index=1]")
    confirmBtn = (By.ID, "button1")
    # 切换到测试环境
    def check_switchEnv(self):
        logging.info("====check_witchEnv====")
        try:
            element = self.driver.find_element(*self.switchBtn)
        except NoSuchElementException:
            logging.info('切换按钮不存在')
        else:
            logging.info("click switchBtn")
            element.click()
        sleep(1)

    def check_testEnv(self):
        logging.info("====check_testEnv====")
        try:
            element = self.driver.find_element(*self.testEnv)
        except NoSuchElementException:
            logging.info("测试环境不存在")
        else:
            logging.info("click testEnv")
            element.click()

    def check_confirmBtn(self):
        logging.info("=====check_confirmBtn=====")
        try:
            element = self.driver.find_element(*self.confirmBtn)
        except NoSuchElementException:
            logging.info("确定按钮不存在")
        else:
            logging.info("click confirmBtn")
            element.click()

if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_switchEnv()
    com.check_testEnv()
    com.check_confirmBtn()





