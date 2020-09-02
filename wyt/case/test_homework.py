import pytest
import allure
from page.homework import Homework

@allure.feature("作业")
@pytest.mark.run(order=5)
class Test_Homework():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = Homework(driver)

    @allure.story("课前预习")
    def test_picture_shows(self):
        """1.点击作业, 2.点击课前预习, 3.完成作业"""
        result =self.wyt.preview_before_class()
        assert result == True

    @allure.story("作业练习")
    def test_operation_practice(self):
        """1.点击作业, 2.点击作业练习, 3.完成作业"""
        result = self.wyt.operation_practice()
        assert result == True