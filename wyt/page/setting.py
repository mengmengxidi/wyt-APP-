from common.baseapp import BaseApp
from time import sleep
import os
import allure

class Setting(BaseApp):
    """设置"""

    #元素定位
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的
    loc_shezhi = ("xpath", "//*[@text='设置']")  #设置
    loc_dy_shezhi = ("xpath", "//*[@text='App设置']")  #断言设置
    loc_jianchashengji = ("xpath", "//*[@text='检查升级']")  #检查升级
    loc_qingchuhuancun = ("xpath", "//*[@text='清除缓存']")  #清除缓存
    loc_quxiao_qingchuhuancun = ("id", "com.viaton.wyt:id/tv_cancle")  #取消-清除缓存
    loc_queding_qingchuhuancun = ("id", "com.viaton.wyt:id/tv_confirm")  #确定-清除缓存
    loc_dy_queding_qingchuhuancun = ("xpath", "//*[@text='0MB']")  #清除成功后，缓存为0MB
    loc_lanyalianjiemoshi = ("xpath", "//*[@text='蓝牙连接模式']")  #蓝牙连接模式
    loc_dy_lanyalianjiemoshi = ("xpath", "//*[contains(@text,'您在蓝牙连接过程多次尝试仍旧失败')]")  #断言蓝牙连接模式
    loc_BLE = ("xpath", "//*[@text='BLE']")  #BLE
    loc_jindianlanya = ("xpath", "//*[@text='经典蓝牙']")  #经典蓝牙
    loc_guanyuwomen = ("xpath", "//*[@text='关于我们']")  #关于我们
    loc_dy_guanyuwomen = ("xpath", "//*[contains(@text,'当前版本')]")  #断言关于我们
    loc_yinsishuoming = ("xpath", "//*[@text='隐私说明']")  #隐私说明
    loc_dy_yinsishuoming = ("xpath", "//*[@text='隐私条款']")
    loc_zhanghaozhuxiaoshengqing = ("xpath", "//*[@text='帐号注销申请']")  #账号注销申请
    loc_dy_zhanghaozhuxiaoshengqing = ("xpath", "//*[@text='提交']")  #断言账号注销申请
    loc_shiyongbangzhu = ("xpath", "//*[@text='使用帮助']")  #使用帮助
    loc_dy_shiyongbangzhu = ('xpath', "//*[@text='功能使用']")  #断言使用帮助
    loc_1 = ("xpath", "//*[@text='音频点播功能（仅限V10点读笔）']")  #1、音频点播功能（仅限V10点读笔）
    loc_2 = ("xpath", "//*[@text='语音助手功能（V9、V10点读笔）']")  #2、语音助手功能（V9、V10点读笔）
    loc_3 = ("xpath", "//*[@text='口语评测功能（V9、V10点读笔）']")  #3、口语评测功能（V9、V10点读笔）
    loc_4 = ("xpath", "//*[@text='云点视功能']")  #4、云点视功能
    loc_5 = ("xpath", "//*[@text='单词学习如何使用？']")  #5、单词学习如何使用？
    loc_6 = ("xpath", "//*[@text='电子词典如何使用？']")  #6、电子词典如何使用？
    loc_7 = ("xpath", "//*[contains(@text,'为什么安卓系统的手机搜索不到点读笔')]")  #7、为什么用点读笔点击图书封面，读出的书名不对应？
    loc_8 = ("xpath", "//*[@text='为什么安卓系统的手机搜索不到点读笔，无法绑定？']")  #8、为什么安卓系统的手机搜索不到点读笔，无法绑定？
    loc_9 = ("xpath", "//*[@text='云点读时，为什么发出“滴滴”声？']")  #9、云点读时，为什么发出“滴滴”声？
    loc_10 = ("xpath", "//*[@text='点读时为什么提示“网络不成功”？']")  #10、点读时为什么提示“网络不成功”？
    loc_11 = ("xpath", "//*[@text='为什么在APP的书架中，搜索不到想要找的图书？']")  #11、为什么在APP的书架中，搜索不到想要找的图书？
    loc_12 = ("xpath", "//*[@text='如何缓存资源到笔中？']")  #12、如何缓存资源到笔中？
    loc_shiyongshouce = ("xpath", "//*[@text='使用手册']")  #使用手册
    loc_VT_10 = ("xpath", "//*[@text='VT-10']")  #VT-10
    loc_VT_9 = ("xpath", "//*[@text='VT-9']")  #VT-9
    loc_VT_8 = ("xpath", "//*[@text='VT-8 Cloud']")  #VT-8 Cloud
    loc_dy_VT_8_9_10 = ("xpath", "//*[@text='使用手册']")  #VT-10
    loc_yijianfankui = ("xpath", "//*[@text='意见反馈']")  #意见反馈
    loc_lianxifangsi_shouhuijianpan = ("xpath", "//*[contains(@text,'联系方式')]")  #点击联系方式，收回键盘
    loc_shurukuang_yijianhoujianyi = ("xpath", "//*[@class='android.widget.EditText' and @instance='0']")  #意见或建议
    loc_shurukuang_lianxifangsi = ("xpath", "//*[@class='android.widget.EditText' and @instance='1']")  #联系方式
    loc_tijiao = ("xpath", "//*[@text='提交']")  #提交
    loc_dy_a = ("xpath", "//*[@text='a']")  #断言a
    loc_dy_15927391993 = ("xpath", "//*[@text='反馈内容不能为空！']")  #断言15927391992
    loc_kefudianhua = ("xpath", "//*[@text='客服电话']")  #客服电话
    loc_dy_kefudianhua_1 = ("id", 'com.android.contacts:id/dialButton')  #断言客服电话-1
    loc_dy_kefudianhua_2 = ("xpath", "//*[@text='400 898 9008']")  #断言客服电话-2
    loc_xiugaimima = ("xpath", "//*[@text='修改密码']")  #修改密码
    loc_dy_xiugaimima = ("id", "com.viaton.wyt:id/tv_next")  #断言修改密码
    loc_liaojiezhinengdiandubi = ("xpath", "//*[@text='了解智能点读笔']")  #了解智能点读笔
    loc_dy_liaojiezhinengdiandubi = ("id", "com.android.browser:id/topbar")  #断言了解智能点读笔
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习

    @allure.step("设置")
    def setting(self):
        "设置"

        #点击我的
        self.click_(self.loc_wode)

        #点击设置
        self.click_(self.loc_shezhi)

        #判断进入设置页面
        result = self.is_element_Exist(self.loc_dy_shezhi)

        return result

    @allure.step("检查升级")
    def upgrade(self):
        "检查升级"

        #点击检查升级
        self.click_(self.loc_jianchashengji)

        #提示已经是最新版本，判断还在设置页面上
        result = self.is_element_Exist(self.loc_jianchashengji)

        return result

    @allure.step("清楚缓存-取消")
    def clear_cache_cancel(self):
        "清楚缓存-取消"

        #点击清除缓存
        self.click_(self.loc_qingchuhuancun)

        #点击取消
        self.click_(self.loc_quxiao_qingchuhuancun)

        #判断还在设置页面
        result = self.is_element_Exist(self.loc_qingchuhuancun)

        return result

    @allure.step("清楚缓存")
    def clear_cache(self):
        "清楚缓存"

        #点击清除缓存
        self.click_(self.loc_qingchuhuancun)

        #点击确定
        self.click_(self.loc_queding_qingchuhuancun)

        #判断缓存为0MB
        result = self.is_element_Exist(self.loc_dy_queding_qingchuhuancun)

        return result

    @allure.step("蓝牙连接模式")
    def bluetooth_mode(self):
        "蓝牙连接模式"

        #点击蓝牙连接模式
        self.click_(self.loc_lanyalianjiemoshi)

        #判断进入蓝牙连接模式页面
        result = self.is_element_Exist(self.loc_dy_lanyalianjiemoshi)

        return result

    @allure.step("蓝牙连接模式-BLE")
    def bluetooth_mode_BLE(self):
        "蓝牙连接模式-BLE"

        try:
            #点击BLE
            self.click_(self.loc_BLE)

            #休眠3秒
            sleep(3)
        except:
            return False
        else:
            return True

    @allure.step("蓝牙连接模式-经典蓝牙")
    def bluetooth_mode_classic(self):
        "蓝牙连接模式-经典蓝牙"

        try:
            #点击经典模式
            self.click_(self.loc_jindianlanya)

            #休眠3秒
            sleep(3)
        except:
            return False
        else:
            self.driver.press_keycode(4)
            return True

    @allure.step("关于我们")
    def about_us(self):
        "关于我们"

        #点击关于我们
        self.click_(self.loc_guanyuwomen)

        #判断进入版本显示页面
        result = self.is_element_Exist(self.loc_dy_guanyuwomen)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("隐私说明")
    def privacy(self):
        "隐私说明"

        #点击隐私说明
        self.click_(self.loc_yinsishuoming)

        #判断进入隐私说明页面
        result = self.is_element_Exist(self.loc_dy_yinsishuoming)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("护眼模式")
    def eyeshield(self):
        "护眼模式"

        try:
            #休眠3秒
            sleep(3)

            #点击护眼模式按钮,关闭（或打开）护眼模式
            cmd = "adb shell input tap 984 1184"
            os.system(cmd)

            #休眠3秒
            sleep(3)

            #点击护眼模式按钮,关闭（或打开）护眼模式
            cmd = "adb shell input tap 984 1184"
            os.system(cmd)

        except:
            return False
        else:
            return True

    @allure.step("消息推送")
    def push_notification(self):
        "消息推送"

        try:
            #休眠3秒
            sleep(3)

            #点击消息推送按钮,关闭（或打开）护眼模式
            cmd = "adb shell input tap 982 1328"
            os.system(cmd)

            #休眠3秒
            sleep(3)

            #点击消息推送按钮,关闭（或打开）护眼模式
            cmd = "adb shell input tap 982 1328"
            os.system(cmd)

        except:
            return False
        else:
            return True

    @allure.step("使用帮助")
    def usinghelp(self):
        "使用帮助"

        #休眠3秒
        sleep(3)

        #点击使用帮助
        self.click_(self.loc_shiyongbangzhu)

        #休眠5秒
        sleep(5)

        #判断进入使用帮助页面
        result = self.is_element_Exist(self.loc_dy_shiyongbangzhu)

        return result

    @allure.step("使用帮助-第1项")
    def usinghelp_1(self):
        "使用帮助-第1项"

        #点击第1项
        self.click_(self.loc_1)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_1)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用帮助-第2项")
    def usinghelp_2(self):
        "使用帮助-第2项"

        #点击第2项
        self.click_(self.loc_2)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_2)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用帮助-第3项")
    def usinghelp_3(self):
        "使用帮助-第3项"

        #点击第3项
        self.click_(self.loc_3)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_3)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用帮助-第4项")
    def usinghelp_4(self):
        "使用帮助-第4项"

        #点击第4项
        self.click_(self.loc_4)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_4)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用帮助-第5项")
    def usinghelp_5(self):
        "使用帮助-第5项"

        #点击第5项
        self.click_(self.loc_5)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_5)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用帮助-第6项")
    def usinghelp_6(self):
        "使用帮助-第6项"

        #点击第6项
        self.click_(self.loc_6)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_6)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用帮助-第7项")
    def usinghelp_7(self):
        "使用帮助-第7项"

        #点击第7项
        self.click_(self.loc_7)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_7)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用帮助-第8项")
    def usinghelp_8(self):
        "使用帮助-第8项"

        #点击第8项
        self.click_(self.loc_8)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_8)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用帮助-第9项")
    def usinghelp_9(self):
        "使用帮助-第9项"

        #点击第9项
        self.click_(self.loc_9)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_9)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用帮助-第10项")
    def usinghelp_10(self):
        "使用帮助-第10项"

        #点击第10项
        self.click_(self.loc_10)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_10)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用帮助-第11项")
    def usinghelp_11(self):
        "使用帮助-第11项"

        #点击第11项
        self.click_(self.loc_11)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_11)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用帮助-第12项")
    def usinghelp_12(self):
        "使用帮助-第12项"

        #点击第11项
        self.click_(self.loc_12)

        #休眠5秒,等待页面加载
        sleep(5)

        #判断进入使用帮主页面
        result = self.is_element_Exist(self.loc_12)

        #回退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用手册-VT-10笔")
    def handbook_vt_10(self):
        "使用手册-vt-10笔"

        #点击使用手册
        self.click_(self.loc_shiyongshouce)

        #休眠8秒,等待页面加载
        sleep(8)

        #点击VT-10笔
        self.click_(self.loc_VT_10)

        #休眠3秒,等待页面加载
        sleep(3)

        #判断进入vt-10笔使用手册
        result = self.is_element_Exist(self.loc_shiyongshouce)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用手册-VT-9笔")
    def handbook_vt_9(self):
        "使用手册-vt-9笔"

        #休眠8秒,等待页面加载
        sleep(8)

        #点击使用手册
        self.click_(self.loc_shiyongshouce)

        #点击VT-9笔
        self.click_(self.loc_VT_9)

        #休眠3秒,等待页面加载
        sleep(3)

        #判断进入vt-9笔使用手册
        result = self.is_element_Exist(self.loc_shiyongshouce)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("使用手册-VT-8笔")
    def handbook_vt_8(self):
        "使用手册-vt-8笔"

        #休眠8秒,等待页面加载
        sleep(8)

        #点击使用手册
        self.click_(self.loc_shiyongshouce)

        #点击VT-8笔
        self.click_(self.loc_VT_9)

        #休眠3秒,等待页面加载
        sleep(3)

        #判断进入vt-8笔使用手册
        result = self.is_element_Exist(self.loc_shiyongshouce)

        #回退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("意见反馈-只输入意见")
    def feedback_1(self):
        "意见反馈-只输入意见"

        #点击意见反馈
        self.click_(self.loc_yijianfankui)

        #休眠8秒
        sleep(8)

        #点击意见或建议，聚焦光标
        self.click_(self.loc_shurukuang_yijianhoujianyi)

        #输入“a”
        self.send_Keys(self.loc_shurukuang_yijianhoujianyi, "a")

        #点击联系方式，收回键盘
        self.click_(self.loc_lianxifangsi_shouhuijianpan)

        #点击提交
        self.click_(self.loc_tijiao)

        #休眠3秒
        sleep(3)

        #提交成功后，意见或建议框会清空，我们这里判断“a”不在意见反馈页面中
        result = self.is_element_Exist(self.loc_dy_a)

        return result

    @allure.step("意见反馈-只输入联系方式")
    def feedback_2(self):
        "意见反馈-只输入联系方式"

        #点击联系方式
        self.click_(self.loc_shurukuang_lianxifangsi)

        #输入15927391992
        self.send_Keys(self.loc_shurukuang_lianxifangsi, "15927391992")

        #点击联系方式，收回键盘
        self.click_(self.loc_lianxifangsi_shouhuijianpan)

        #点击提交
        self.click_(self.loc_tijiao)

        #休眠3秒
        sleep(3)

        #提示反馈内容不能为空,判断“反馈内容不能为空”在页面上
        result = self.is_element_Exist(self.loc_dy_15927391993)

        return result

    @allure.step("意见反馈-意见和联系方式都正确输入")
    def feedback_3(self):
        "意见反馈-都正确输入"

        #点击意见或建议
        self.click_(self.loc_shurukuang_yijianhoujianyi)

        #输入200个字
        self.send_Keys(self.loc_shurukuang_yijianhoujianyi, "0.1234568800asdfghkjygfttNCGDEUGFUHGYU!@#$0.1234568800asdfghkjygfttNCGDEUGFUHGYU!@#$0.1234568800asdfghkjygfttNCGDEUGFUHGYU!@#$0.1234568800asdfghkjygfttNCGDEUGFUHGYU!@#$0.1234568800asdfghkjygfttNCGDEUG")

        #点击联系方式，收回键盘
        self.click_(self.loc_lianxifangsi_shouhuijianpan)

        #点击提交
        self.click_(self.loc_tijiao)

        #休眠3秒
        sleep(3)

        #提交成功后，判断联系方式消失
        result = self.is_element_Exist(self.loc_dy_15927391993)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("客服电话")
    def service_tel(self):
        "客服电话"

        #点击客服电话
        self.click_(self.loc_kefudianhua)

        #判断进入拨打电话页面，400 898 9008 和拨号键都出现在页面中
        result_1 = self.is_element_Exist(self.loc_dy_kefudianhua_1)
        result_2 = self.is_element_Exist(self.loc_dy_kefudianhua_2)

        #回退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #回退
        self.driver.press_keycode(4)

        if result_1 and result_2:
            return True
        else:
            return False

    @allure.step("修改密码")
    def change_password(self):
        "修改密码"

        #向上滑半个屏幕
        self.swipeUp()

        #点击修改密码
        self.click_(self.loc_xiugaimima)

        #判断进入修改密码页面，因为要输入验证码，我们这里就只判断是否进入修改密码页面
        result = self.is_element_Exist(self.loc_dy_xiugaimima)

        #回退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("了解智能点读笔")
    def learn_read_pen(self):
        "了解智能点读笔"

        #点击了解智能点读笔
        self.click_(self.loc_liaojiezhinengdiandubi)

        #休眠8秒，等待页面加载完成
        sleep(8)

        #判断是否进入点读笔介绍页面
        result = self.is_element_Exist(self.loc_dy_liaojiezhinengdiandubi)

        #回退
        self.driver.press_keycode(4)

        #点击学习
        self.click_(self.loc_xuexi)

        #休眠5秒
        sleep(5)

        return result
