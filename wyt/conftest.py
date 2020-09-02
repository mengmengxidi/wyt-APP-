from appium import webdriver
import pytest
from time import sleep

desired_leidian = {
    "platformName": "Android",
    "deviceName": "***********", 
    "platformVersion": "10",
    "appPackage": "**********",
    "appActivity": "************************************",
    "noReset": True,
    "unicodeKeyboard": True,   # 使用Unicode编码方式发送字符串
    "resetKeyboard": True,    # 隐藏键盘
    # "automationName": "Uiautomator2"
    }

_driver = None

@pytest.fixture(scope='session')
def driver(request):
    global _driver

    if _driver is None:
        _driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_leidian)
        sleep(10)
        print("正在启动Android***APP")

    def fn():
        print("所有用例都执行完毕,退出Android***APP")
        _driver.quit()
    request.addfinalizer(fn)
    return _driver
