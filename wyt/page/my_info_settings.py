from common.baseapp import BaseApp
from time import sleep
import os
import allure

class My_Info_Settings(BaseApp):
    """我的信息设置"""

    #元素定位
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的
    loc_youshangjiao = ("id", "com.viaton.wyt:id/iv_edit")  #我的-右上角
    loc_touxiang = ("xpath", "//*[@text='头像']")  #头像
    loc_congshoujixiangcexuanze = ("xpath", "//*[@text='从手机相册选择']")  #从手机相册选择
    loc_downloads = ("xpath", "//*[@text='downloads']")  #选择downloads
    loc_dy_wodexinzishezhi = ("xpath", "//*[@text='我的信息设置']")  #判断我的信息设置
    loc_paizhao = ("xpath", "//*[@text='拍照']")  #拍照
    loc_quxiao_touxiang = ("id", "com.viaton.wyt:id/tv_cancel")  #取消-头像
    loc_gou_xuanzezhaopian = ("id", "com.android.gallery3d:id/head_select_right")  #√-选择照片
    loc_cha_xiujianzhaopian = ("id", "com.android.gallery3d:id/head_select_left")  #×-修剪照片
    loc_gou_xiujianzhaopian = ("id", "com.android.gallery3d:id/head_select_right")  #√-修剪照片
    loc_niceng = ("xpath", "//*[@text='昵称']")  #昵称
    loc_niceng_shurukuang = ("id", "com.viaton.wyt:id/et_input")  #昵称输入框
    loc_nicheng_queding = ("id", "com.viaton.wyt:id/tv_confirm")  #昵称-确定
    loc_dy_niHAO12345 = ("xpath", "//*[@text='niHAO12345']")  #断言昵称“niHAO你好123”是否修改成功
    loc_dy_abc_123_ABC = ("xpath", "//*[@text='abc_123_ABC']")  #断言昵称“abc_123_ABC”是否修改成功
    loc_dy_teshufuhao = ("xpath", "//*[@text='!@#$%']")  #断言昵称“!@#$%”是否修改成功
    loc_dy_159 = ("xpath", "//*[@text='159']")  #断言昵称“159”是否修改成功
    loc_nicheng_quxiao = ("id", "com.viaton.wyt:id/tv_cancel")  #昵称-取消
    loc_nianling = ("xpath", "//*[@text='年龄']")  #年龄
    loc_nianling_shurukuang = ("id", "com.viaton.wyt:id/et_input")  #年龄输入框
    loc_dy_nianling_1 = ("xpath", "//*[@text='1']")  #断言年龄1
    loc_dy_nianling_0 = ("xpath", "//*[@text='0']")  #断言年龄0
    loc_dy_nianling_18 = ("xpath", "//*[@text='18']")  #断言年龄18
    loc_dy_nianling_99 = ("xpath", "//*[@text='99']")  #断言年龄99
    loc_dy_nianling_50 = ("xpath", "//*[@text='1']")  #断言年龄50
    loc_queding_nianling = ("id", "com.viaton.wyt:id/tv_confirm")  #确定-年龄
    loc_quxiao_nianling = ("id", "com.viaton.wyt:id/tv_cancel")  #取消-年龄
    loc_xingbie = ("xpath", "//*[@text='性别']")  #性别
    loc_nan = ("xpath", "//*[@text='男']")  #男
    loc_dy_nan = ("xpath", "//*[@text='男']")  #断言男
    loc_nv = ("xpath", "//*[@text='女']")  #女
    loc_dy_nv = ("xpath", "//*[@text='女']")  #断言女
    loc_quxiao_xingbie = ("id", "com.viaton.wyt:id/tv_cancel")  #取消
    loc_nianji = ("xpath", "//*[@text='年级']")  #年级
    loc_youeryuanxiaoban = ("xpath", "//*[@text='幼儿园小班']")  #幼儿园小班
    loc_dy_youeryuanxiaoban = ("xpath", "//*[@text='幼儿园小班']")  #断言幼儿园小班
    loc_daxuesinianji = ("xpath", "//*[@text='大学四年级']")  #大学四年级
    loc_dy_daxuesinianji = ("xpath", "//*[@text='大学四年级']")  #断言大学四年级
    loc_xiaoxuewunianji = ("xpath", "//*[@text='小学五年级']")  #小学五年级
    loc_dy_xiaoxuewunianji = ("xpath", "//*[@text='小学五年级']")  #断言小学五年级
    loc_queding_nianji = ("id", "com.viaton.wyt:id/tv_confirm")  #确定-年级
    loc_buxuanze = ("xpath", "//*[@text='你现在读几年级？']")  #判断还在选择页面
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习
    loc_xuexijilu = ("xpath", "//*[@text='学习记录']")  #学习记录


    @allure.step("头像-从手机相册选择-中途取消")
    def cellphone_cancel(self):
        "头像-从手机相册选择-中途取消"

        #点击我的
        self.click_(self.loc_wode)

        #点击我的右上角
        self.click_(self.loc_youshangjiao)

        #点击头像
        self.click_(self.loc_touxiang)

        #点击从手机相册选择
        self.click_(self.loc_congshoujixiangcexuanze)

        #点击downloads
        self.click_(self.loc_downloads)

        #选择第一张图片
        cmd = "adb shell input tap 179 427"
        os.system(cmd)

        #点击√
        self.click_(self.loc_gou_xuanzezhaopian)

        #点击×，取消更换头像
        self.click_(self.loc_cha_xiujianzhaopian)

        #判断我的信息设置页面是否完全显示
        result = self.is_element_Exist(self.loc_dy_wodexinzishezhi)

        return result

    @allure.step("头像-从手机相册选择")
    def cellphone(self):
        "头像-从手机相册选择"

        #点击头像
        self.click_(self.loc_touxiang)

        #点击从手机相册选择
        self.click_(self.loc_congshoujixiangcexuanze)

        #点击downloads
        self.click_(self.loc_downloads)

        #选择第一张图片
        cmd = "adb shell input tap 179 427"
        os.system(cmd)

        #点击√
        self.click_(self.loc_gou_xuanzezhaopian)

        #点击√
        self.click_(self.loc_gou_xiujianzhaopian)

        #休眠5秒,等待上传成功
        sleep(5)

        #判断我的信息设置页面是否完全显示
        result = self.is_element_Exist(self.loc_dy_wodexinzishezhi)

        return result

    @allure.step("头像-取消")
    def cancel(self):
        "头像-取消"

        #点击头像
        self.click_(self.loc_touxiang)

        #点击取消
        self.click_(self.loc_quxiao_touxiang)

        #判断我的信息设置页面是否完全显示
        result = self.is_element_Exist(self.loc_dy_wodexinzishezhi)

        return result

    @allure.step("昵称-输入10个字")
    def nickname_10(self):
        "昵称-输入10个字"

        #点击昵称
        self.click_(self.loc_niceng)

        #输入“niHAO12345”
        self.send_Keys(self.loc_niceng_shurukuang, "niHAO12345")

        #点击确定
        self.click_(self.loc_nicheng_queding)

        #判断昵称“niHAO你好123”是否修改成功
        result = self.is_element_Exist(self.loc_dy_niHAO12345)

        return result

    @allure.step("昵称-输入11个字")
    def nickname_11(self):
        "昵称-输入11个字"

        #点击昵称
        self.click_(self.loc_niceng)

        #输入“abc_123_ABC”
        self.send_Keys(self.loc_niceng_shurukuang, "abc_123_ABC")

        #点击确定
        self.click_(self.loc_nicheng_queding)

        #判断昵称“abc_123_ABC”是否修改成功
        result = self.is_element_Exist(self.loc_dy_abc_123_ABC)

        return result

    @allure.step("昵称-不输入")
    def nickname_not_enter(self):
        "昵称-不输入"

        #点击昵称
        self.click_(self.loc_niceng)

        #不输入，直接点击确定
        self.click_(self.loc_nicheng_queding)

        #判断昵称是否还为“abc_123_ABC”
        result = self.is_element_Exist(self.loc_dy_abc_123_ABC)

        return result

    @allure.step("昵称-输入特殊符号")
    def nickname_symbol(self):
        "昵称-输入特殊符号"

        #点击昵称
        self.click_(self.loc_niceng)

        #输入特殊符号“!@#$%”
        self.send_Keys(self.loc_niceng_shurukuang, "!@#$%")

        #点击确定
        self.click_(self.loc_nicheng_queding)

        #判断昵称“!@#$%”是否修改成功
        result = self.is_element_Exist(self.loc_dy_teshufuhao)

        return result

    @allure.step("昵称-输入159")
    def nickname_159(self):
        "昵称-输入159"

        #点击昵称
        self.click_(self.loc_niceng)

        #输入159
        self.send_Keys(self.loc_niceng_shurukuang, "159")

        #点击确定
        self.click_(self.loc_nicheng_queding)

        #判断昵称“159”是否修改成功
        result = self.is_element_Exist(self.loc_dy_159)

        return result

    @allure.step("昵称-取消")
    def nickname_cancel(self):
        "昵称-取消"

        #点击昵称
        self.click_(self.loc_niceng)

        #点击取消
        self.click_(self.loc_nicheng_quxiao)

        #取消昵称应还为“159”，判断昵称“159”是否还在页面
        result = self.is_element_Exist(self.loc_dy_159)

        return result

    @allure.step('年龄-输入1岁')
    def age_1(self):
        "年龄-输入1岁"

        #点击年龄
        self.click_(self.loc_nianling)

        #输入1
        self.send_Keys(self.loc_nianling_shurukuang, "1")

        #点击确定
        self.click_(self.loc_queding_nianling)

        #判断年龄是否修改为“1”
        result = self.is_element_Exist(self.loc_dy_nianling_1)

        return result

    @allure.step('年龄-输入0岁')
    def age_0(self):
        "年龄-输入0岁"

        #点击年龄
        self.click_(self.loc_nianling)

        #输入0
        self.send_Keys(self.loc_nianling_shurukuang, "0")

        #点击确定
        self.click_(self.loc_queding_nianling)

        #判断年龄是否修改为“0”
        result = self.is_element_Exist(self.loc_dy_nianling_0)

        return result

    @allure.step('年龄-输入99岁')
    def age_99(self):
        "年龄-输入99岁"

        #点击年龄
        self.click_(self.loc_nianling)

        #输入99
        self.send_Keys(self.loc_nianling_shurukuang, "99")

        #点击确定
        self.click_(self.loc_queding_nianling)

        #判断年龄是否修改为“99”
        result = self.is_element_Exist(self.loc_dy_nianling_99)

        return result

    @allure.step('年龄-输入18岁')
    def age_18(self):
        "年龄-输入18岁"

        #点击年龄
        self.click_(self.loc_nianling)

        #输入18
        self.send_Keys(self.loc_nianling_shurukuang, "18")

        #点击确定
        self.click_(self.loc_queding_nianling)

        #判断年龄是否修改为“18”
        result = self.is_element_Exist(self.loc_dy_nianling_18)

        return result

    @allure.step("年龄-不输入")
    def age_not_enter(self):
        "年龄-不输入"

        #点击年龄
        self.click_(self.loc_nianling)

        #不输入，直接点击确定
        self.click_(self.loc_queding_nianling)

        #判断年龄是否还为“18”
        result = self.is_element_Exist(self.loc_dy_nianling_18)

        return result

    @allure.step("年龄-取消")
    def age_cancel(self):
        "年龄-取消"

        #点击年龄
        self.click_(self.loc_nianling)

        #点击取消
        self.click_(self.loc_quxiao_nianling)

        #判断年龄是否还为“18”
        result = self.is_element_Exist(self.loc_dy_nianling_18)

        return result

    @allure.step('性别-男')
    def man(self):
        "性别-男"

        #点击性别
        self.click_(self.loc_xingbie)

        #点击男
        self.click_(self.loc_nan)

        #判断性别是否修改为男
        result = self.is_element_Exist(self.loc_dy_nan)

        return result

    @allure.step('性别-女')
    def woman(self):
        "性别-女"

        #点击性别
        self.click_(self.loc_xingbie)

        #点击女
        self.click_(self.loc_nv)

        #判断性别是否修改为女
        result = self.is_element_Exist(self.loc_dy_nv)

        return result

    @allure.step("性别-取消")
    def gender_cancel(self):
        "性别-取消"

        #点击性别
        self.click_(self.loc_xingbie)

        #点击取消
        self.click_(self.loc_quxiao_xingbie)

        #取消，判断性别还为女
        result = self.is_element_Exist(self.loc_dy_nv)

        return result

    @allure.step("年级-不选择")
    def uncheck(self):
        "年级-不选择"

        #点击年级
        self.click_(self.loc_nianji)

        #点击确定
        self.click_(self.loc_queding_nianji)

        #判断还在选择年级页面
        result = self.is_element_Exist(self.loc_buxuanze)

        return result


    @allure.step("年级-幼儿园小班")
    def primary_class(self):
        "年级-幼儿园小班"

        #点击幼儿园小班
        self.click_(self.loc_youeryuanxiaoban)

        #点击确定
        self.click_(self.loc_queding_nianji)

        #判断幼儿园小班是否修改成功
        result = self.is_element_Exist(self.loc_dy_youeryuanxiaoban)

        return result

    @allure.step("年级-大学四年级")
    def senior(self):
        "年级-大学四年级"

        #点击年级
        self.click_(self.loc_nianji)

        #点击大学四年级
        self.click_(self.loc_daxuesinianji)

        #点击确定
        self.click_(self.loc_queding_nianji)

        #判断大学四年级是否修改成功
        result = self.is_element_Exist(self.loc_dy_daxuesinianji)

        return result

    @allure.step("年级-小学五年级")
    def fifth_grade(self):
        "年级-小学五年级"

        #点击年级
        self.click_(self.loc_nianji)

        #点击小学五年级
        self.click_(self.loc_xiaoxuewunianji)

        #点击确定
        self.click_(self.loc_queding_nianji)

        #判断小学五年级是否修改成功
        result = self.is_element_Exist(self.loc_dy_xiaoxuewunianji)

        #回退
        self.driver.press_keycode(4)

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        #点击学习记录，保准每个用例集的起点一致
        self.click_(self.loc_xuexijilu)

        #休眠5秒，等待页面加载
        sleep(5)

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        #休眠5秒，等待页面加载
        sleep(5)

        return result
