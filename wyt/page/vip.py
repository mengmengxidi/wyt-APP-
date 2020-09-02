from common.baseapp import BaseApp
from time import sleep
import os
import allure

class Vip(BaseApp):
    """配音秀会员"""

    #元素定位
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的
    loc_vip_tubiao = ("id", "com.viaton.wyt:id/iv_dub_vip_icon")  #vip图标
    loc_dy_title = ("id", "com.viaton.wyt:id/tv_page_title")  #断言title显示
    loc_dy_touxiang = ("id", "com.viaton.wyt:id/civ_photo")  #断言头像显示
    loc_dy_mingzi = ("id", "com.viaton.wyt:id/tv_name")  #断言名称显示
    loc_dy_viptubiao = ("id", "com.viaton.wyt:id/iv_dub_vip_icon")  #断言vip图标
    loc_dy_zi = ("id", "com.viaton.wyt:id/tv_dub_vip")  #断言配音秀会员
    loc_dy_zunxiangfuwu = ("id", "com.viaton.wyt:id/tv_vip_first_note")  #断言配音秀会员尊享服务
    loc_dy_daoqishijian = ("id", "com.viaton.wyt:id/tv_vip_second_note")  #断言到期时间
    loc_jiaoyijilu = ("xpath", "//*[@resource-id='com.viaton.wyt:id/tv_page_title']/../*[@instance='2']")  #交易记录图标
    loc_dy_jiaoyijilu = ("xpath", "//*[@text='交易记录']")  #断言交易记录
    loc_12yue = ("id", "com.viaton.wyt:id/rl_price_left")  #12个月
    loc_36yue = ("id", "com.viaton.wyt:id/rl_price_right")  #36个月
    loc_lijixufei = ("id", "com.viaton.wyt:id/tv_pay")  #立即续费
    loc_dy_zhifubao = ("xpath", "//*[@text='支 支付宝付款']")  #断言支付宝
    loc_weixin_gou = ("xpath", "//*[@resource-id='com.viaton.wyt:id/iv_ali_pay']/../*[@instance='8']")  #勾选微信
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习

    @allure.step("配音秀会员-页面显示")
    def display(self):
        "配音秀会员-页面显示"

        #点击我的
        self.click_(self.loc_wode)

        #休眠5秒
        sleep(5)

        #点击VIP图标
        self.click_(self.loc_vip_tubiao)

        #休眠5秒
        sleep(5)

        #判断title、头像、名称、vip图标、vip字样、尊贤会员、到期时间是否正确显示
        result_1 = self.is_element_Exist(self.loc_dy_title)
        result_2 = self.is_element_Exist(self.loc_dy_touxiang)
        result_3 = self.is_element_Exist(self.loc_dy_mingzi)
        result_4 = self.is_element_Exist(self.loc_dy_viptubiao)
        result_5 = self.is_element_Exist(self.loc_dy_zi)
        result_6 = self.is_element_Exist(self.loc_dy_zunxiangfuwu)
        result_7 = self.is_element_Exist(self.loc_dy_daoqishijian)

        if result_1 and result_2 and result_3 and result_4 and result_5 and result_6 and result_7:
            return True
        else:
            return False

    @allure.step("交易记录")
    def record(self):
        "交易记录"

        #休眠5秒
        sleep(5)

        #点击交易记录图标
        self.click_(self.loc_jiaoyijilu)

        #判断交易记录页面是否正确显示
        result = self.is_element_Exist(self.loc_dy_jiaoyijilu)

        #休眠2秒
        sleep(2)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("支付宝-12个月")
    def alipay_12(self):
        "支付宝-12个月"

        #休眠3秒
        sleep(3)

        #点击12个月
        self.click_(self.loc_12yue)

        #休眠3秒
        sleep(3)

        #点击立即续费
        self.click_(self.loc_lijixufei)

        #休眠10秒
        sleep(10)

        #判断是否调到支付宝付款页面
        result = self.is_element_Exist(self.loc_dy_zhifubao)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("支付宝-36各月")
    def alipay_36(self):
        "支付宝-36各月"

        #休眠3秒
        sleep(3)

        #点击36个月
        self.click_(self.loc_36yue)

        #休眠3秒
        sleep(3)

        #点击立即续费
        self.click_(self.loc_lijixufei)

        #休眠10秒
        sleep(10)

        #判断是否调到支付宝付款页面
        result = self.is_element_Exist(self.loc_dy_zhifubao)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("微信-12个月")
    def wechat_12(self):
        "微信-12个月"

        #休眠3秒
        sleep(3)

        #点击12个月
        self.click_(self.loc_12yue)

        #休眠3秒
        sleep(3)

        #点击微信
        self.click_(self.loc_weixin_gou)

        #休眠3秒
        sleep(3)

        #点击立即续费
        self.click_(self.loc_lijixufei)

        #断言还在立即续费页面
        result = self.is_element_Exist(self.loc_lijixufei)

        return result

    @allure.step("微信-36个月")
    def wechat_36(self):
        "微信-36个月"

        #休眠3秒
        sleep(3)

        #点击12个月
        self.click_(self.loc_36yue)

        #休眠3秒
        sleep(3)

        #点击微信
        self.click_(self.loc_weixin_gou)

        #休眠3秒
        sleep(3)

        #点击立即续费
        self.click_(self.loc_lijixufei)

        #断言还在立即续费页面
        result = self.is_element_Exist(self.loc_lijixufei)

        #回退
        self.driver.press_keycode(4)

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        #休眠5秒
        sleep(5)

        return result