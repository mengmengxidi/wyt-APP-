from common.baseapp import BaseApp
from time import sleep
import os
import allure

class Pen_Setting(BaseApp):
    """点读笔设置"""

    #元素定位
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的
    loc_vt_10 = ("id", "com.viaton.wyt:id/tv_pen")  #VT-10
    loc_dy_diandubishezhi = ("id", "com.viaton.wyt:id/tv_title")  #判断是否进入点读笔设置
    loc_wodebi = ("id", "com.viaton.wyt:id/tv_my_pen")  #我的笔，点击断开连接
    loc_quxiao_duankailianjie = ("id", "com.viaton.wyt:id/tv_cancel")  #取消-断开连接
    loc_queding_duankailianjie = ("id", "com.viaton.wyt:id/tv_confirm")  #确定-断开连接
    loc_wifi_shezhi = ("xpath", "//*[@text='Wi-Fi设置']")  #wifi设置
    loc_huancunguanli = ("xpath", "//*[@text='缓存管理']")  #缓存管理
    loc_dy_huancunguanli = ("id", "com.viaton.wyt:id/tv_title")  #断言缓存管理
    loc_shanchu_huancun = ("id", "com.viaton.wyt:id/tv_right")  #删除缓存按钮
    loc_quanxuan = ("xpath", "//*[@text='全选']")  #全选
    loc_shanchu_quanbu = ("id", "com.viaton.wyt:id/tv_delete")  #删除全部按钮
    loc_quxiao_shanchu = ("id", "com.viaton.wyt:id/tv_cancle")  #取消删除
    loc_queding_shanchu = ("id", "com.viaton.wyt:id/tv_confirm")  #确定删除
    loc_dy_shanchu_chenggong = ("xpath", "//*[@text='暂无缓存,请继续保持']")  #判断删除完成
    loc_gujianshengji = ("xpath", "//*[@text='固件升级']")  #固件升级
    loc_lanyayinxiang = ("xpath", "//*[@text='蓝牙音箱']")  #蓝牙音箱
    loc_dy_lanyaxinxiang = ("id", "com.viaton.wyt:id/tv_title")  #断言蓝牙音箱
    loc_shuaxin_lanyayinxiang = ("id", "com.viaton.wyt:id/tv_right")  #刷新
    loc_zidongxiazai = ("xpath", "//*[@text='自动下载']")  #自动下载
    loc_dy_zidongxiazai = ("id", "com.viaton.wyt:id/tv_title")  #断言自动下载设置
    loc_jinyong_zidongxiazai = ("xpath", "//*[@text='禁用']")  #禁用
    loc_dy_jinyong_zidongxiazai = ("xpath", "//*[@text='禁用']")  #断言禁用
    loc_kaiqi_zidongxiazai = ('xpath', "//*[@text='开启']")  #开启
    loc_dy_kaiqi_zidongxiazai = ('xpath', "//*[@text='开启']")  #断言开启
    loc_xiumianshijian = ("xpath", "//*[@text='休眠时间']")  #休眠时间
    loc_dy_xiumianshijian = ("xpath", "//*[@text='休眠时间设置']")  #断言休眠时间设置
    loc_xiumianshijian_5 = ("xpath", "//*[@text='5分钟']")  #5分钟
    loc_dy_xiumianshijian_5 = ("xpath", "//*[@text='5分钟']")  #断言5分钟
    loc_xiumianshijian_10 = ("xpath", "//*[@text='10分钟']")  #10分钟
    loc_dy_xiumianshijian_10 = ("xpath", "//*[@text='10分钟']")  #断言10分钟
    loc_xiumianshijian_30 = ("xpath", "//*[@text='30分钟']")  #30分钟
    loc_dy_xiumianshijian_30 = ("xpath", "//*[@text='30分钟']")  #断言30分钟
    loc_xiumianshijian_yongbu = ("xpath", "//*[@text='永不']")  #永不
    loc_dy_xiumianshijian_yongbu = ("xpath", "//*[@text='永不']")  #断言永不
    loc_zidongguanji = ("xpath", "//*[@text='自动关机']")  #自动关机
    loc_dy_zidongguanji = ("id", "com.viaton.wyt:id/tv_title")  #判断自动关机
    loc_zidongguanji_30 = ("xpath", "//*[@text='30分钟']")  #30分钟
    loc_dy_zidongguanji_30 = ("xpath", "//*[@text='30分钟']")  #断言30分钟
    loc_zidongguanji_60 = ("xpath", "//*[@text='60分钟']")  #60分钟
    loc_dy_zidongguanji_60 = ("xpath", "//*[@text='60分钟']")  #断言60分钟
    loc_zidongguanji_120 = ("xpath", "//*[@text='120分钟']")  #120分钟
    loc_dy_zidongguanji_120 = ("xpath", "//*[@text='120分钟']")  #断言120分钟
    loc_zidongguanji_yongbu = ("xpath", "//*[@text='永不']")  #永不
    loc_dy_zidongguanji_yongbu = ("xpath", "//*[@text='永不']")  #永不
    loc_benjixinxi = ("xpath", "//*[@text='本机信息']")  #本机信息
    loc_dy_benjixinxi_1 = ("xpath", "//*[@text='本机信息']")  #本机信息
    loc_dy_benjixinxi_2 = ("xpath", "//*[@text='电量']")  #电量
    loc_dy_benjixinxi_3 = ("xpath", "//*[@text='容量']")  #容量
    loc_dy_benjixinxi_4 = ("xpath", "//*[@text='型号']")  #型号
    loc_dy_benjixinxi_5 = ("xpath", "//*[@text='软件版本']")  #软件版本
    loc_dy_benjixinxi_6 = ("xpath", "//*[@text='系统版本']")  #系统版本
    loc_dy_benjixinxi_7 = ("xpath", "//*[@text='笔ID']")  #笔ID
    loc_dy_benjixinxi_8 = ("xpath", "//*[@text='序列号']")  #序列号
    loc_pingmuxianshinicheng = ("xpath", "//*[@text='屏幕显示昵称']")  #屏幕显示昵称
    loc_dy_pingmuxianshinicheng = ("id", "com.viaton.wyt:id/tv_title")  #断言屏幕显示昵称
    loc_shurukuang_xiugainicheng = ("xpath", "//*[@text='请输入11字以内的昵称']")  #修改昵称输入框
    loc_baocun_xiugainicheng = ("id", "com.viaton.wyt:id/tv_modify")  #保存-修改昵称
    loc_dy_xiugainicheng_1 = ("xpath", "//*[@text='1']")  #断言输入“1”保存成功
    loc_dy_xiugainicheng_10 = ("xpath", "//*[@text='abc1234ABC']")  #断言输入“abc1234ABC”保存成功
    loc_dy_xiugainicheng_11 = ('xpath', "//*[@text='0.12ABCBabc']")  #断言输入“	0.12ABCBabc”保存成功
    loc_dy_xiugainicheng_fuhao = ("xpath", "//*[@text='!@#$%^*']")  #断言输入“!@#$%^&*”保存成功
    loc_dy_xiugainicheng_159 = ("xpath", "//*[@text='159']")  #断言输入“159”保存成功
    loc_xuexizhanghao = ("xpath", "//*[@text='学习帐号']")  #学习帐号
    loc_dy_xuexizhanghao = ("xpath", "//*[@text='绑定帐号设置']")  #断言学习账号
    loc_yichubangding = ("id", "com.viaton.wyt:id/tv_bottom_button")  #移除绑定
    loc_quxiao_yichubangding = ("id", "com.viaton.wyt:id/tv_cancle")  #取消-移除绑定
    loc_queding_yichubangding = ("id", "com.viaton.wyt:id/tv_confirm")  #确定-移除绑定
    loc_dy_queding_yichubangding = ("xpath", "//*[@text='15927391992']")  #断言-移除绑定
    loc_bangdingxinbi = ("id", "com.viaton.wyt:id/tv_bind_new_pen")  #绑定新笔
    loc_quxiao_bangdingxinbi = ("id", "com.viaton.wyt:id/tv_cancle")  #取消-绑定新笔
    loc_queding_bangdingxinbi = ("id", "com.viaton.wyt:id/tv_confirm")  #确定-绑定新笔
    loc_vt_10_bangdingxinbi = ("id", "com.viaton.wyt:id/tv_vt_10")  #选择vt-10
    loc_woyikaiji_xiayibu = ("id", "com.viaton.wyt:id/tv_next")  #我以开机，下一步
    loc_queding = ("id", "com.viaton.wyt:id/tv_confirm")  #确定
    loc_dy_bangdingxinbi = ("xpath", "//*[@text='连接成功']")  #断言连接成功
    loc_kaishishiyong = ("id", "com.viaton.wyt:id/tv_bind_pen_with_account_cancel")  #开始使用
    loc_cha = ("id", "com.viaton.wyt:id/iv_close")  #绑定新笔后，点击×
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习
    loc_queding_lianjie = ("id", "com.viaton.wyt:id/tv_confirm")  #确定-连接笔
    loc_dy_wifi_shezhi = ("id", "com.viaton.wyt:id/tv_title")  #判断进入点读笔wifi设置页面
    loc_shuaxin = ("id", "com.viaton.wyt:id/tv_right")  #刷新
    loc_tianjiawangluo = ("id", "com.viaton.wyt:id/tv_add_wifi")  #添加网络
    loc_dy_tianjiawangluo = ("xpath", "//*[@text='输入网络信息']")  #输入网络信息


    @allure.step("点读笔设置-页面显示")
    def display(self):
        "点读笔设置-页面显示"

        #休眠3秒
        sleep(3)

        #点击我的
        self.click_(self.loc_wode)

        #点击vt-10
        self.click_(self.loc_vt_10)

        #休眠3秒
        sleep(3)

        #判断是否进入点读笔设置页面
        result = self.is_element_Exist(self.loc_dy_diandubishezhi)

        return result

    @allure.step("断开连接-取消")
    def disconnect_cancel(self):
        "断开连接-取消"

        #点击右上角我的笔
        self.click_(self.loc_wodebi)

        #点击取消
        self.click_(self.loc_quxiao_duankailianjie)

        #取消后，wifi设置应该继续显示
        result = self.is_element_Exist(self.loc_wifi_shezhi)

        return result

    @allure.step("断开连接")
    def disconnect(self):
        "断开连接"

        #点击右上角我的笔
        self.click_(self.loc_wodebi)

        #点击确定
        self.click_(self.loc_queding_duankailianjie)

        #取消后，wifi设置应该消失
        result = self.is_element_Exist(self.loc_wifi_shezhi)

        return result

    @allure.step("连接")
    def connect(self):
        "连接"

        #点击右上角我的笔
        self.click_(self.loc_wodebi)

        #点击确定
        self.click_(self.loc_queding_lianjie)

        #休眠5秒
        sleep(5)

        #成功连接后，wifi设置应该继续显示
        result = self.is_element_Exist(self.loc_wifi_shezhi)

        return result

    @allure.step("wifi")
    def wifi(self):

        #点击wifi设置
        self.click_(self.loc_wifi_shezhi)

        #休眠10秒
        sleep(10)

        #判断是否进入wifi设置页面
        result = self.is_element_Exist(self.loc_dy_wifi_shezhi)

        return result

    @allure.step("刷新")
    def refresh(self):
        "刷新"

        #点击刷新
        self.click_(self.loc_shuaxin)

        #休眠10秒
        sleep(10)

        #判断是否还在wifi设置页面
        result = self.is_element_Exist(self.loc_dy_wifi_shezhi)

        return result

    @allure.step("添加网络")
    def add_networking(self):
        "添加网络"

        #点击添加网络
        self.click_(self.loc_tianjiawangluo)

        #判断是否进入输入网络信息页面
        result = self.is_element_Exist(self.loc_dy_tianjiawangluo)

        #回退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("缓存管理")
    def cache(self):
        "缓存管理"

        #点击缓存管理
        self.click_(self.loc_huancunguanli)

        #判断是否进入缓存管理页面
        result = self.is_element_Exist(self.loc_dy_huancunguanli)

        return result

    @allure.step("删除缓存-取消")
    def delete_cache_cancel(self):
        "删除缓存-取消"

        #点击删除
        self.click_(self.loc_shanchu_huancun)

        #休眠3秒
        sleep(3)

        #点击全选
        self.click_(self.loc_quanxuan)

        #点击删除
        self.click_(self.loc_shanchu_quanbu)

        #点击取消
        self.click_(self.loc_quxiao_shanchu)

        #判断删除按钮还在页面
        result = self.is_element_Exist(self.loc_shanchu_quanbu)

        return result

    @allure.step("删除缓存")
    def delete_cache(self):
        "删除缓存"

        #点击删除
        self.click_(self.loc_shanchu_quanbu)

        #点击确定
        self.click_(self.loc_queding_shanchu)

        #休眠5秒,等待删除完成
        sleep(5)

        #判断“暂无缓存,请继续保持”显示在页面，表示删除成功
        result = self.is_element_Exist(self.loc_dy_shanchu_chenggong)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("固件升级")
    def upgrade(self):
        "固件升级"

        #点击固件升级
        self.click_(self.loc_gujianshengji)

        #提示点读笔已经是最新版本，判断还在点读笔设置页面
        result = self.is_element_Exist(self.loc_gujianshengji)

        return result

    @allure.step("蓝牙音箱")
    def bluetooth_speaker(self):
        "蓝牙音箱"

        #点击蓝牙音箱
        self.click_(self.loc_lanyayinxiang)

        #休眠5秒,等待页面加载完成
        sleep(5)

        #判断进入蓝牙音箱页面
        result = self.is_element_Exist(self.loc_dy_lanyaxinxiang)

        return result

    @allure.step("蓝牙音箱-刷新")
    def bluetooth_speaker_refresh(self):
        "蓝牙音箱-刷新"

        #点击刷新
        self.click_(self.loc_shuaxin_lanyayinxiang)

        #休眠8秒
        sleep(8)

        #刷新后，判断页面还在蓝牙音箱
        result = self.is_element_Exist(self.loc_dy_lanyaxinxiang)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("自动下载")
    def automatic_download(self):
        "自动下载"

        #点击自动下载
        self.click_(self.loc_zidongxiazai)

        #判断回到自动下载设置页面
        result = self.is_element_Exist(self.loc_dy_zidongxiazai)

        return result

    @allure.step("自动下载-禁用")
    def forbidden(self):
        "自动下载-禁用"

        #点击禁用
        self.click_(self.loc_jinyong_zidongxiazai)

        #判断点读笔设置页面，自动下载显示为禁用
        result = self.is_element_Exist(self.loc_dy_jinyong_zidongxiazai)

        return result

    @allure.step("自动下载-开启")
    def open(self):
        "自动下载-开启"

        #点击自动下载
        self.click_(self.loc_zidongxiazai)

        #点击开启
        self.click_(self.loc_kaiqi_zidongxiazai)

        #判断点读笔设置页面，自动下载显示为开启
        result = self.is_element_Exist(self.loc_dy_kaiqi_zidongxiazai)

        return result

    @allure.step("休眠时间")
    def sleep_time(self):
        "休眠时间"

        #点击休眠时间
        self.click_(self.loc_xiumianshijian)

        #判断是否进入休眠时间设置页面
        result = self.is_element_Exist(self.loc_dy_xiumianshijian)

        return result

    @allure.step("休眠时间-5分钟")
    def sleep_time_5(self):
        "休眠时间-5分钟"

        #点击休眠时间5分钟
        self.click_(self.loc_xiumianshijian_5)

        #休眠1秒
        sleep(1)

        #判断点读笔设置页面，休眠时间显示为5分钟
        result = self.is_element_Exist(self.loc_dy_xiumianshijian_5)

        return result

    @allure.step("休眠时间-10分钟")
    def sleep_time_10(self):
        "休眠时间-10分钟"

        #点击休眠时间
        self.click_(self.loc_xiumianshijian)

        #点击休眠时间10分钟
        self.click_(self.loc_xiumianshijian_10)

        #休眠1秒
        sleep(1)

        #判断点读笔设置页面，休眠时间显示为10分钟
        result = self.is_element_Exist(self.loc_dy_xiumianshijian_10)

        return result

    @allure.step("休眠时间-30分钟")
    def sleep_time_30(self):
        "休眠时间-30分钟"

        #点击休眠时间
        self.click_(self.loc_xiumianshijian)

        #点击休眠时间30分钟
        self.click_(self.loc_xiumianshijian_30)

        #休眠1秒
        sleep(1)

        #判断点读笔设置页面，休眠时间显示为30分钟
        result = self.is_element_Exist(self.loc_dy_xiumianshijian_30)

        return result

    @allure.step("休眠时间-永不")
    def sleep_time_perpetual(self):
        "休眠时间-永不"

        #点击休眠时间
        self.click_(self.loc_xiumianshijian)

        #点击休眠时间永不
        self.click_(self.loc_xiumianshijian_yongbu)

        #休眠1秒
        sleep(1)

        #判断点读笔设置页面，休眠时间显示为永不
        result = self.is_element_Exist(self.loc_dy_xiumianshijian_yongbu)

        return result


    @allure.step("自动关机")
    def automatic_shut(self):
        "自动关机"

        #点击自动关机
        self.click_(self.loc_zidongguanji)

        #判断进入自动关机设置页面
        result = self.is_element_Exist(self.loc_dy_zidongguanji)

        return result

    @allure.step("自动关机-30分钟")
    def automatic_shut_30(self):
        "自动关机-30分钟"

        #点击30分钟
        self.click_(self.loc_zidongguanji_30)

        #休眠1秒
        sleep(1)

        #判断点读笔设置页面，自动关机显示为30分钟
        result = self.is_element_Exist(self.loc_dy_zidongguanji_30)

        return result

    @allure.step("自动关机-60分钟")
    def automatic_shut_60(self):
        "自动关机-60分钟"

        #点击自动关机
        self.click_(self.loc_zidongguanji)

        #点击60分钟
        self.click_(self.loc_zidongguanji_60)

        #休眠1秒
        sleep(1)

        #判断点读笔设置页面，自动关机显示为60分钟
        result = self.is_element_Exist(self.loc_dy_zidongguanji_60)

        return result

    @allure.step("自动关机-120分钟")
    def automatic_shut_120(self):
        "自动关机-120分钟"

        #点击自动关机
        self.click_(self.loc_zidongguanji)

        #点击120分钟
        self.click_(self.loc_zidongguanji_120)

        #休眠1秒
        sleep(1)

        #判断点读笔设置页面，自动关机显示为120分钟
        result = self.is_element_Exist(self.loc_dy_zidongguanji_120)

        return result

    @allure.step("自动关机-永不")
    def automatic_shut_perpetual(self):
        "自动关机-永不"

        #点击自动关机
        self.click_(self.loc_zidongguanji)

        #点击永不
        self.click_(self.loc_zidongguanji_yongbu)

        #休眠1秒
        sleep(1)

        #判断点读笔设置页面，自动关机显示为永不
        result = self.is_element_Exist(self.loc_dy_zidongguanji_yongbu)

        return result



    @allure.step("本机信息")
    def device_info(self):
        "本机信息"

        #点击本机信息
        self.click_(self.loc_benjixinxi)

        #判断本机信息页面中本机信息、电量、容量、型号、软件版本、系统版本、笔ID、序列号是否正确显示
        result_1 = self.is_element_Exist(self.loc_dy_benjixinxi_1)
        result_2 = self.is_element_Exist(self.loc_dy_benjixinxi_2)
        result_3 = self.is_element_Exist(self.loc_dy_benjixinxi_3)
        result_4 = self.is_element_Exist(self.loc_dy_benjixinxi_4)
        result_5 = self.is_element_Exist(self.loc_dy_benjixinxi_5)
        result_6 = self.is_element_Exist(self.loc_dy_benjixinxi_6)
        result_7 = self.is_element_Exist(self.loc_dy_benjixinxi_7)

        if result_1 and result_2 and result_3 and result_4 and result_5 and result_6 and result_7:
            return True
        else:
            return False

    @allure.step("修改昵称-直接点击保存")
    def change_nickname_save(self):
        "修改昵称-直接点击保存"

        #点击屏幕显示昵称
        self.click_(self.loc_pingmuxianshinicheng)

        #直接点击保存
        self.click_(self.loc_baocun_xiugainicheng)

        #直接点击保存，判断页面还在修改屏幕昵称
        result = self.is_element_Exist(self.loc_dy_pingmuxianshinicheng)

        return result

    @allure.step("修改昵称-输入1位数")
    def change_nickname_1(self):
        "修改昵称-输入1位数"

        #输入“1”
        self.send_Keys(self.loc_shurukuang_xiugainicheng, "1")

        #点击修改屏幕昵称，收回键盘
        self.click_(self.loc_dy_pingmuxianshinicheng)

        #直接点击保存
        self.click_(self.loc_baocun_xiugainicheng)

        #判断本机信息，屏幕显示昵称是否修改为“1”
        result = self.is_element_Exist(self.loc_dy_xiugainicheng_1)

        return result

    @allure.step("修改昵称-输入10位数")
    def change_nickname_10(self):
        "修改昵称-输入10位数"

        #点击屏幕显示昵称
        self.click_(self.loc_pingmuxianshinicheng)

        #输入“abc1234ABC”
        self.send_Keys(self.loc_shurukuang_xiugainicheng, "abc1234ABC")

        #点击修改屏幕昵称，收回键盘
        self.click_(self.loc_dy_pingmuxianshinicheng)

        #直接点击保存
        self.click_(self.loc_baocun_xiugainicheng)

        #判断本机信息，屏幕显示昵称是否修改为“abc1234ABC”
        result = self.is_element_Exist(self.loc_dy_xiugainicheng_10)

        return result

    @allure.step("修改昵称-输入11位数")
    def change_nickname_11(self):
        "修改昵称-输入11位数"

        #点击屏幕显示昵称
        self.click_(self.loc_pingmuxianshinicheng)

        #输入“0.12ABCBabc”
        self.send_Keys(self.loc_shurukuang_xiugainicheng, "0.12ABCBabc")

        #点击修改屏幕昵称，收回键盘
        self.click_(self.loc_dy_pingmuxianshinicheng)

        #直接点击保存
        self.click_(self.loc_baocun_xiugainicheng)

        #判断本机信息，屏幕显示昵称是否修改为“0.12ABCBabc”
        result = self.is_element_Exist(self.loc_dy_xiugainicheng_11)

        return result

    @allure.step("修改昵称-输入特殊符号")
    def change_nickname_symbol(self):
        "修改昵称-输入特殊符号"

        #点击屏幕显示昵称
        self.click_(self.loc_pingmuxianshinicheng)

        #输入“!@#$%^&*”
        self.send_Keys(self.loc_shurukuang_xiugainicheng, "!@#$%^*")

        #点击修改屏幕昵称，收回键盘
        self.click_(self.loc_dy_pingmuxianshinicheng)

        #直接点击保存
        self.click_(self.loc_baocun_xiugainicheng)

        #判断本机信息，屏幕显示昵称是否修改为“!@#$%^&*”
        result = self.is_element_Exist(self.loc_dy_xiugainicheng_fuhao)

        return result

    @allure.step("修改昵称-输入159")
    def change_nickname_159(self):
        "修改昵称-输入159"

        #点击屏幕显示昵称
        self.click_(self.loc_pingmuxianshinicheng)

        #输入“159”
        self.send_Keys(self.loc_shurukuang_xiugainicheng, "159")

        #点击修改屏幕昵称，收回键盘
        self.click_(self.loc_dy_pingmuxianshinicheng)

        #直接点击保存
        self.click_(self.loc_baocun_xiugainicheng)

        #判断本机信息，屏幕显示昵称是否修改为“159”
        result = self.is_element_Exist(self.loc_dy_xiugainicheng_159)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("学习账号")
    def learning_account(self):
        "学习账号"

        #点击学习账号
        self.click_(self.loc_xuexizhanghao)

        #判断是否进入“绑定账号设置”页面
        result = self.is_element_Exist(self.loc_dy_xuexizhanghao)

        return result

    @allure.step("移除绑定-取消")
    def remove_binding_cancel(self):
        "移除绑定"

        #点击移除绑定
        self.click_(self.loc_yichubangding)

        #点击取消
        self.click_(self.loc_quxiao_yichubangding)

        #判断移除绑定还在页面上
        result = self.is_element_Exist(self.loc_yichubangding)

        return result

    @allure.step("移除绑定")
    def remove_binding(self):
        "移除绑定"

        #点击移除绑定
        self.click_(self.loc_yichubangding)

        #点击确定
        self.click_(self.loc_queding_yichubangding)

        #判断1学习账号“15927391992”不显示在点读笔设置中
        result = self.is_element_Exist(self.loc_dy_queding_yichubangding)

        return result

    @allure.step("绑定学习账号")
    def binding_study_account(self):
        "绑定学习账号"

        #点击学习账号
        self.click_(self.loc_xuexizhanghao)

        #绑定成功后，判断1学习账号“15927391992”显示在点读笔设置中
        result = self.is_element_Exist(self.loc_dy_queding_yichubangding)

        return result

    @allure.step("绑定新笔-取消")
    def binding_new_pen_cancel(self):
        "绑定新笔-取消"

        #点击绑定新笔
        self.click_(self.loc_bangdingxinbi)

        #点击取消
        self.click_(self.loc_quxiao_bangdingxinbi)

        #判断绑定新笔还显示在页面
        result = self.is_element_Exist(self.loc_bangdingxinbi)

        return result

    @allure.step("绑定新笔-成功")
    def  binding_new_pen(self):
        "绑定新笔"

        #点击绑定新笔
        self.click_(self.loc_bangdingxinbi)

        #点击确定
        self.click_(self.loc_queding_bangdingxinbi)

        #选择vt-10笔
        self.click_(self.loc_vt_10_bangdingxinbi)

        #点击我已开始，下一步
        self.click_(self.loc_woyikaiji_xiayibu)

        #点击屏幕中间
        cmd = "adb shell input tap 540 1129"
        os.system(cmd)

        #休眠15秒，等待搜索完成
        sleep(15)

        #点击确定
        self.click_(self.loc_queding_bangdingxinbi)

        #休眠15秒，等待绑定成功
        sleep(15)

        #判断连接成功页面是否正确显示
        result = self.is_element_Exist(self.loc_dy_bangdingxinbi)

        #点击开始使用
        self.click_(self.loc_kaishishiyong)

        #休眠20秒，等待页面加载
        sleep(20)

        #回退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #点击×
        try:
            self.click_(self.loc_cha)
        except:
            print("绑定新笔没有弹窗")

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        #休眠5秒
        sleep(5)

        return result
