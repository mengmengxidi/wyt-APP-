from common.baseapp import BaseApp
from time import sleep
import os
import allure

class Dropdown(BaseApp):
    """预览、下载、新手引导"""

    #元素定位
    loc_shujia = ("xpath", "//*[@text='书架' and @resource-id='com.viaton.wyt:id/page_bookshelf']")  #书架
    loc_jixupeiyin = ("xpath", "//*[@instance='8' and @resource-id='com.viaton.wyt:id/tv_dubbing']")  #继续学习
    loc_shezhi_5 = ("id", "com.viaton.wyt:id/tv_settings")  #设置
    loc_xiala_yulan = ("id", "com.viaton.wyt:id/tv_preview")  #预览
    loc_xiala_xiazai = ("id", "com.viaton.wyt:id/tv_down_note")  #下载
    loc_xiala_xinshouyindao = ("id", "com.viaton.wyt:id/tv_guide")  #新手引导
    loc_dy_yulan = ("xpath", "//*[@text='继续配音']")  #判断点击预览后有继续配音字样
    loc_fenxianganniu = ("id", "com.viaton.wyt:id/iv_right_icon")  #分享按钮
    loc_weixinpengyouquan = ("xpath", "//*[@text='微信朋友圈']")  #微信朋友圈
    loc_weixin = ("xpath", "//*[@text='微信']")  #微信
    loc_quxiaofeniang = ("xpath", "//*[@text='取消分享']")  #取消分享
    loc_jixupeiyin_yulan = ("id", "com.viaton.wyt:id/tv_restart")  #继续配音—预览页面中
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习
    loc_xuexijilu = ("xpath", "//*[@text='学习记录']")  #学习记录

    @allure.step("书架-搜索")
    def preview(self):
        "书架-搜索"

        #点击书架
        self.click_(self.loc_shujia)

        #点击继续配音
        self.click_(self.loc_jixupeiyin)

        #点击设置
        self.click_(self.loc_shezhi_5)

        #点击预览
        self.click_(self.loc_xiala_yulan)

        #点击预览后，判断继续配音字样是否正确显示
        result = self.is_element_Exist(self.loc_dy_yulan)

        return result

    # @allure.step("微信朋友圈")
    # def friend(self):
    #     "微信朋友圈"
    #
    #     #点击分享按钮
    #     self.click_(self.loc_fenxianganniu)
    #
    #     #点击微信朋友圈
    #     self.click_(self.loc_weixinpengyouquan)
    #
    #     #这里只能分享给微信朋友圈，前面我们需要验证 1、手机安装应用（QQ） 2、手机没有安装（微信）
    #     #这里安装微信的话，就无法验证前面分享时手机没有安装应用这种场景，所以这里只验证手机没有安装
    #     result = self.is_element_Exist(self.loc_fenxianganniu)
    #
    #     return result
    #
    # @allure.step("微信")
    # def wechat(self):
    #     "微信"
    #
    #     #点击分享按钮
    #     self.click_(self.loc_fenxianganniu)
    #
    #     #点击微信
    #     self.click_(self.loc_weixin)
    #
    #     #判断分享失败后在预览页面
    #     result = self.is_element_Exist(self.loc_fenxianganniu)
    #
    #     return result
    #
    # @allure.step("取消分享")
    # def cancel(self):
    #     "取消分享"
    #
    #     #点击分享按钮
    #     self.click_(self.loc_fenxianganniu)
    #
    #     #取消分享
    #     self.click_(self.loc_quxiaofeniang)
    #
    #     #判断分享失败后在预览页面
    #     result = self.is_element_Exist(self.loc_fenxianganniu)
    #
    #     return result

    @allure.step("继续配音")
    def continue_voice(self):
        "继续配音"

        #点击继续配音
        self.click_(self.loc_jixupeiyin_yulan)

        #判断继续配音字样消失
        result = self.is_element_Exist(self.loc_dy_yulan)

        return result

    @allure.step("下载")
    def download(self):
        "下载"

        #点击设置
        self.click_(self.loc_shezhi_5)

        #等待3秒
        sleep(3)

        #点击下载
        self.click_(self.loc_xiala_xiazai)

        #等待5秒
        sleep(5)

        #回退
        self.driver.press_keycode(4)

        #判断设置是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_shezhi_5)

        return result

    @allure.step("新手引导")
    def guidance(self):
        "新手引导"

        #点击设置
        self.click_(self.loc_shezhi_5)

        #点击新手引导
        self.click_(self.loc_xiala_xinshouyindao)

        #休眠20秒，等待页面完全加载
        sleep(20)

        #回退
        self.driver.press_keycode(4)

        #判断点读页面是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_shezhi_5)

        #等待2秒
        sleep(2)

        #回退
        self.driver.press_keycode(4)

        #刷新页面
        self.swipeDown()

        #休眠2秒
        sleep(2)

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        #点击学习记录，保准每个用例集的起点一致
        self.click_(self.loc_xuexijilu)

        #休眠5秒
        sleep(5)

        return result
