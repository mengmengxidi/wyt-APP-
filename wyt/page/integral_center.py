from common.baseapp import BaseApp
from time import sleep
import os
import allure

class Integral_Center(BaseApp):
    """积分中心"""

    #元素定位
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的
    loc_jifen = ("id", "com.viaton.wyt:id/tv_score")  #积分
    loc_dy_xianshi = ("xpath", "//*[@text='积分中心']")  #断言积分中心
    loc_dy_fenshu = ("id", "com.viaton.wyt:id/tv_score")  #断言分数
    loc_dy_zuanjifen = ("id", "com.viaton.wyt:id/integral_center_getintegral")  #赚积分
    loc_dy_jifenjilu = ("id", "com.viaton.wyt:id/integral_center_record")   #积分记录
    loc_zuanjifen = ("xpath", "//*[@text='赚积分']")  #赚积分
    loc_dy_huoqujifen = ("xpath", "//*[@text='如何获取积分']")  #断言赚积分
    loc_jifenjilu = ("xpath", "//*[@text='积分记录']")  #积分记录
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习
    loc_xuexijilu = ("xpath", "//*[@text='学习记录']")  #学习记录

    @allure.step("积分中心-页面显示")
    def display(self):
        "积分中心-页面显示"

        #点击我的
        self.click_(self.loc_wode)

        #点击积分
        self.click_(self.loc_jifen)

        #休眠3秒
        sleep(3)

        result_1 = self.is_element_Exist(self.loc_dy_xianshi)
        result_2 = self.is_element_Exist(self.loc_dy_fenshu)
        result_3 = self.is_element_Exist(self.loc_dy_zuanjifen)
        result_4 = self.is_element_Exist(self.loc_dy_jifenjilu)

        #判断title、分数 、赚积分、积分记录是否都正确显示
        if result_1 and result_2 and result_3 and result_4:
            return True
        else:
            return False

    @allure.step("赚积分")
    def gain(self):
        "赚积分"

        #点击赚积分
        self.click_(self.loc_zuanjifen)

        #休眠5秒，等待页面加载
        sleep(5)

        #判断是否进入如何获取积分页面
        result = self.is_element_Exist(self.loc_dy_huoqujifen)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("积分记录")
    def record(self):
        "积分记录"

        #点击积分记录
        self.click_(self.loc_jifenjilu)

        #休眠5秒，等待页面加载
        sleep(5)

        #判断积分记录页面是否正确显示
        result = self.is_element_Exist(self.loc_jifenjilu)

        #回退
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)

        #休眠5秒
        sleep(5)

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        return result
