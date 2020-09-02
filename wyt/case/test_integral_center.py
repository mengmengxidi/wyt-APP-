import pytest
import allure
from page.integral_center import Integral_Center

@allure.feature("积分中心")
@pytest.mark.run(order=11)
class Test_Integral_Center():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = Integral_Center(driver)

    @allure.story("积分中心显示")
    def test_display(self):
        """1、进入我的界面  2、进入积分中心"""
        result = self.wyt.display()
        assert result == True

    @allure.story("赚积分")
    def test_gain(self):
        """1、进入我的界面  2、进入积分中心  3、点击赚积分"""
        result = self.wyt.gain()
        assert result == True

    @allure.story("积分记录")
    def test_record(self):
        """1、进入我的界面  2、进入积分中心  3、点击积分记录"""
        result = self.wyt.record()
        assert result == True