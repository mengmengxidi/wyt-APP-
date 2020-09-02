import pytest
import allure
from page.my_medal import My_Medal

@allure.feature("我的勋章")
@pytest.mark.run(order=10)
class Test_My_Medal():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = My_Medal(driver)

    @allure.story("我的勋章显示")
    def test_display(self):
        """1、进入我的界面  2、进入我的勋章"""
        result = self.wyt.display()
        assert result == True

    @allure.story("卸下勋章")
    def test_unload_medal(self):
        """1、进入我的界面；2、点击卸下；3、返回我的界面。"""
        result =self.wyt.unload_medal()
        assert result == True

    @allure.story("佩戴勋章")
    def test_wear_medal(self):
        """1、进入我的界面；2、选择一个勋章，点击佩戴；3、返回我的界面。"""
        result = self.wyt.wear_medal()
        assert result == True

    @allure.story("分享炫耀")
    def test_flaunt(self):
        """1、进入我的界面；2、选择一个勋章，点击佩戴；3、点击分享炫耀一下"""
        result = self.wyt.flaunt()
        assert result == True

    @allure.story("分享到微信")
    def test_wechat(self):
        """1、进入我的界面；2、选择一个勋章，点击佩戴；3、点击分享炫耀一下  4、点击分享到微信"""
        result = self.wyt.wechat()
        assert result == True

    @allure.story("分享到微信朋友圈")
    def test_friend(self):
        """1、进入我的界面；2、选择一个勋章，点击佩戴；3、点击分享炫耀一下  4、点击分享到微信朋友圈"""
        result = self.wyt.friend()
        assert result == True

    @allure.story("分享到QQ-中途取消")
    def test_QQ_cancel(self):
        """1、进入我的界面；2、选择一个勋章，点击佩戴；3、点击分享炫耀一下  4、点击分享到QQ  5、中途取消"""
        result = self.wyt.QQ_cancel()
        assert result == True

    @allure.story("分享到QQ-成功")
    def test_QQ(self):
        """1、进入我的界面；2、选择一个勋章，点击佩戴；3、点击分享炫耀一下  4、点击分享到QQ  5、分享成功"""
        result = self.wyt.QQ()
        assert result == True

    @allure.story("分享到QQ空间-中途取消")
    def test_QQ_interspace_cancel(self):
        """1、进入我的界面；2、选择一个勋章，点击佩戴；3、点击分享炫耀一下  4、点击分享到QQ空间  5、中途取消"""
        result = self.wyt.QQ_interspace_cancel()
        assert result == True

    @allure.story("分享到QQ空间-成功")
    def test_QQ_interspace_succeed(self):
        """1、进入我的界面；2、选择一个勋章，点击佩戴；3、点击分享炫耀一下  4、点击分享到QQ空间  5、发布成功"""
        result = self.wyt.QQ_interspace_succeed()
        assert result == True

    @allure.story("分享-取消分享")
    def test_cancel(self):
        """1、进入我的界面；2、选择一个勋章，点击佩戴；3、点击分享炫耀一下  4、点击分享  5、点击取消分享"""
        result = self.wyt.cancel()
        assert result == True