from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.wait import WebDriverWait
import os
import time
#cmd中获取activity:   adb shell dumpsys activity top | findstr ACTIVITY
#cmd中获取包名和首页activity：  aapt dump badging app文件(直接拖)

class BaseApp():
    """Appium的二次封装"""

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.t = 0.5
        self.size = self.driver.get_window_size()

    def find_Element(self, locator):
        """定位元素(单数方法)"""
        if not isinstance(locator, tuple):     #isinstance函数判断locator对象是否是元祖类型
            print("locator参数类型错误，请传入元祖类型")
        else:
            print("正在定位元素：定位方式->%s, 值->%s" % (locator[0], locator[1]))
            if locator[0] == "content_desc":
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element_by_accessibility_id(locator[1]))
            elif locator[0] == "android_uiautomator":
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element_by_android_uiautomator(locator[1]))
            else:
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
                #*locator将两个参数依次传入
            return ele

    def find_Elements(self, locator):
        """定位元素（复数方法）,返回一个list对象，如果没有定位到返回空列表[]"""
        if not isinstance(locator, tuple):     #isinstance函数判断locator对象是否是元祖类型
            print("locator必须传元祖类型")
        else:
            print("正在定位元素：定位方式：%s, 值：%s" % (locator[0], locator[1]))
            if locator[0] == "content_desc":
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements_by_accessibility_id(locator[1]))
            elif locator[0] == "android_uiautomator":
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements_by_android_uiautomator(locator[1]))
            else:
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))    #*locator将两个参数依次传入
            return eles




    #----------------------------------------屏幕上下左右滑动开始----------------------------------------
    def swipeUp(self, duration=500, n=1):
        """向上滑动半个屏幕，duration控制整个滑动过程时间，n控制滑动次数"""
        y_start = self.size["height"] * 3/4
        y_end = self.size["height"] * 1/4
        x = self.size["width"] * 1/2

        for i in range(n):
            self.driver.swipe(x, y_start, x, y_end)

    def swipeDown(self, duration=500, n=1):
        """向下滑动半个屏幕，duration控制整个滑动过程时间，n控制滑动次数"""
        y_start = self.size["height"] * 1/4
        y_end = self.size["height"] * 3/4
        x = self.size["width"] * 1/2

        for i in range(n):
            self.driver.swipe(x, y_start, x, y_end, duration)

    def swipeLeft(self, duration=500, n=1):
        """向左滑动半个屏幕，duration控制整个滑动过程时间，n控制滑动次数"""
        x_start = self.size['width']*3/4
        x_end = self.size['width']*1/4
        y = self.size['height']*1/2

        for i in range(n):
            self.driver.swipe(x_start, y, x_end, y, duration)

    def swipeRight(self, duration=500, n=1):
        """向右滑动半个屏幕，duration控制整个滑动过程时间，n控制滑动次数"""
        x_start = self.size['width']*1/4
        x_end = self.size['width']*3/4
        y = self.size['height']*1/2

        for i in range(n):
            self.driver.swipe(x_start, y, x_end, y, duration)
    #----------------------------------------屏幕上下左右滑动结束----------------------------------------



    def click_(self, locator):
        """单击操作"""
        ele = self.find_Element(locator)
        ele.click()

    def send_Keys(self, locator, text):
        """send_keys输入操作"""
        ele = self.find_Element(locator)
        ele.send_keys(text)

    def tap_Webview(self, locator):
        """嵌套的webview页面click失效时，用selenium中TouchActions库里的tap事件"""
        element = self.find_Element(locator)
        TouchActions(self.driver).tap(element).perform()

    def tap_Native_App(self, locator=None, x=None, y=None, count=1):
        """安卓原生的NATIVE_APP页面click失效时，用appium中TouchAction库里的tap事件"""
        if locator:
            element = self.find_Element(locator)
            TouchAction(self.driver).tap(element=element, count=count).perform()
        else:
            TouchAction(self.driver).tap(x=x, y=y, count=count).perform()

    def is_toast_in(self, text):
        """定位toast消息,（后退显示的‘再按一次退出程序’弹窗）, 判断toast信息是否包含text文本内容,没有定位到也返回False"""
        loc_toast = ("xpath", "//*[contains(@text, '%s')]" % text)
        try:
            ele = WebDriverWait(self.driver, self.timeout, 0.2).until(lambda x: x.find_element(*loc_toast))
            print(ele.text)
            if text in ele.text:
                return True
            else:
                return False
        except:
            return False

    def webview_html(self, filename):
        """webview中源码保存到html, 传入保存的html文件名称"""
        p = self.driver.page_source
        with open(filename, "wb") as fp:
            fp.write(p.encode("utf-8"))

    def clear_(self, locator):
        """文本框清除操作"""
        ele = self.find_Element(locator)
        ele.clear()

    def is_element_Exist(self, locator):
        """主要断言方法，判断元素是否存在,返回bool值"""
        try:
            self.find_Element(locator)
            print("已经定位到元素，返回True")
            return True
        except:
            print("元素不存在，返回False")
            return False

    def is_elements_Exist(self, locator):
        """复数定位判断元素是否存在,存在返回True，不存在就是一个空列表，返回False"""
        ele = self.find_Elements(locator)
        numbers = len(ele)
        if numbers == 0:
            print("元素不存在，返回False")
            return False
        else:
            print("定位到了%s个元素对象" % numbers)
            return True
from appium import webdriver

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import os

desired_leidian = {
    "platformName": "Android",
    "deviceName": "79UDU19918003766",
    "platformVersion": "10",
    "appPackage": "com.viaton.wyt",
    "appActivity": "com.mp.phone.module.logic.welcome.SplashActivity",
    "noReset": True,
    "unicodeKeyboard": True,   # 使用Unicode编码方式发送字符串
    "resetKeyboard": True,    # 隐藏键盘
    # "automationName": "Uiautomator2"
    }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_leidian)

app = BaseApp(driver)

loc_shujia = ("xpath", "//*[@text='书架' and @resource-id='com.viaton.wyt:id/page_bookshelf']")  #书架
loc_jixupeiyin = ("xpath", "//*[@instance='8' and @resource-id='com.viaton.wyt:id/tv_dubbing']")  #继续配音

app.click_(loc_shujia)
app.click_(loc_jixupeiyin)
sleep(5)

cmd = "adb shell input tap 109 449"
os.system(cmd)
sleep(5)

cmd = "adb shell input tap 109 610"
os.system(cmd)
sleep(5)
