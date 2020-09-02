from common.baseapp import BaseApp
from time import sleep
import os
import allure

class My_Medal(BaseApp):
    """我的勋章"""

    #元素定位
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的
    loc_dy_wodexunzhang = ("xpath", "//*[@text='我的勋章']")  #我的勋章
    loc_dy_touxiang = ("id", "com.viaton.wyt:id/my_medal_headphoto")  #断言-头像
    loc_dy_xunzhangjimei = ("id", "com.viaton.wyt:id/my_medal_num")  #断言-勋章
    loc_dy_xunzhangmingcheng = ("id", "com.viaton.wyt:id/my_medal_designation")  #断言-勋章名称
    loc_dy_neirong_1 = ("id", "com.viaton.wyt:id/my_medal_info")  #断言-内容-1
    loc_dy_neirong_2 = ("id", 'com.viaton.wyt:id/get_medal_for_rule')  #断言内容-2
    loc_dy_putongxuznhang = ("id", "com.viaton.wyt:id/my_medal_medalname")  #断言普通勋章
    loc_dy_jindu = ("id", "com.viaton.wyt:id/my_medal_progress")  #断言-进度
    loc_dy_yihoude = ("id", "com.viaton.wyt:id/tv_medal_size")  #断言-已获得
    loc_xunzhang = ("id", "com.viaton.wyt:id/my_medal")  #勋章
    loc_xiexia = ("xpath", "//*[@text='卸下']")  #卸下
    loc_chuchumaolu = ("xpath", "//*[@text='初出茅庐']")  #初出茅庐
    loc_peidai = ("xpath", "//*[@text='佩戴']")  #佩戴
    loc_xunzhangpeidaichenggong = ("xpath", "//*[@text='勋章佩戴成功']")  #勋章佩戴成功
    loc_cha = ("id", "com.viaton.wyt:id/iv_close")  #点击×
    loc_honghuashaonian = ("xpath", "//*[@text='红花少年']")  #红花少年
    loc_fenxiangxuanyao = ("id", "com.viaton.wyt:id/tv_share_button")  #分享炫耀一下
    loc_dy_fenxiangxunzhang = ("xpath", "//*[@text='分享勋章']")  #分享勋章
    loc_fenxiang_youshangjiao = ("id", "com.viaton.wyt:id/tv_right")  #分享
    loc_fenxiang_weixin =("xpath", "//*[@text='微信']")  #分享微信
    loc_fenxiang_weixinpengyouquan =("xpath", "//*[@text='微信朋友圈']")  #分享微信朋友圈
    loc_fenxiang_QQ =("xpath", "//*[@text='QQ']")  #分享QQ
    loc_wodediannao = ("xpath", "//*[@text='我的电脑']")  #选择我的电脑
    loc_wodediannao_quxiao = ("xpath", "//*[@text='取消']")  #取消
    loc_quxiao_guanbi = ("xpath", "//*[@text='关闭']")  #关闭
    loc_wodediannao_fasong = ("xpath", "//*[@text='发送']")  #发送
    loc_dy_fenxiangchenggong = ("xpath", "//*[@text='分享成功']")  #断言分享成功
    loc_fanhuiwanyantong = ("xpath", "//*[@text='返回外研通']")  #返回外研通
    loc_fenxiang_QQkongjian =("xpath", "//*[@text='QQ空间']")  #分享QQ空间
    loc_qqkongjian_quxiao = ("xpath", "//*[@text='取消']")  #取消
    loc_qqkongjian_fangqi = ("xpath", "//*[@text='放弃上传']")  #放弃上传
    loc_qqkongjian_fabiao = ("xpath", "//*[@text='发表']")  #发表
    loc_fenxiang_quxiaofenxiang =("xpath", "//*[@text='取消分享']")  #取消分享
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习
    loc_xuexijilu = ("xpath", "//*[@text='学习记录']")  #学习记录



    @allure.step("我的勋章-页面显示")
    def display(self):
        "我的勋章-页面显示"

        #点击我的
        self.click_(self.loc_wode)

        #点击勋章
        self.click_(self.loc_xunzhang)

        #判断我的勋章、头像、勋章几枚、勋章名称、内容、普通勋章、进度条、已获得几枚等是否显示在页面
        result_1 = self.is_element_Exist(self.loc_dy_wodexunzhang)
        result_2 = self.is_element_Exist(self.loc_dy_touxiang)
        result_3 = self.is_element_Exist(self.loc_dy_xunzhangjimei)
        result_4 = self.is_element_Exist(self.loc_dy_xunzhangmingcheng)
        result_5 = self.is_element_Exist(self.loc_dy_neirong_1)
        result_6 = self.is_element_Exist(self.loc_dy_neirong_2)
        result_7 = self.is_element_Exist(self.loc_dy_putongxuznhang)
        result_8 = self.is_element_Exist(self.loc_dy_jindu)
        result_9 = self.is_element_Exist(self.loc_dy_yihoude)

        if result_1 and result_2 and result_3 and result_4 and result_5 and result_6 and result_7 and result_8 and result_9:
            return True
        else:
            return False


    @allure.step("卸下勋章")
    def unload_medal(self):
        "卸下勋章"

        #向上滑半个屏幕
        self.swipeUp()

        #点击卸下
        self.click_(self.loc_xiexia)

        #卸下后，判断是否显示为佩戴
        result = self.is_element_Exist(self.loc_peidai)

        return result

    @allure.step("佩戴勋章")
    def wear_medal(self):
        "佩戴勋章"

        #点击初出茅庐
        self.click_(self.loc_chuchumaolu)
        self.click_(self.loc_chuchumaolu)

        #休眠5秒
        sleep(5)

        #点击佩戴
        self.click_(self.loc_peidai)

        #判断勋章佩戴成功页面是否正确显示
        result = self.is_element_Exist(self.loc_xunzhangpeidaichenggong)

        #点击"×"
        self.click_(self.loc_cha)

        return result

    @allure.step("分享炫耀一下")
    def flaunt(self):
        "分享炫耀一下"

        #点击红花少年
        self.click_(self.loc_honghuashaonian)
        self.click_(self.loc_honghuashaonian)

        #休眠5秒
        sleep(5)

        #点击佩戴
        self.click_(self.loc_peidai)

        #点击分享炫耀一下
        self.click_(self.loc_fenxiangxuanyao)

        #判断分享勋章页面是否正确显示
        result = self.is_element_Exist(self.loc_dy_fenxiangxunzhang)

        return result

    @allure.step("分享到微信")
    def wechat(self):
        "分享到微信"

        #点击分享
        self.click_(self.loc_fenxiang_youshangjiao)

        #点击微信
        self.click_(self.loc_fenxiang_weixin)

        #因为没有安装微信应用，判断是否回到分享勋章页面
        result = self.is_element_Exist(self.loc_dy_fenxiangxunzhang)

        return result

    @allure.step("分享到微信朋友圈")
    def friend(self):
        "分享到微信朋友圈"

        #点击分享
        self.click_(self.loc_fenxiang_youshangjiao)

        #点击微信朋友圈
        self.click_(self.loc_fenxiang_weixinpengyouquan)

        #因为没有安装微信应用，判断是否回到分享勋章页面
        result = self.is_element_Exist(self.loc_dy_fenxiangxunzhang)

        return result

    @allure.step("分享到QQ-中途取消")
    def QQ_cancel(self):
        "分享到QQ-中途取消"

        #点击分享
        self.click_(self.loc_fenxiang_youshangjiao)

        #点击QQ
        self.click_(self.loc_fenxiang_QQ)

        #点击“我的电脑”
        self.click_(self.loc_wodediannao)

        #点击取消
        self.click_(self.loc_wodediannao_quxiao)

        #点击关闭
        self.click_(self.loc_quxiao_guanbi)

        #中途取消分享QQ，判断是否回到分享勋章页面
        result = self.is_element_Exist(self.loc_dy_fenxiangxunzhang)

        return result

    @allure.step("QQ-分享成功")
    def QQ(self):
        "QQ-分享成功"

        #点击分享
        self.click_(self.loc_fenxiang_youshangjiao)

        #点击QQ
        self.click_(self.loc_fenxiang_QQ)

        #点击“我的电脑”
        self.click_(self.loc_wodediannao)

        #点击发送
        self.click_(self.loc_wodediannao_fasong)

        #判断分享成功弹窗是否弹出，返回Bool
        result = self.is_element_Exist(self.loc_dy_fenxiangchenggong)

        #点击返回外研通
        self.click_(self.loc_fanhuiwanyantong)

        return result

    @allure.step("QQ空间-中途取消")
    def QQ_interspace_cancel(self):
        "QQ空间-中途取消"

        #点击分享
        self.click_(self.loc_fenxiang_youshangjiao)

        #点击QQ空间
        self.click_(self.loc_fenxiang_QQkongjian)

        #点击取消
        self.click_(self.loc_qqkongjian_quxiao)

        #点击放弃上传
        self.click_(self.loc_qqkongjian_fangqi)

        #中途取消分享到QQ空间，判断是否回到分享勋章页面
        result = self.is_element_Exist(self.loc_dy_fenxiangxunzhang)

        return result

    @allure.step("QQ空间-成功")
    def QQ_interspace_succeed(self):
        "QQ空间-成功"

        #点击分享
        self.click_(self.loc_fenxiang_youshangjiao)

        #点击QQ空间
        self.click_(self.loc_fenxiang_QQkongjian)

        #点击发表
        self.click_(self.loc_qqkongjian_fabiao)

        #发表成功，判断是否回到分享勋章页面
        result = self.is_element_Exist(self.loc_dy_fenxiangxunzhang)

        return result

    @allure.step("分享-取消分享")
    def cancel(self):
        "分享-取消分享"

        #点击分享
        self.click_(self.loc_fenxiang_youshangjiao)

        #点击取消分享
        self.click_(self.loc_fenxiang_quxiaofenxiang)

        #取消分享，判断是否回到分享勋章页面
        result = self.is_element_Exist(self.loc_dy_fenxiangxunzhang)

        #回退3次，退出我的
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)

        #休眠5秒
        sleep(5)

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        #点击学习记录，保准每个用例集的起点一致
        self.click_(self.loc_xuexijilu)

        #休眠5秒，等待页面加载
        sleep(5)

        return result
