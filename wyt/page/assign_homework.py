from appium import webdriver
import time
from time import sleep
import os
from common.baseapp import BaseApp

class Assign_Homework():
    """为保证自动化代码能重复执行，作业端能每次都有新的作业，必须先启动外研通园丁APP布置作业"""

    def assign_homework(self):

        #元素定位
        loc_buzhi = ("id", "com.viaton.teacher:id/iv_assign_homework")  #布置
        loc_keqiandaoxue = ("id", "com.viaton.teacher:id/rl_courses_leading_learn")  #课前导学
        loc_daoxuemingcheng = ("id", "com.viaton.teacher:id/et_task_name")  #导学名称
        loc_renwu = ("id", "com.viaton.teacher:id/et_task_info")  #请输入导学任务
        loc_tupian = ("xpath", "//*[@text='图片']")  #图片
        loc_quxiao = ("xpath", "//*[@text='取消']")  #取消
        loc_xuyaoxueshenghuida = ("id", "com.viaton.teacher:id/iv_need_to_be_answered")  #需要学生回答
        loc_jiezhirqi = ("id", "com.viaton.teacher:id/tv_deadline")  #截止日期
        loc_banji = ("id", "com.viaton.teacher:id/tv_classes")  #班级
        loc_buzhizuoye = ("id", "com.viaton.teacher:id/tv_assign_homework")  #布置作业
        loc_dy_zuoyebuzhichenggong = ("id", "com.viaton.teacher:id/tv_success_note")  #作业布置成功
        loc_fanhuishouye = ("id", "com.viaton.teacher:id/tv_back_main")  #布置一个作业后返回首页
        loc_xuexirenwu = ("xpath", "//*[@text='学习任务']")  #学习任务
        loc_kebenxuexi = ("xpath", "//*[@text='课本学习']")  #课本学习
        loc_zuoye1 = ("xpath", "//*[@resource-id='com.viaton.teacher:id/tv_button_info' and @instance='8']")
        loc_zuoye2 = ("xpath", "//*[@resource-id='com.viaton.teacher:id/tv_button_info' and @instance='17']")
        loc_dianjiyulan = ("id", "com.viaton.teacher:id/tv_to_check_homework")  #点击预览
        loc_jiezhishijian_1 = ("xpath", "//*[@text='截止时间']")  #截止日期
        loc_banji_1 = ("xpath", "//*[@text='班级']")  #班级
        loc_liuyan = ("id", "com.viaton.teacher:id/et_remark")  #留言
        loc_tianxiezuoyexinxi = ("id", "com.viaton.teacher:id/tv_title")  #点击填写作业信息，收回键盘
        loc_querenbuzhi = ("id", "com.viaton.teacher:id/tv_confirm_homework")  #确认布置

        desired_leidian = {
            "platformName": "Android",
            "deviceName": "79UDU19918003766",
            "platformVersion": "10",
            "appPackage": "com.viaton.teacher",
            "appActivity": "com.mp.phone.teacher.module.logic.welcome.WelcomeActivity",
            "noReset": True,
            "unicodeKeyboard": True,   # 使用Unicode编码方式发送字符串
            "resetKeyboard": True,    # 隐藏键盘
            # "automationName": "Uiautomator2"
            }

        #启动外研通园丁APP
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_leidian)

        #休眠5秒，等待启动完成
        sleep(5)

        #实例化BaseApp，传入driver参数
        app = BaseApp(driver)

        #布置课前预习

        #点击布置
        app.click_(loc_buzhi)

        #点击课前导学
        app.click_(loc_keqiandaoxue)

        #输入导学名称，并加上时间戳
        app.send_Keys(loc_daoxuemingcheng, "Today's task %s" % time.strftime("  %Y.%m.%d"))

        #点击导学任务，聚集光标
        app.click_(loc_renwu)

        #输入导学任务，并加上时间戳
        app.send_Keys(loc_renwu, "This is today's task %s" % time.strftime("  %Y.%m.%d"))

        #点击图片，用于收回键盘
        app.click_(loc_tupian)

        #点击取消，用于收回键盘
        app.click_(loc_quxiao)

        #点击需要学生回答
        app.click_(loc_xuyaoxueshenghuida)

        #点击截止日期，请选择
        app.click_(loc_jiezhirqi)

        #点击确定
        cmd = "adb shell input tap 993 1759"
        os.system(cmd)

        #休眠5秒
        sleep(5)

        #点击班级，请选择
        app.click_(loc_banji)

        #点击确定
        cmd = "adb shell input tap 993 1759"
        os.system(cmd)

        #休眠5秒
        sleep(5)

        #点击布置作业
        app.click_(loc_buzhizuoye)

        #判断是否布置成功，返回Bool值
        result_1 = app.is_element_Exist(loc_dy_zuoyebuzhichenggong)

        #布置完成作业后，点击返回首页
        app.click_(loc_fanhuishouye)

        #布置作业练习

        #点击布置
        app.click_(loc_buzhi)

        #点击学习任务
        app.click_(loc_xuexirenwu)

        #点击课本学习
        app.click_(loc_kebenxuexi)

        #选中作业1
        app.click_(loc_zuoye1)

        #选中作业2
        app.click_(loc_zuoye2)

        #已选择2道作业，点击预览
        app.click_(loc_dianjiyulan)

        #点击布置作业
        app.click_(loc_buzhizuoye)

        #点击截止日期，请选择
        app.click_(loc_jiezhishijian_1)

        #点击确定
        cmd = "adb shell input tap 993 1759"
        os.system(cmd)

        #休眠5秒
        sleep(5)

        #点击班级，请选择
        app.click_(loc_banji_1)

        #点击确定
        cmd = "adb shell input tap 993 1759"
        os.system(cmd)

        #休眠5秒
        sleep(5)

        #输入留言
        app.send_Keys(loc_liuyan, "Please finish your homework carefully")

        #点击填写作业信息，用来收回键盘
        app.click_(loc_tianxiezuoyexinxi)

        #点击确认布置
        app.click_(loc_querenbuzhi)

        #判断是否布置成功，返回Bool值
        result_2 = app.is_element_Exist(loc_dy_zuoyebuzhichenggong)

        #回退3次，退出外研通园丁APP
        driver.press_keycode(4)
        driver.press_keycode(4)
        driver.press_keycode(4)

        #如果两次作业都布置成功，就返回True
        if result_1 and result_2:
            print("课前预习和作业练习布置成功")
            return True
        else:
            print("课前预习和作业练习布置失败")
            return False
