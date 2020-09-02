from common.baseapp import BaseApp
from time import sleep
import os
import allure

class Ranking_List(BaseApp):
    """学习-学习排行榜"""

    #元素定位
    loc_paihangbang = ("xpath", "//*[@text='学习排行榜']")  #学习排行榜
    loc_dy_Day_1 = ("xpath", "//*[@text='1' and @resource-id='com.viaton.wyt:id/tv_position']")  #断言Day-1
    loc_dy_Day_2 = ("xpath", "//*[@text='2' and @resource-id='com.viaton.wyt:id/tv_position']")  #断言Day-1
    loc_dy_Day_3 = ("xpath", "//*[@text='3' and @resource-id='com.viaton.wyt:id/tv_position']")  #断言Day-1
    loc_Week = ('xpath', "//*[@text='Week']")  #Week
    loc_dy_Week_1 = ("xpath", "//*[@text='1' and @resource-id='com.viaton.wyt:id/tv_position']")  #断言Week-1
    loc_dy_Week_2 = ("xpath", "//*[@text='2' and @resource-id='com.viaton.wyt:id/tv_position']")  #断言Week-2
    loc_dy_Week_3 = ("xpath", "//*[@text='3' and @resource-id='com.viaton.wyt:id/tv_position']")  #断言Week-3
    loc_Month = ('xpath', "//*[@text='Month']")  #Month
    loc_dy_Month_1 = ("xpath", "//*[@text='1' and @resource-id='com.viaton.wyt:id/tv_position']")  #断言Month-1
    loc_dy_Month_2 = ("xpath", "//*[@text='2' and @resource-id='com.viaton.wyt:id/tv_position']")  #断言Month-2
    loc_dy_Month_3 = ("xpath", "//*[@text='3' and @resource-id='com.viaton.wyt:id/tv_position']")  #断言Month-3
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习
    loc_xuexijilu = ("xpath", "//*[@text='学习记录']")  #学习记录

    @allure.step("学习排行榜-Day")
    def day(self):
        "学习排行榜-Day"

        #点击学习排行榜
        self.click_(self.loc_paihangbang)

        #判断是否显示前3位同学，返回Bool
        result_1 = self.is_element_Exist(self.loc_dy_Day_1)
        result_2 = self.is_element_Exist(self.loc_dy_Day_2)
        result_3 = self.is_element_Exist(self.loc_dy_Day_3)

        if result_1 and result_2 and result_3:
            return True
        else:
            return False

    @allure.step("学习排行榜-Week")
    def week(self):
        "学习排行榜-Week"

        #点击Week
        self.click_(self.loc_Week)

        #点击一次可能没跳转，再次点击一次
        self.click_(self.loc_Week)

        #判断是否显示前3位同学，返回Bool
        result_1 = self.is_element_Exist(self.loc_dy_Day_1)
        result_2 = self.is_element_Exist(self.loc_dy_Day_2)
        result_3 = self.is_element_Exist(self.loc_dy_Day_3)

        if result_1 and result_2 and result_3:
            return True
        else:
            return False

    @allure.step("学习排行榜-Month")
    def month(self):
        "学习排行榜-Month"

        #点击Month
        self.click_(self.loc_Month)

        #点击一次可能没跳转，再次点击一次
        self.click_(self.loc_Month)

        #判断是否显示前3位同学，返回Bool
        result_1 = self.is_element_Exist(self.loc_dy_Day_1)
        result_2 = self.is_element_Exist(self.loc_dy_Day_2)
        result_3 = self.is_element_Exist(self.loc_dy_Day_3)

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        #点击学习记录，保准每个用例集的起点一致
        self.click_(self.loc_xuexijilu)

        #休眠5秒，等待页面加载
        sleep(5)

        if result_1 and result_2 and result_3:
            return True
        else:
            return False
