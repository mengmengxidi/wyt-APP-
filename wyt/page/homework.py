from common.baseapp import BaseApp
from time import sleep
import os
import allure

class Homework(BaseApp):
    """作业"""

    #元素定位
    loc_zuoye = ("id", "com.viaton.wyt:id/page_homework")  #作业
    loc_keqianyuxi = ("xpath", "//*[@text='课前预习']")  #课前预习
    loc_1 = ("xpath", "//*[@text='进行中' and @instance='6']")
    loc_huidalaoshiwenti = ("id", "com.viaton.wyt:id/et_text")  #回答老师问题
    loc_wodezuoye = ("xpath", "//*[@text='我的作业']")  #我的作业
    loc_shangchuan_tupian = ("id", "com.viaton.wyt:id/iv_picture")  #上传图片
    loc_xiangji = ("xpath", "//*[@text='相机']")  #相机
    loc_paizhao = ('xpath', "//*[@class='android.widget.LinearLayout' and @instance='5']")  #拍照
    loc_gouxuan = ("id", "com.huawei.camera:id/done_button")  #勾选
    loc_luyin = ('id', "com.viaton.wyt:id/iv_audio")  #录音
    loc_dianji_luyin = ("id", "com.viaton.wyt:id/iv_action")  #点击录音
    loc_shangchuan_luyin = ("id", "com.viaton.wyt:id/tv_upload")  #上传录音
    loc_shipin = ("id", "com.viaton.wyt:id/iv_video")  #视频
    loc_shipinku = ("id", "com.viaton.wyt:id/tv_content")  #视频库
    loc_diyigeshipin = ("xpath", "//*[@resource-id='com.android.documentsui:id/item_root' and @instance='7']")  #第一个视频
    loc_tijiaozuoye = ("id", "com.viaton.wyt:id/submit")  #提交作业
    loc_dy_qiankeyuxi = ("id", "com.viaton.wyt:id/collapsing_toolbar_layout")  #断言课前预习
    loc_zuoyelianxi = ("xpath", "//*[@text='作业练习']")  #作业练习
    loc_2 = ("xpath", "//*[@text='进行中' and @instance='5']")
    loc_quedin_tijiao = ("id", "com.viaton.wyt:id/tv_confirm")  #确定提交
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习
    loc_xuexijilu = ("xpath", "//*[@text='学习记录']")  #学习记录

    @allure.step("课前预习")
    def preview_before_class(self):
        "课前预习"

        #点击作业
        self.click_(self.loc_zuoye)

        #已在教师端布置完作业，我们这里选择第一个作业就是最新的作业
        self.click_(self.loc_1)

        #点击回到老师问题或者给老师留言，聚集光标
        self.click_(self.loc_huidalaoshiwenti)

        #输入Teacher, I have finished my homework
        self.send_Keys(self.loc_huidalaoshiwenti, "Teacher, I have finished my homework")

        #点击我的作业，用来收回键盘
        self.click_(self.loc_wodezuoye)

        #点击图片
        self.click_(self.loc_shangchuan_tupian)

        #点击相机
        self.click_(self.loc_xiangji)

        #点击拍照键
        self.click_(self.loc_paizhao)

        #选择“√”
        self.click_(self.loc_gouxuan)

        #点击录音键
        self.click_(self.loc_luyin)

        #点击开始录音
        self.click_(self.loc_dianji_luyin)

        #录音10秒
        sleep(10)

        #点击暂停录音
        self.click_(self.loc_dianji_luyin)

        #点击上传
        self.click_(self.loc_shangchuan_luyin)

        #点击视频按钮
        self.click_(self.loc_shipin)

        #点击视频库
        self.click_(self.loc_shipinku)

        #选择第一个视频
        self.click_(self.loc_diyigeshipin)

        #向上滑一个屏幕
        self.swipeUp()

        #点击提交作业
        self.click_(self.loc_tijiaozuoye)

        #提交有点慢，休眠10秒，等待提交完成
        sleep(10)

        #判断是否回到课前预习页面，返回Bool
        result = self.is_element_Exist(self.loc_dy_qiankeyuxi)

        return result

    @allure.step("作业练习")
    def operation_practice(self):
        "作业练习"

        #点击作业练习
        self.click_(self.loc_zuoyelianxi)

        #已在教师端布置完作业，我们这里选择第一个作业就是最新的作业
        self.click_(self.loc_2)

        #向上滑动半个屏幕
        self.swipeUp()

        #点击提交作业
        self.click_(self.loc_tijiaozuoye)

        #自动化代码运行中，再去人工点击课本完成作业，就不是自动化了，所以这里我们不完成作业，点击确认提交
        self.click_(self.loc_quedin_tijiao)

        #判断是否回到课前预习页面，返回Bool
        result = self.is_element_Exist(self.loc_zuoye)

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        #点击学习记录，保准每个用例集的起点一致
        self.click_(self.loc_xuexijilu)

        #休眠5秒
        sleep(5)

        return result
