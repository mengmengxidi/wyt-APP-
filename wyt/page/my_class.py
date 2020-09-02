from common.baseapp import BaseApp
from time import sleep
import os
import allure

class My_Class(BaseApp):
    """我的班级"""

    #元素定位
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的
    loc_wodebanji = ("xpath", "//*[@text='我的班级']")  #我的班级
    loc_dy_wodebanji_1 = ("id", "com.viaton.wyt:id/tv_title")  #断言我的班级title
    loc_dy_wodebanji_2 = ("xpath", "//*[@text='班级编号']")  #断言班级编号
    loc_dy_wodebanji_3 = ("xpath", "//*[@text='我的学校']")  #断言我的学校
    loc_sandian_youshangjiao = ("id", "com.viaton.wyt:id/iv_right")  #三点-右上角
    loc_quxiao_tuichubanji = ("id", "com.viaton.wyt:id/tv_cancel")  #取消退出班级
    loc_tuichubanji = ("id", "com.viaton.wyt:id/ll_root")  #退出班级
    loc_dy_tuichubanji = ("xpath", "//*[@text='完善班级信息']")  #断言退出班级，完善班级信息在页面上
    loc_quxiao_bianji = ("id", "com.viaton.wyt:id/tv_cancel")  #取消编辑
    loc_chongxinbianji = ("id", "com.viaton.wyt:id/ll_root")  #重新编辑
    loc_dy_chongxinbianji = ("xpath", "//*[@text='完善班级信息']")  #断言重新编辑
    loc_nidexuexijieduan = ("xpath", "//*[@text='请选择你的学习阶段']")  #请选择你的学习阶段
    loc_nidebanji = ("xpath", "//*[@text='请选择你的班级']")  #请选择你的班级
    loc_nijiududexuexiao = ("xpath", "//*[@text='请填写你就读的学校']")  #请填写你就读的学校
    loc_shurukuang_xuexiao = ("id", "com.viaton.wyt:id/et_input")  #输入框-输入学校
    loc_queding_shuruxuexiao = ("id", "com.viaton.wyt:id/tv_confirm")  #确定-输入学校
    loc_nishiyongdejiaocai = ("xpath", "//*[@text='请选择你使用的教材版本']")  #请选择你使用的教材版本
    loc_queding_nishiyongdejiaocaibanben = ("id", "com.viaton.wyt:id/btnSubmit")  #确定-你使用的教材版本
    loc_queding_bianjibanjixinxi = ("id", "com.viaton.wyt:id/btnSubmit")  #确定-编辑班级信息
    loc_dy_1_bianjibanjixinxi = ("xpath", "//*[@text='a']")  #输入1位
    loc_dy_20_bianjibanjixinxi = ("xpath", "//*[@text='!@#$%6.254ZXCVBlkjhg']")  #输入20位
    loc_dy_jianghan_school_bianjibanjixinxi = ("xpath", "//*[@text='jianghan_school']")  #输入jianghan_school
    loc_shurubanjiyaoqingma = ("id", "com.viaton.wyt:id/rb_invitation_code")  #输入班级邀请码
    loc_qingshurulaoshigeideyaoqingma = ("xpath", "//*[@text='请输入老师给的邀请码']")  #请输入老师给的邀请码
    loc_shurukuang_banjiyaoqingma = ("id", "com.viaton.wyt:id/et_input")  #输入框-班级邀请码
    loc_queding_banjiyaoqingma = ("id", "com.viaton.wyt:id/tv_confirm")  #确定-班级邀请码
    loc_qingshurunidezhenshixingming = ('xpath', "//*[@text='请输入你的真实姓名']")  #请输入你的真实姓名
    loc_shurukuang_zhenshixingming = ("id", "com.viaton.wyt:id/et_input")  #输入框-真实姓名
    loc_queding_zhenshixingming = ("id", "com.viaton.wyt:id/tv_confirm")  #确定-真实姓名
    loc_queren_wanshanbanjixinxi = ("id", "com.viaton.wyt:id/confirm")  #确认-完善班级信息
    loc_jiarubanji = ("id", "com.viaton.wyt:id/confirm")  #加入班级
    loc_dy_jiarubanji_chenggong = ("xpath", "//*[contains(@text,'你是第')]")  #断言加入班级成功
    loc_fanhui = ("id", "com.viaton.wyt:id/tv_back")  #返回
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习

    @allure.step("我的班级")
    def my_class(self):
        "我的班级"

        #点击我的
        self.click_(self.loc_wode)

        #点击我的班级
        self.click_(self.loc_wodebanji)

        #判断我的班级title、班级编号、我的学校是否正确显示
        result_1 = self.is_element_Exist(self.loc_dy_wodebanji_1)
        result_2 = self.is_element_Exist(self.loc_dy_wodebanji_2)
        result_3 = self.is_element_Exist(self.loc_dy_wodebanji_3)

        if result_1 and result_2 and result_3:
            return True
        else:
            return False

    @allure.step("退出班级-取消")
    def out_class_cancel(self):
        "退出班级-取消"

        #点击右上角三点
        self.click_(self.loc_sandian_youshangjiao)

        #点击取消
        self.click_(self.loc_quxiao_tuichubanji)

        #判断又回到我的班级页面
        result = self.is_element_Exist(self.loc_sandian_youshangjiao)

        return result

    @allure.step("退出班级")
    def out_class(self):
        "退出班级"

        #点击右上角三点
        self.click_(self.loc_sandian_youshangjiao)

        #点击退出班级
        self.click_(self.loc_tuichubanji)

        #判断退出班级成功
        result = self.is_element_Exist(self.loc_dy_tuichubanji)

        return result

    @allure.step("重新编辑-取消")
    def reedit_cancel(self):
        "重新编辑-取消"

        #点击我的班级
        self.click_(self.loc_wodebanji)

        #点击右上角三点
        self.click_(self.loc_sandian_youshangjiao)

        #点击取消
        self.click_(self.loc_quxiao_bianji)

        #判断右上角3个点还在页面上
        result = self.is_element_Exist(self.loc_sandian_youshangjiao)

        return result

    @allure.step("重新编辑")
    def reedit(self):
        "重新编辑"

        #点击右上角三点
        self.click_(self.loc_sandian_youshangjiao)

        #点击重新编辑
        self.click_(self.loc_chongxinbianji)

        #判断是否进入重新编辑页面
        result = self.is_element_Exist(self.loc_dy_chongxinbianji)

        return result

    @allure.step("编辑班级信息-学校输入1位数")
    def class_info_1(self):
        "编辑班级信息-学校输入1位数"

        #点击年级
        self.click_(self.loc_nidexuexijieduan)

        #点击确定
        self.click_(self.loc_queding_bianjibanjixinxi)

        #点击班级
        self.click_(self.loc_nidebanji)

        #点击确定
        self.click_(self.loc_queding_bianjibanjixinxi)

        #点击学校
        self.click_(self.loc_nijiududexuexiao)

        #输入“a”
        self.send_Keys(self.loc_shurukuang_xuexiao, "a")

        #点击确定
        self.click_(self.loc_queding_shuruxuexiao)

        #点击教材版本
        self.click_(self.loc_nishiyongdejiaocai)

        #点击确定
        self.click_(self.loc_queding_nishiyongdejiaocaibanben)

        #点击确认
        self.click_(self.loc_queren_wanshanbanjixinxi)

        #点击我的班级
        self.click_(self.loc_wodebanji)

        #学校修改为“a”，判断我的学校为“a”
        result = self.is_element_Exist(self.loc_dy_1_bianjibanjixinxi)

        return result

    @allure.step("编辑班级信息-学校输入20位数")
    def class_info_20(self):
        "编辑班级信息-学校输入20位数"

        #点击右上角三点
        self.click_(self.loc_sandian_youshangjiao)

        #点击重新编辑
        self.click_(self.loc_chongxinbianji)

        #点击年级
        self.click_(self.loc_nidexuexijieduan)

        #点击确定
        self.click_(self.loc_queding_bianjibanjixinxi)

        #点击班级
        self.click_(self.loc_nidebanji)

        #点击确定
        self.click_(self.loc_queding_bianjibanjixinxi)

        #点击学校
        self.click_(self.loc_nijiududexuexiao)

        #输入“!@#$%6.254ZXCVBlkjhg”
        self.send_Keys(self.loc_shurukuang_xuexiao, "!@#$%6.254ZXCVBlkjhg")

        #点击确定
        self.click_(self.loc_queding_shuruxuexiao)

        #点击教材版本
        self.click_(self.loc_nishiyongdejiaocai)

        #点击确定
        self.click_(self.loc_queding_nishiyongdejiaocaibanben)

        #点击确认
        self.click_(self.loc_queren_wanshanbanjixinxi)

        #点击我的班级
        self.click_(self.loc_wodebanji)

        #学校修改为“!@#$%6.254ZXCVBlkjhg”，判断我的学校为“!@#$%6.254ZXCVBlkjhg”
        result = self.is_element_Exist(self.loc_dy_20_bianjibanjixinxi)

        return result

    @allure.step("编辑班级信息-学校输入jianghan_school")
    def class_info_jianghan_school(self):
        "编辑班级信息-学校输入jianghan_school"

        #点击右上角三点
        self.click_(self.loc_sandian_youshangjiao)

        #点击重新编辑
        self.click_(self.loc_chongxinbianji)

        #点击年级
        self.click_(self.loc_nidexuexijieduan)

        #点击确定
        self.click_(self.loc_queding_bianjibanjixinxi)

        #点击班级
        self.click_(self.loc_nidebanji)

        #点击确定
        self.click_(self.loc_queding_bianjibanjixinxi)

        #点击学校
        self.click_(self.loc_nijiududexuexiao)

        #输入“jianghan_school”
        self.send_Keys(self.loc_shurukuang_xuexiao, "jianghan_school")

        #点击确定
        self.click_(self.loc_queding_shuruxuexiao)

        #点击教材版本
        self.click_(self.loc_nishiyongdejiaocai)

        #点击确定
        self.click_(self.loc_queding_nishiyongdejiaocaibanben)

        #点击确认
        self.click_(self.loc_queren_wanshanbanjixinxi)

        #点击我的班级
        self.click_(self.loc_wodebanji)

        #学校修改为“jianghan_school”，判断我的学校为“jianghan_school”
        result = self.is_element_Exist(self.loc_dy_jianghan_school_bianjibanjixinxi)

        return result

    @allure.step("班级邀请码-错误的班级邀请码")
    def invitation_code_inexistence(self):
        "班级邀请码-错误的班级邀请码"

        #点击右上角三点
        self.click_(self.loc_sandian_youshangjiao)

        #点击重新编辑
        self.click_(self.loc_chongxinbianji)

        #点击输入班级邀请码按钮
        self.click_(self.loc_shurubanjiyaoqingma)

        #点击请输入老师给的邀请码
        self.click_(self.loc_qingshurulaoshigeideyaoqingma)

        #输入不存在的邀请码,如“123456”
        self.send_Keys(self.loc_shurukuang_banjiyaoqingma, "123456")

        #点击确认
        self.click_(self.loc_queding_banjiyaoqingma)

        #点击输入你的真实姓名
        self.click_(self.loc_qingshurunidezhenshixingming)

        #输入“qinneng”
        self.send_Keys(self.loc_shurukuang_zhenshixingming, "qinneng")

        #点击确定
        self.click_(self.loc_queding_zhenshixingming)

        #点击确认
        self.click_(self.loc_queren_wanshanbanjixinxi)

        #输入不存在版班级邀请码，会提示“未查询到相应班级”，判断还在完善班级信息页面
        result = self.is_element_Exist(self.loc_shurubanjiyaoqingma)

        return result

    @allure.step("班级邀请码-正确的班级邀请码")
    def invitation_code(self):
        "班级邀请码-正确的班级邀请码"

        #点击请输入老师给的邀请码
        self.click_(self.loc_qingshurulaoshigeideyaoqingma)

        #输入正确的邀请码,如“001366”
        self.send_Keys(self.loc_shurukuang_banjiyaoqingma, "001366")

        #点击确认
        self.click_(self.loc_queding_banjiyaoqingma)

        #点击输入你的真实姓名
        self.click_(self.loc_qingshurunidezhenshixingming)

        #输入“qinneng”
        self.send_Keys(self.loc_shurukuang_zhenshixingming, "qinneng")

        #点击确定
        self.click_(self.loc_queding_zhenshixingming)

        #点击确认
        self.click_(self.loc_queren_wanshanbanjixinxi)

        #点击加入班级
        self.click_(self.loc_jiarubanji)

        #加入成功后，会提示你是第几个加入班级的同学
        result = self.is_element_Exist(self.loc_dy_jiarubanji_chenggong)

        #点击返回
        self.click_(self.loc_fanhui)

        #点击学习
        self.click_(self.loc_xuexi)

        #休眠5秒
        sleep(5)

        return result
