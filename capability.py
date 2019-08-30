import yaml

# 读取yaml文件中的配置信息
desired_caps = {}
fl = open('desired_caps.yaml', 'r', encoding='utf-8')
data = yaml.safe_load(fl)
desired_caps['platformName'] = data['platformName']
desired_caps['platformVersion'] = data['platformVersion']
desired_caps['deviceName'] = data['deviceName']
desired_caps['app'] = data['app']
desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']
desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
desired_caps['resetKeyboard'] = data['resetKeyboard']
desired_caps['noReset'] = data['noReset']



"""
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    'deviceName': '127.0.0.1:62001' or 'vivo X7',
    'app': r'D:\ME\家长端\Android\app-7.0.0.apk',
    'appPackage': 'com.gwchina.lssw.parent',
    'appActivity': 'com.gwchina.sdk.debug.DebugActivity',
    'unicodeKeyboard': 'True',
    'resetKeyboard': 'True',
    'noReset': 'False'
    # com.gwchina.sdk.debug.DebugActivity
}
"""
