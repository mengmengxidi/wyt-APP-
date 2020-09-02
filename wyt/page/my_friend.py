from common.baseapp import BaseApp
from time import sleep
import os
import allure

class My_Friend(BaseApp):
    """我的好友"""

    #元素定位
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的
    loc_wodehaoyou = ("xpath", "//*[@text='我的好友']")  #我的好友
    loc_dy_wodehaoyou = ("xpath", "//*[contains(@text,'我的好友(')]")  #断言我的好友
    loc_jia_youshangjiao = ("id", "com.viaton.wyt:id/iv_right")  #＋  右上角
    loc_dy_jia = ("id", "com.viaton.wyt:id/et_input")  #断言点击+后，出现输入框
    loc_shurukuang_tianjiahaoyou = ("id", "com.viaton.wyt:id/et_input")  #输入框-添加好友
    loc_sousuo = ("id", "com.viaton.wyt:id/rl_add_to_someone")  #搜索
    loc_tianjiahaoyou = ("id", "com.viaton.wyt:id/tv_add")  #添加好友
    loc_yanzhengxinxi_yanzhnegshenqing = ("id", "com.viaton.wyt:id/et_verify")  #验证信息
    loc_beizhu_yanzhnegshenqing = ("id", "com.viaton.wyt:id/et_remark")  #备注
    loc_fasong_yanzhnegshenqing = ("id", "com.viaton.wyt:id/tv_right")  #发送
    loc_dy_fasong = ("xpath", "//*[@text='详细资料']")  #发送成功，断言回到详细资料页面
    loc_quxiao_tianjiahaoyou = ("id", "com.viaton.wyt:id/tv_right")  #取消-添加好友
    loc_tianyi = ("xpath", "//*[@text='tianyi']")  #tianyi
    loc_sandian_youshangjiao = ("id", "com.viaton.wyt:id/iv_right")  #右上角三个点
    loc_quxiao = ("id", "com.viaton.wyt:id/tv_cancle")  #取消
    loc_dy_quxiao = ("id", "com.viaton.wyt:id/tv_reName")  #断言取消
    loc_shezhibeizhu = ("id", "com.viaton.wyt:id/iv_next_page")  #设置备注
    loc_shurukuang_shezhibeizhu = ("id", "com.viaton.wyt:id/et_input_name")  #输入框-设置备注
    loc_shezhibeuzhu_title = ("id", "com.viaton.wyt:id/tv_title")  #设置备注，收回键盘
    loc_baocun_shezhibeizhu = ("id", "com.viaton.wyt:id/tv_save")  #保存
    loc_dy_1_shezhibeizhu = ("xpath", "//*[@text='a']")  #1
    loc_dy_9_shezhibeizhu = ("xpath", "//*[@text='asdFGHjkl']")  #9
    loc_dy_10_shezhibeizhu = ("xpath", "//*[@text='QWERTyuiop']")  #10
    loc_dy_yingwen_shuzi_shezhibeizhu = ("xpath", "//*[@text='abc123']")  #英文加数字
    loc_dy_teshufuhao_shezhibeizhu = ("xpath", "//*[@text='!@#$%^*']")  #特殊符号
    loc_dy_tianyi_shezhibeizhu = ("xpath", "//*[@text='tianyi']")  #tianyi
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习

    @allure.step("我的好友")
    def my_friend(self):
        "我的好友"

        #点击我的
        self.click_(self.loc_wode)

        #点击我的好友
        self.click_(self.loc_wodehaoyou)

        #判断是否进入我的好友页面
        result = self.is_element_Exist(self.loc_dy_wodehaoyou)

        return result

    @allure.step("搜索注册过的手机号")
    def have_register(self):
        "搜索注册过的手机号"

        #点击右上角+
        self.click_(self.loc_jia_youshangjiao)

        #输入17709908458
        self.send_Keys(self.loc_shurukuang_tianjiahaoyou, "17709908458")

        #点击搜索
        self.click_(self.loc_sousuo)

        #点击添加好友
        self.click_(self.loc_tianjiahaoyou)

        #输入验证信息
        self.send_Keys(self.loc_yanzhengxinxi_yanzhnegshenqing, "my name is qin, add you as a friend")

        #点击备注，聚集光标
        self.click_(self.loc_beizhu_yanzhnegshenqing)

        #输入备注
        self.send_Keys(self.loc_beizhu_yanzhnegshenqing, "177")

        #点击发送
        self.click_(self.loc_fasong_yanzhnegshenqing)

        #判断发送成功后，回到详细资料页面
        result = self.is_element_Exist(self.loc_dy_fasong)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("搜索未注册过的手机号")
    def not_register(self):
        "搜索未注册过的手机号"

        #清空输入框
        self.clear_(self.loc_shurukuang_tianjiahaoyou)

        #输入未注册过的手机号
        self.send_Keys(self.loc_shurukuang_tianjiahaoyou, "17709908459")

        #点击搜索
        self.click_(self.loc_sousuo)

        #不会出现搜索结果，判断还在搜索页面上
        result = self.is_element_Exist(self.loc_sousuo)

        return result

    @allure.step("搜索11位不符合手机号段格式的手机号")
    def inconformity(self):
        "搜索11位不符合手机号段格式的手机号"

        #清空输入框
        self.clear_(self.loc_shurukuang_tianjiahaoyou)

        #输入11位不符合手机号段格式的手机号
        self.send_Keys(self.loc_shurukuang_tianjiahaoyou, "98765432100")

        #点击搜索
        self.click_(self.loc_sousuo)

        #不会出现搜索结果，判断还在搜索页面上
        result = self.is_element_Exist(self.loc_sousuo)

        #点击取消
        self.click_(self.loc_quxiao_tianjiahaoyou)

        return result

    @allure.step("删除好友-取消")
    def delete_cancel(self):
        "删除好友-取消"

        #点击好友tianyi
        self.click_(self.loc_tianyi)

        #点击右上角三个点
        self.click_(self.loc_sandian_youshangjiao)

        #点击取笑
        self.click_(self.loc_quxiao)

        #判断还在好友详情上
        result = self.is_element_Exist(self.loc_dy_quxiao)

        return result

    @allure.step("备注-1位数")
    def notes_1(self):
        "备注-1位数"

        #点击设置备注
        self.click_(self.loc_shezhibeizhu)

        #输入1位数
        self.send_Keys(self.loc_shurukuang_shezhibeizhu, "a")

        #点击设置备注title，收回键盘
        self.click_(self.loc_shezhibeuzhu_title)

        #点击保存
        self.click_(self.loc_baocun_shezhibeizhu)

        #判断“a”在我的好友页面上
        result = self.is_element_Exist(self.loc_dy_1_shezhibeizhu)

        return result

    @allure.step("备注-9位数")
    def notes_9(self):
        "备注-9位数"

        #点击好友tianyi
        self.click_(self.loc_dy_1_shezhibeizhu)

        #点击设置备注
        self.click_(self.loc_shezhibeizhu)

        #输入9位数
        self.send_Keys(self.loc_shurukuang_shezhibeizhu, "asdFGHjkl")

        #点击设置备注title，收回键盘
        self.click_(self.loc_shezhibeuzhu_title)

        #点击保存
        self.click_(self.loc_baocun_shezhibeizhu)

        #判断“asdFGHjkl”在我的好友页面上
        result = self.is_element_Exist(self.loc_dy_9_shezhibeizhu)

        return result

    @allure.step("备注-10位数")
    def notes_10(self):
        "备注-10位数"

        #点击好友tianyi
        self.click_(self.loc_dy_9_shezhibeizhu)

        #点击设置备注
        self.click_(self.loc_shezhibeizhu)

        #输入10位数
        self.send_Keys(self.loc_shurukuang_shezhibeizhu, "QWERTyuiop")

        #点击设置备注title，收回键盘
        self.click_(self.loc_shezhibeuzhu_title)

        #点击保存
        self.click_(self.loc_baocun_shezhibeizhu)

        #判断“QWERTyuiop”在我的好友页面上
        result = self.is_element_Exist(self.loc_dy_10_shezhibeizhu)

        return result

    @allure.step("备注-英文加数字")
    def notes_english_numbers(self):
        "备注-英文加数字"

        #点击好友tianyi
        self.click_(self.loc_dy_10_shezhibeizhu)

        #点击设置备注
        self.click_(self.loc_shezhibeizhu)

        #输入英文加数字
        self.send_Keys(self.loc_shurukuang_shezhibeizhu, "abc123")

        #点击设置备注title，收回键盘
        self.click_(self.loc_shezhibeuzhu_title)

        #点击保存
        self.click_(self.loc_baocun_shezhibeizhu)

        #判断“abc123”在我的好友页面上
        result = self.is_element_Exist(self.loc_dy_yingwen_shuzi_shezhibeizhu)

        return result

    @allure.step("备注-特殊符号")
    def notes_symbol(self):
        "备注-特殊符号"

        #点击好友tianyi
        self.click_(self.loc_dy_yingwen_shuzi_shezhibeizhu)

        #点击设置备注
        self.click_(self.loc_shezhibeizhu)

        #输入特殊符号
        self.send_Keys(self.loc_shurukuang_shezhibeizhu, "!@#$%^*")

        #点击设置备注title，收回键盘
        self.click_(self.loc_shezhibeuzhu_title)

        #点击保存
        self.click_(self.loc_baocun_shezhibeizhu)

        #判断“!@#$%^*”在我的好友页面上
        result = self.is_element_Exist(self.loc_dy_teshufuhao_shezhibeizhu)

        return result

    @allure.step("备注-tianyi")
    def notes_tianyi(self):
        "备注-特殊符号"

        #点击好友tianyi
        self.click_(self.loc_dy_teshufuhao_shezhibeizhu)

        #点击设置备注
        self.click_(self.loc_shezhibeizhu)

        #输入tianyi
        self.send_Keys(self.loc_shurukuang_shezhibeizhu, "tianyi")

        #点击设置备注title，收回键盘
        self.click_(self.loc_shezhibeuzhu_title)

        #点击保存
        self.click_(self.loc_baocun_shezhibeizhu)

        #判断“tianyi”在我的好友页面上
        result = self.is_element_Exist(self.loc_dy_tianyi_shezhibeizhu)

        #回退
        self.driver.press_keycode(4)

        return result
