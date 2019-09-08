import yaml
import logging
import logging.config
from appium import webdriver


CON_LOG='./log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
    fl = open('./desired_caps.yaml', 'r')
    data = yaml.safe_load(fl)

    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['platformVersion']=data['platformVersion']

    desired_caps['app']=data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    logging.info('start app...')
    driver = webdriver.Remote(
        "http://"+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    return driver

if __name__ == '__main__':
    appium_desired()