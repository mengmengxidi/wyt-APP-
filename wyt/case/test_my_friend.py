import pytest
from page.my_friend import My_Friend
import allure

@allure.feature("我的好友")
@pytest.mark.run(order=15)
class Test_My_Friend():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = My_Friend(driver)

    @allure.story("我的好友")
    def test_my_friend(self):
        """1.点击我的  2.点击我的好友"""
        result = self.wyt.my_friend()
        assert result == True

    @allure.story("搜索-注册过的手机号")
    def test_have_registered(self):
        """1.点击我的  2.点击我的好友  3.点击右上角＋  4.搜索注册过的手机号"""
        result = self.wyt.have_register()
        assert result == True

    @allure.story("搜索-注册未过的手机号")
    def test_not_register(self):
        """1.点击我的  2.点击我的好友  3.点击右上角＋  4.搜索未注册过的手机号"""
        result = self.wyt.not_register()
        assert result == True

    @allure.story("搜索-11位不符合手机号段格式的手机号")
    def test_inconformity(self):
        """1.点击我的  2.点击我的好友  3.点击右上角＋  4.搜索11位不符合手机号段格式的手机号"""
        result = self.wyt.inconformity()
        assert result == True

    @allure.story("删除好友-取消")
    def test_delete_cancel(self):
        """1.点击我的  2.点击我的好友  3.点击好友名称  4.点击删除好友  5.点击取消"""
        result = self.wyt.delete_cancel()
        assert result == True

    @allure.story("备注-1位数")
    def test_notes_1(self):
        """1.点击我的  2.点击我的好友  3.点击好友名称  4.点击设置备注  5.输入1位数  6.点击保存"""
        result = self.wyt.notes_1()
        assert result == True

    @allure.story("备注-9位数")
    def test_notes_9(self):
        """1.点击我的  2.点击我的好友  3.点击好友名称  4.点击设置备注  5.输入9位数  6.点击保存"""
        result = self.wyt.notes_9()
        assert result == True

    @allure.story("备注-10位数")
    def test_notes_10(self):
        """1.点击我的  2.点击我的好友  3.点击好友名称  4.点击设置备注  5.输入10位数  6.点击保存"""
        result = self.wyt.notes_10()
        assert result == True

    @allure.story("备注-英文+数字")
    def test_notes_english_numbers(self):
        """1.点击我的  2.点击我的好友  3.点击好友名称  4.点击设置备注  5.输入英文+数字  6.点击保存"""
        result = self.wyt.notes_english_numbers()
        assert result == True

    @allure.story("备注-特殊符号")
    def test_notes_symbol(self):
        """1.点击我的  2.点击我的好友  3.点击好友名称  4.点击设置备注  5.输入特殊符号  6.点击保存"""
        result = self.wyt.notes_symbol()
        assert result == True

    @allure.story("备注-tianyi")
    def test_notes_tianyi(self):
        """1.点击我的  2.点击我的好友  3.点击好友名称  4.点击设置备注  5.输入tianyi  6.点击保存"""
        result = self.wyt.notes_tianyi()
        assert result == True
