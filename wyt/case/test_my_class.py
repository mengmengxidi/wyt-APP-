import pytest
from page.my_class import My_Class
import allure

@allure.feature("我的班级")
@pytest.mark.run(order=16)
class Test_My_Class():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = My_Class(driver)

    @allure.story("我的班级")
    def test_my_class(self):
        """1.点击我的  2.点击我的班级"""
        result = self.wyt.my_class()
        assert result == True

    @allure.story("退出班级-取消")
    def test_out_class_cancel(self):
        """1.点击我的  2.点击我的班级  3.点击退出  4.点击取消"""
        result = self.wyt.out_class_cancel()
        assert result == True

    @allure.story("退出班级-成功")
    def test_out_class(self):
        """1.点击我的  2.点击我的班级  3.点击退出"""
        result = self.wyt.out_class()
        assert result == True

    @allure.story("重新编辑-取消")
    def test_reedit_cancel(self):
        """1.点击我的  2.点击我的班级  3.点击取消"""
        result = self.wyt.reedit_cancel()
        assert result == True

    @allure.story("重新编辑")
    def test_reedit(self):
        """1.点击我的  2.点击我的班级  3.点击重新编辑"""
        result = self.wyt.reedit()
        assert result == True

    @allure.story("编辑班级信息-学校输入1位数")
    def test_class_info_1(self):
        """1.点击我的  2.点击我的班级  3.点击重新编辑  4.学校输入1位数，其他正确输入  5.点击确定"""
        result = self.wyt.class_info_1()
        assert result == True

    @allure.story("编辑班级信息-学校输入20位数")
    def test_class_info_20(self):
        """1.点击我的  2.点击我的班级  3.点击重新编辑  4.学校输入20位数，其他正确输入  5.点击确定"""
        result = self.wyt.class_info_20()
        assert result == True

    @allure.story("编辑班级信息-学校输入jianghan_school")
    def test_class_info_jianghan_school(self):
        """1.点击我的  2.点击我的班级  3.点击重新编辑  4.学校输入jianghan_school，其他正确输入  5.点击确定"""
        result = self.wyt.class_info_jianghan_school()
        assert result == True

    @allure.story("编辑班级信息-输入错误的班级邀请码")
    def test_invitation_code_inexistence(self):
        """1.点击我的  2.点击我的班级  3.点击重新编辑  4.输入不存在的邀请码，其他正确输入  5.点击确定"""
        result = self.wyt.invitation_code_inexistence()
        assert result == True

    @allure.story("编辑班级信息-输入正确班级邀请码")
    def test_invitation_code(self):
        """1.点击我的  2.点击我的班级  3.点击重新编辑  4.输入正确的邀请码，其他正确输入  5.点击确定"""
        result = self.wyt.invitation_code()
        assert result == True
