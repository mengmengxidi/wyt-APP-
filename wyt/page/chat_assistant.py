from common.baseapp import BaseApp
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import os
import allure

class Chat_Assistant(BaseApp):

    #元素定位
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的
    loc_zhinengbiliaotianxiaozhushou = ("id", "com.viaton.wyt:id/rl_chat")  #智能笔聊天小助手
    loc_qunliao = ("id", "com.viaton.wyt:id/rl_info")  #15927391992的群聊
    loc_shezhi = ("id", "com.viaton.wyt:id/iv_right")  #设置
    loc_dy_shezhi = ("xpath", "//*[@text='V10智能笔']")  #断言V10智能笔在页面中
    loc_tianjia = ("xpath", "//*[@text='添加']")  #添加
    loc_dy_tianjia = ("xpath", "//*[@text='邀请好友']")  #断言添加，邀请好友在页面中
    loc_fenxiang = ("id", "com.viaton.wyt:id/tv_right")  #分享
    loc_weixin = ("xpath", "//*[@text='微信']")  #微信
    loc_weixinpengyouquan = ("xpath", "//*[@text='微信朋友圈']")  #微信朋友圈
    loc_quxiaofenxiang = ("xpath", "//*[@text='取消分享']")  #取消分享
    loc_yichu = ("xpath", "//*[@text='移除']")  #移除
    loc_liaotianmingcheng = ("xpath", "//*[@text='聊天名称']")  #聊天名称
    loc_queren_liaotianmingcheng = ('id', 'com.viaton.wyt:id/tv_confirm')  #确定-聊天名称
    loc_shurukuang_liaotianmingcheng = ("id" ,"com.viaton.wyt:id/et_input")  #聊天输入框
    loc_dy_bushuru_liaotianmingcheng = ('xpath', "//*[@text='qinneng_group']")  #断言不输入
    loc_dy_1_liaotianmingcheng = ("xpath", "//*[@text='a']")  #断言输入a
    loc_dy_14_liaotianmingcheng = ("xpath", "//*[@text='12345abcdeABCD']")  #断言输入14
    loc_dy_15_liaotianmingcheng = ("xpath", "//*[@text='0.123mnbvcLKJHG']")  #断言输入15
    loc_dy_teshufuhao_liaotianmingcheng = ("xpath", "//*[@text='!@#$%^*']")  #断言输入特殊符号
    loc_dy_qinneng_group_liaotianmingcheng = ("xpath", "//*[@text='qinneng_group']")  #断言输入qinneng group
    loc_quxiao_liaotianmingcheng = ("id", "com.viaton.wyt:id/tv_cancel")  #取消-聊天名称
    loc_wozailiaotianzhongdenicheng = ("xpath", "//*[@text='我在聊天中的昵称']")  #我在聊天中的昵称
    loc_queren_wodenicheng = ("id", "com.viaton.wyt:id/tv_confirm")  #确认-我的昵称
    loc_shurukuang_wodenicheng = ("xpath", "//*[@text='修改聊天昵称']")  #输入框-我的昵称
    loc_dy_bushuru_wodenicheng = ("xpath", "//*[@text='qinneng']")   #断言不输入
    loc_dy_1_wodenicheng = ("xpath", "//*[@text='a']")  #断言输入1
    loc_dy_10_wodenicheng = ("xpath", "//*[@text='56789poiuy']")  #断言输入10
    loc_dy_11_wodenicheng = ("xpath", "//*[@text='0.39abcdOKM']")  #断言输入11
    loc_dy_fuhao_wodenocheng = ("xpath", "//*[@text='!@#$%^*']")  #断言输入特殊符号
    loc_dy_qinneng_wodenicheng = ("xpath", "//*[@text='qinneng']")  #断言输入qinneng
    loc_quxiao_wodenicheng = ("id", "com.viaton.wyt:id/tv_cancel")  #取消-我的昵称
    loc_yaoqingjiatingchengyuan = ("xpath", "//*[@text='邀请家庭成员一起加入']")  #邀请家庭成员一起加入
    loc_zhinengbishangxiantixing = ("id", "com.viaton.wyt:id/slideButton")  #智能笔上线提醒
    loc_text = ("id", "com.viaton.wyt:id/tv_note")   #时间的id相同，获取全部的text
    loc_a = ("xpath", "//*[@text='按住 说话']")
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习

    @allure.step("发送消息-5秒")
    def message_5s(self):
        """成功发送消息"""

        #点击“我的”
        self.click_(self.loc_wode)

        #点击智能聊天笔小助手
        self.click_(self.loc_zhinengbiliaotianxiaozhushou)

        #点击进入群聊
        self.click_(self.loc_qunliao)

        #获取操作前全部的text
        result_start = []
        eles = self.find_Elements(self.loc_text)
        for i in eles:
            t = i.text
            result_start.append(t)
            print(result_start)

        #按住说话
        ele = self.find_Element(self.loc_a)
        TouchAction(self.driver).long_press(ele,duration=5000).wait(1000).perform()

        #休眠10s,等待消息成功发送
        sleep(10)

        #获取操作后全部的text
        result_end = []
        eles = self.find_Elements(self.loc_text)
        for i in eles:
            t = i.text
            result_end.append(t)
        print(result_end)

        #两次屏幕显示有变化，说明有新消息发出
        if result_start == result_end:
            print("屏幕没有变化，发送失败")
            return False
        else:
            print("屏幕有变化，发送成功")
            return True

    @allure.step("发送消息-60秒")
    def message_60s(self):
        """发送消息按住61秒"""

        #获取操作前全部的text
        result_start = []
        eles = self.find_Elements(self.loc_text)
        for i in eles:
            t = i.text
            result_start.append(t)
            print(result_start)

        #休眠5s
        sleep(5)

        #按住说话
        ele = self.find_Element(self.loc_a)
        TouchAction(self.driver).long_press(ele,duration=62000).wait(1000).perform()

        #休眠15s,等待消息成功发送
        sleep(15)

        #获取操作后全部的text
        result_end = []
        eles = self.find_Elements(self.loc_text)
        for i in eles:
            t = i.text
            result_end.append(t)
        print(result_end)

        #两次屏幕显示有变化，说明有新消息发出
        if result_start == result_end:
            print("屏幕没有变化，发送失败")
            return False
        else:
            print("屏幕有变化，发送成功")
            return True

    @allure.step("发送消息-向上滑取消")
    def message_cancel(self):
        """向上滑动取消发送消息"""

        #获取操作前全部的text
        result_start = []
        eles = self.find_Elements(self.loc_text)
        for i in eles:
            t = i.text
            result_start.append(t)
        print(result_start)

        #长按“按住说话”5s，向上滑动到屏幕中心后松开，取消发送语音
        pingmu = self.driver.get_window_size()
        height = pingmu["height"]/2
        width = pingmu["width"]/2
        TouchAction(self.driver).press(x=535, y=2242).wait(5000).move_to(x=width,y=height).release().perform()

        #获取操作后全部的text
        result_end = []
        eles = self.find_Elements(self.loc_text)
        for i in eles:
            t = i.text
            result_end.append(t)
        print(result_end)

        if result_start == result_end:
            print("屏幕没有变化，发送失败")
            return False
        else:
            print("屏幕有变化，发送成功")
            return True

    @allure.step("设置")
    def setting(self):
        "设置"

        #点击设置
        self.click_(self.loc_shezhi)

        #判断进入设置页面
        result = self.is_element_Exist(self.loc_dy_shezhi)

        return result

    @allure.step("添加")
    def add(self):
        "添加"

        #点击添加
        self.click_(self.loc_tianjia)

        #休眠8秒,等待页面加载
        sleep(8)

        #判断进入添加页面，邀请好友在页面中显示
        result = self.is_element_Exist(self.loc_dy_tianjia)

        return result

    @allure.step("分享-微信")
    def wechat_1(self):
        "分享-微信"

        #点击分享
        self.click_(self.loc_fenxiang)

        #点击微信
        self.click_(self.loc_weixin)

        #没有安装微信，判断分享还在页面中
        result = self.is_element_Exist(self.loc_fenxiang)

        return result

    @allure.step("分享-微信朋友圈")
    def friends_1(self):
        "分享-微信朋友圈"

        #点击分享
        self.click_(self.loc_fenxiang)

        #点击微信朋友圈
        self.click_(self.loc_weixinpengyouquan)

        #没有安装微信，判断分享还在页面中
        result = self.is_element_Exist(self.loc_fenxiang)

        return result

    @allure.step("分享-取消分享")
    def cancel_1(self):
        "分享-取消分享"

        #点击分享
        self.click_(self.loc_fenxiang)

        #点击取消分享
        self.click_(self.loc_quxiaofenxiang)

        #取消分享，判断分享还在页面中
        result = self.is_element_Exist(self.loc_fenxiang)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("移除")
    def remove(self):
        "移除"

        #点击移除
        self.click_(self.loc_yichu)

        #无可删除成员，判断V10智能笔还在页面中
        result = self.is_element_Exist(self.loc_dy_shezhi)

        return result

    @allure.step("聊天群名称-不输入")
    def group_name_no(self):
        "聊天群名称-不输入"

        #点击聊天名称
        self.click_(self.loc_liaotianmingcheng)

        #直接点确定
        self.click_(self.loc_queren_liaotianmingcheng)

        #判断聊天名称还为qinneng_group
        result = self.is_element_Exist(self.loc_dy_bushuru_liaotianmingcheng)

        return result

    @allure.step("聊天群名称-1位数")
    def group_name_1(self):
        "聊天群名称-1位数"

        #点击聊天名称
        self.click_(self.loc_liaotianmingcheng)

        #输入“a”
        self.send_Keys(self.loc_shurukuang_liaotianmingcheng, "a")

        #直接点确定
        self.click_(self.loc_queren_liaotianmingcheng)

        #判断聊天名称修改为"a"
        result = self.is_element_Exist(self.loc_dy_1_liaotianmingcheng)

        return result

    @allure.step("聊天群名称-14位数")
    def group_name_14(self):
        "聊天群名称-14位数"

        #点击聊天名称
        self.click_(self.loc_liaotianmingcheng)

        #输入“12345abcdeABCD”
        self.send_Keys(self.loc_shurukuang_liaotianmingcheng, "12345abcdeABCD")

        #直接点确定
        self.click_(self.loc_queren_liaotianmingcheng)

        #判断聊天名称修改为"12345abcdeABCD"
        result = self.is_element_Exist(self.loc_dy_14_liaotianmingcheng)

        return result

    @allure.step("聊天群名称-15位数")
    def group_name_15(self):
        "聊天群名称-15位数"

        #点击聊天名称
        self.click_(self.loc_liaotianmingcheng)

        #输入“0.123mnbvcLKJHG”
        self.send_Keys(self.loc_shurukuang_liaotianmingcheng, "0.123mnbvcLKJHG")

        #直接点确定
        self.click_(self.loc_queren_liaotianmingcheng)

        #判断聊天名称修改为"0.123mnbvcLKJHG"
        result = self.is_element_Exist(self.loc_dy_15_liaotianmingcheng)

        return result

    @allure.step("聊天群名称-特殊符号")
    def group_name_symbol(self):
        "聊天群名称-特殊符号"

        #点击聊天名称
        self.click_(self.loc_liaotianmingcheng)

        #输入“!@#$%^*”
        self.send_Keys(self.loc_shurukuang_liaotianmingcheng, "!@#$%^*")

        #直接点确定
        self.click_(self.loc_queren_liaotianmingcheng)

        #判断聊天名称修改为"!@#$%^*"
        result = self.is_element_Exist(self.loc_dy_teshufuhao_liaotianmingcheng)

        return result

    @allure.step("聊天群名称-qinneng_group")
    def group_name_qinneng_group(self):
        "聊天群名称-特殊符号"

        #点击聊天名称
        self.click_(self.loc_liaotianmingcheng)

        #输入“qinneng_group”
        self.send_Keys(self.loc_shurukuang_liaotianmingcheng, "qinneng_group")

        #直接点确定
        self.click_(self.loc_queren_liaotianmingcheng)

        #判断聊天名称修改为"qinneng_group"
        result = self.is_element_Exist(self.loc_dy_qinneng_group_liaotianmingcheng)

        return result

    @allure.step("我的昵称-不输入")
    def my_nickname_no(self):
        "我的昵称-不输入"

        #点击我的昵称
        self.click_(self.loc_wozailiaotianzhongdenicheng)

        #直接点确定
        self.click_(self.loc_queren_wodenicheng)

        #直接点确定，昵称不会修改，判断昵称名称还为“qinneng”
        result = self.is_element_Exist(self.loc_dy_bushuru_wodenicheng)

        return result

    @allure.step("我的昵称-1位数")
    def my_nickname_1(self):
        "我的昵称-1位数"

        #点击我的昵称
        self.click_(self.loc_wozailiaotianzhongdenicheng)

        #输入1位数
        self.send_Keys(self.loc_shurukuang_wodenicheng, "a")

        #点击确定
        self.click_(self.loc_queren_wodenicheng)

        #判断昵称是否被修改为“a”
        result = self.is_element_Exist(self.loc_dy_1_wodenicheng)

        return result

    @allure.step("我的昵称-10位数")
    def my_nickname_10(self):
        "我的昵称-10位数"

        #点击我的昵称
        self.click_(self.loc_wozailiaotianzhongdenicheng)

        #输入10位数
        self.send_Keys(self.loc_shurukuang_wodenicheng, "56789poiuy")

        #点击确定
        self.click_(self.loc_queren_wodenicheng)

        #判断昵称是否被修改为“56789poiuy”
        result = self.is_element_Exist(self.loc_dy_10_wodenicheng)

        return result

    @allure.step("我的昵称-11位数")
    def my_nickname_11(self):
        "我的昵称-11位数"

        #点击我的昵称
        self.click_(self.loc_wozailiaotianzhongdenicheng)

        #输入11位数
        self.send_Keys(self.loc_shurukuang_wodenicheng, "0.39abcdOKM")

        #点击确定
        self.click_(self.loc_queren_wodenicheng)

        #判断昵称是否被修改为“0.39abcdOKM”
        result = self.is_element_Exist(self.loc_dy_11_wodenicheng)

        return result

    @allure.step("我的昵称-特殊符号")
    def my_nickname_symbol(self):
        "我的昵称-特殊符号"

        #点击我的昵称
        self.click_(self.loc_wozailiaotianzhongdenicheng)

        #输入特殊符号
        self.send_Keys(self.loc_shurukuang_wodenicheng, "!@#$%^*")

        #点击确定
        self.click_(self.loc_queren_wodenicheng)

        #判断昵称是否被修改为“!@#$%^*”
        result = self.is_element_Exist(self.loc_dy_fuhao_wodenocheng)

        return result

    @allure.step("我的昵称-qinneng")
    def my_nickname_qinneng(self):
        "我的昵称-qinneng"

        #点击我的昵称
        self.click_(self.loc_wozailiaotianzhongdenicheng)

        #输入特殊符号
        self.send_Keys(self.loc_shurukuang_wodenicheng, "qinneng")

        #点击确定
        self.click_(self.loc_queren_wodenicheng)

        #判断昵称是否被修改为“qinneng”
        result = self.is_element_Exist(self.loc_dy_qinneng_wodenicheng)

        return result

    @allure.step("邀请家庭成员一起加入")
    def invite(self):
        "邀请家庭成员一起加入"

        #点击邀请家庭成员一起加入
        self.click_(self.loc_yaoqingjiatingchengyuan)

        #判断进入添加页面，邀请好友在页面中显示
        result = self.is_element_Exist(self.loc_dy_tianjia)

        return result

    @allure.step("分享-微信")
    def wechat_2(self):
        "分享-微信"

        #点击分享
        self.click_(self.loc_fenxiang)

        #点击微信
        self.click_(self.loc_weixin)

        #没有安装微信，判断分享还在页面中
        result = self.is_element_Exist(self.loc_fenxiang)

        return result

    @allure.step("分享-微信朋友圈")
    def friends_2(self):
        "分享-微信朋友圈"

        #点击分享
        self.click_(self.loc_fenxiang)

        #点击微信朋友圈
        self.click_(self.loc_weixinpengyouquan)

        #没有安装微信，判断分享还在页面中
        result = self.is_element_Exist(self.loc_fenxiang)

        return result

    @allure.step("分享-取消分享")
    def cancel_2(self):
        "分享-取消分享"

        #点击分享
        self.click_(self.loc_fenxiang)

        #点击取消分享
        self.click_(self.loc_quxiaofenxiang)

        #取消分享，判断分享还在页面中
        result = self.is_element_Exist(self.loc_fenxiang)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("智能笔上线提醒")
    def remind(self):
        "智能笔上线提醒"

        #尝试点击智能笔上线提醒，如果流程走通返回True，出错返回False
        try:
            self.click_(self.loc_zhinengbishangxiantixing)

            sleep(3)

            self.click_(self.loc_zhinengbishangxiantixing)
        except:
            return False
        else:
            #回退
            self.driver.press_keycode(4)

            #休眠3秒
            sleep(3)

            #回退
            self.driver.press_keycode(4)

            #休眠3秒
            sleep(3)

            #回退
            self.driver.press_keycode(4)

            #点击学习，保准每个用例集的起点一致
            self.click_(self.loc_xuexi)

            #休眠5秒
            sleep(5)

            return True
