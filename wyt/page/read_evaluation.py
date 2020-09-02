from common.baseapp import BaseApp
from time import sleep
import os
import allure

class Read_Evaluation(BaseApp):
    """学习-阅读评测"""

    #元素定位
    loc_yuedupingce = ("xpath", "//*[@text='阅读评测']")  #阅读评测
    loc_dy_wodedengji = ("xpath", "//*[contains(@text, '我的等级')]")  #断言我的等级
    loc_dy_chengzhangguiji = ("xpath", "//*[@text='查看成长轨迹']")  #断言查看成长轨迹
    loc_dy_wonengyuejijiduwu = ("xpath", "//*[contains(@text, '我能阅读')]")  #断言我能阅读几级读物
    loc_dy_wohuiganxingqudeshu = ("xpath", "//*[@text='我会感兴趣的书']")  #断言我会感兴趣的书
    loc_zaiceyici = ("xpath", "//*[@text='再测一次']")  #再测一次
    loc_dy_keyong12ci = ("id", "com.viaton.wyt:id/tv_residue_degree_num")  #可用12次
    loc_kaishiceshi = ("id", "com.viaton.wyt:id/tv_start_test")  #开始测试
    loc_dy_queding_kaishiceshi = ("xpath", "//*[@text='确定']")  #确定
    loc_quxiao = ("xpath", "//*[@text='取消']")  #取消
    loc_moniceshi = ("id", "com.viaton.wyt:id/iv_mock_test_icon")  #模拟测试
    loc_A = ("id", "com.viaton.wyt:id/tv_circle_A")  #选A
    loc_xiayiti = ("id", "com.viaton.wyt:id/tv_next")  #下一题
    loc_3_1 = ("xpath", "//*[@text='We like to ride.']")
    loc_3_2 = ("xpath", "//*[@text='We like to jump.']")
    loc_3_3 = ("xpath", "//*[@text='We like to swim.']")
    loc_3_dui_1 = ("xpath", "//*[@class='android.widget.ImageView' and @instance='1']")
    loc_3_dui_2 = ("xpath", "//*[@class='android.widget.ImageView' and @instance='2']")
    loc_3_dui_3 = ("xpath", "//*[@class='android.widget.ImageView' and @instance='3']")
    loc_goumaicishu = ("id", "com.viaton.wyt:id/iv_test_num_icon")  #购买次数
    loc_jilu = ("id", "com.viaton.wyt:id/tv_right")  #记录
    loc_dy_goumaijilu = ("xpath", "//*[@text='购买记录']")  #购买记录
    loc_fuwuxieyi = ("id", "com.viaton.wyt:id/tv_user_deal")  #服务协议
    loc_dy_fuwuxieyi = ("id", "com.viaton.wyt:id/tv_title")  #断言用户协议
    loc_yinsitiaokuan = ("id", "com.viaton.wyt:id/tv_privacy_policy")  #隐私条款
    loc_dy_yinsitiaokuan = ("id", "com.viaton.wyt:id/tv_title")  #断言隐私条款
    loc_lijigoumai = ("id", "com.viaton.wyt:id/tv_immediately_buy")  #立即购买
    loc_querenzhifu = ("id", "com.viaton.wyt:id/tv_confirm_pay")  #确认支付
    loc_dy_zhifubao = ("xpath", "//*[@text='支 支付宝付款']")  #断言支付宝付款
    loc_weixinzhifu = ("id", "com.viaton.wyt:id/iv_choose_wx")  #微信支付
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习
    loc_xuexijilu = ("xpath", "//*[@text='学习记录']")  #学习记录
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的

    @allure.step("阅读评测-我的等级")
    def grade(self):
        "阅读评测-我的等级"

        #休眠5秒
        sleep(5)

        #点击学习
        self.click_(self.loc_xuexi)

        #点击阅读评测
        self.click_(self.loc_yuedupingce)

        #判断阅读评测页面是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_wodedengji)

        return result

    @allure.step("阅读评测-查看成长轨迹")
    def growth_process(self):
        "阅读评测-查看成长轨迹"

        #判断查看成长轨迹是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_chengzhangguiji)

        return result

    @allure.step("阅读评测-我能阅读几级读物")
    def read(self):
        "阅读评测-我能阅读几级读物"

        #判断我能阅读几级读物是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_wonengyuejijiduwu)

        return result

    @allure.step("阅读评测-可用次数")
    def usable_number(self):
        "阅读评测-可用次数"

        #休眠2秒
        sleep(2)

        #点击我的
        self.click_(self.loc_wode)

        #休眠10秒
        sleep(10)

        #点击学习
        self.click_(self.loc_xuexi)

        #点击再测一次
        self.click_(self.loc_zaiceyici)

        #判断可用次数是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_keyong12ci)

        return result

    @allure.step("阅读评测-开始评测")
    def review_began(self):
        "阅读评测-开始评测"

        #点击开始评测
        self.click_(self.loc_kaishiceshi)

        #因为评测题目每次出题的顺序不一样，很难进行阅读评测，而且可用次数只有12次，代码跑12次后就需要购买了
        #所以这里断言提示框是否出现
        result = self.is_element_Exist(self.loc_dy_queding_kaishiceshi)

        #点击取消
        self.click_(self.loc_quxiao)

        return result

    @allure.step("阅读评测-模拟测试")
    def simulation(self):
        "阅读评测-模拟测试"

        #向上滑半个屏幕
        self.swipeUp()

        #点击模拟测试
        self.click_(self.loc_moniceshi)

        #模拟测试-第1题：

        #休眠3秒
        sleep(3)

        #向上滑动半个屏幕
        self.swipeUp()

        #选择A选项
        self.click_(self.loc_A)

        #点击下一题
        self.click_(self.loc_xiayiti)

        #休眠3秒，等待第2题加载完成
        sleep(3)

        #模拟测试-第2题：

        #向上花半个屏幕
        self.swipeUp()

        #选择A选项
        self.click_(self.loc_A)

        #点击下一题
        self.click_(self.loc_xiayiti)

        #休眠3秒，等待第3题加载完成
        sleep(3)

        #模拟测试-第3题：

        #选中左遍第一个选项
        self.click_(self.loc_3_1)

        #选中右边第一个选项
        self.click_(self.loc_3_dui_1)

        #选中左边第二个选项
        self.click_(self.loc_3_2)

        #选中右边第二个选项
        self.click_(self.loc_3_dui_2)

        #选中左边第三个选项
        self.click_(self.loc_3_3)

        #选中右边第三个选项
        self.click_(self.loc_3_dui_3)

        #点击下一题
        self.click_(self.loc_xiayiti)

        #休眠3秒，等待第4题加载完成
        sleep(3)

        #向上滑动半个屏幕
        self.swipeUp()

        #选择A选项
        self.click_(self.loc_A)

        #点击下一题
        self.click_(self.loc_xiayiti)

        #作业完成后，后退
        self.driver.press_keycode(4)

        #判断是否回到阅读评测页面，返回Bool
        result = self.is_element_Exist(self.loc_kaishiceshi)

        return result

    @allure.step("阅读评测-记录")
    def record(self):
        "阅读评测-记录"

        #点击购买次数
        self.click_(self.loc_goumaicishu)

        #点击记录
        self.click_(self.loc_jilu)

        #判断购买记录页面是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_goumaijilu)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("服务协议")
    def agreement(self):
        "服务协议"

        #点击服务协议
        self.click_(self.loc_fuwuxieyi)

        #判断用户协议页面是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_fuwuxieyi)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("隐私条款")
    def privacy_policy(self):
        "隐私条款"

        #点击隐私条款
        self.click_(self.loc_yinsitiaokuan)

        #判断隐私条款页面是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_yinsitiaokuan)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("支付宝支付")
    def alipay(self):
        "支付宝支付"

        #点击立即购买
        self.click_(self.loc_lijigoumai)

        #点击确认支付
        self.click_(self.loc_querenzhifu)

        #此处加载较慢，休眠10秒，等待页面加载
        sleep(10)

        #判断跳转到支付宝付款页面
        result = self.is_element_Exist(self.loc_dy_zhifubao)

        #回退，因为未安装支付宝，提示“支付失败”
        self.driver.press_keycode(4)

        return result

    @allure.step("微信支付")
    def wechat(self):
        "微信支付"

        #点击立即支付
        self.click_(self.loc_lijigoumai)

        #选中微信支付
        self.click_(self.loc_weixinzhifu)

        #点击确认支付
        self.click_(self.loc_querenzhifu)

        #因为未安装微信，会提示“你没有安装微信”，我们这里判断是否跳到立即购买页面
        result = self.is_element_Exist(self.loc_lijigoumai)

        #回退
        self.driver.press_keycode(4)

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        #点击学习记录，保准每个用例集的起点一致
        self.click_(self.loc_xuexijilu)

        #休眠5秒
        sleep(5)

        return result
