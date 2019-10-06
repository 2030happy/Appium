import yaml
from appium import webdriver
from time import ctime
import multiprocessing


# 被测设备信息
with open('desired_caps.yaml', 'r',encoding='utf-8') as fl:
    data = yaml.safe_load(fl)

devices_list = ['127.0.0.1:62001', '127.0.0.1:62025']

def appium_desire(udid, port):
    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['udid']=udid

    desired_caps['app']=data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']

    print('appium port:%s start run %s at %s' %(port, udid,ctime()))
    driver =  webdriver.Remote(
        "http://"+str(data['ip'])+':'+str(port)+'/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    return driver

# 构建desired进程组
desired_process=[]

# 加载desired进程
for i in range(len(devices_list)):
    port=4723 + 2 * i
    desired=multiprocessing.Process(target=appium_desire,
                                    args=(devices_list[i],port))
    desired_process.append(desired)


if __name__  == '__main__':
    # 启动多设备执行测试
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()

