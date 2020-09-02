import pytest
import allure
from page.dropdown import Dropdown

@allure.feature("预览、下载、新手引导")
@pytest.mark.run(order=8)
class Test_Dropdown():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = Dropdown(driver)

    @allure.story("预览")
    def test_preview(self):
        """1.进入书架界面， 2.选择一起一下课本， 3.点击右上角下拉按钮  4.点击预览"""
        result =self.wyt.preview()
        assert result == True

    # @allure.story("微信朋友圈")
    # def test_friend(self):
    #     """1.进入书架界面， 2.选择一起一下课本， 3.点击右上角下拉按钮  4.点击预览 5.点击分享 6.选择微信朋友圈"""
    #     result = self.wyt.friend()
    #     assert result == True
    #
    # @allure.story("微信")
    # def test_wechat(self):
    #     """1.进入书架界面， 2.选择一起一下课本， 3.点击右上角下拉按钮  4.点击预览 5.点击分享 6.选择微信"""
    #     result = self.wyt.wechat()
    #     assert result == True
    #
    # @allure.story("取消分享")
    # def test_cancel(self):
    #     """1.进入书架界面， 2.选择一起一下课本， 3.点击右上角下拉按钮  4.点击预览 5.点击分享 6.点击取消分享"""
    #     result = self.wyt.cancel()
    #     assert result == True

    @allure.story("继续配音")
    def test_continue_voice(self):
        """1.进入书架界面， 2.选择一起一下课本， 3.点击右上角下拉按钮  4.点击预览 5.继续配音"""
        result = self.wyt.continue_voice()
        assert result == False

    @allure.story("下载")
    def test_download(self):
        """1.进入书架界面， 2.选择一起一下课本， 3.点击右上角下拉按钮  4.点击下载"""
        result = self.wyt.download()
        assert result == True

    @allure.story("新手引导")
    def test_guidance(self):
        """1.进入书架界面， 2.选择一起一下课本， 3.点击右上角下拉按钮  4.点击新手引导"""
        result = self.wyt.guidance()
        assert result == True
