import pytest
import allure
from page.vip import Vip

@allure.feature("配音秀会员")
@pytest.mark.run(order=12)
class Test_Vip():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = Vip(driver)

    @allure.story("配音秀会员显示")
    def test_display(self):
        """1、进入我的界面  2、进入配音秀会员"""
        result = self.wyt.display()
        assert result == True

    @allure.story("交易记录")
    def test_record(self):
        """1、进入我的界面  2、进入配音秀会员  3、点击交易记录"""
        result = self.wyt.record()
        assert result == True

    @allure.story("支付宝-12个月")
    def test_alipay_12(self):
        """1、进入我的界面  2、进入配音秀会员  3、选择12个月  4、点击支付宝  5、点击立即续费"""
        result = self.wyt.alipay_12()
        assert result == True

    @allure.story("支付宝-36个月")
    def test_alipay_36(self):
        """1、进入我的界面  2、进入配音秀会员  3、选择36个月  4、点击支付宝  5、点击立即续费"""
        result = self.wyt.alipay_36()
        assert result == True

    @allure.story("微信-12个月")
    def test_wechat_12(self):
        """1、进入我的界面  2、进入配音秀会员  3、选择36个月  4、点击支微信  5、点击立即续费"""
        result = self.wyt.wechat_12()
        assert result == True

    @allure.story("微信-36个月")
    def test_wechat_36(self):
        """1、进入我的界面  2、进入配音秀会员  3、选择36个月  4、点击微信  5、点击立即续费"""
        result = self.wyt.wechat_36()
        assert result == True
