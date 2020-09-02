import pytest
import allure
from page.ranking_list import Ranking_List

@allure.feature("学习-学习排行榜")
@pytest.mark.run(order=3)
class Test_Learning_Record():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = Ranking_List(driver)

    @allure.story("Day")
    def test_day(self):
        """1.进入学习, 2.点击学习排行榜, 3.点击Day"""
        result =self.wyt.day()
        assert result == True

    @allure.story("Week")
    def test_week(self):
        """1.进入学习, 2.点击学习排行榜, 3.点击Week"""
        result =self.wyt.week()
        assert result == True

    @allure.story("Month")
    def test_month(self):
        """1.进入学习, 2.点击学习排行榜, 3.点击Month"""
        result =self.wyt.month()
        assert result == True
