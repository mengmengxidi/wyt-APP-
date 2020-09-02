import pytest
import allure
from page.my_info_settings import My_Info_Settings

@allure.feature("我的信息设置")
@pytest.mark.run(order=9)
class Test_My_Info_Settings():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = My_Info_Settings(driver)

    @allure.story("头像-从手机相册选择-中途取消")
    def test_cellphone_cancel(self):
        """1、进入我的-我的信息设置； 2、点击头像，选择从相册选择；3、选择相册中的图片；4、点击取消"""
        result =self.wyt.cellphone_cancel()
        assert result == True

    @allure.story("头像-从手机相册选择")
    def test_cellphone(self):
        """1、进入我的-我的信息设置； 2、点击头像，选择从相册选择；3、选择相册中的图片；4、点击完成"""
        result = self.wyt.cellphone()
        assert result == True

    @allure.story("头像-取消")
    def test_cancel(self):
        """1、进入我的-我的信息设置； 2、点击头像； 3、点击取消"""
        result = self.wyt.cancel()
        assert result == True

    @allure.story("昵称-输入10个字")
    def test_nickname_10(self):
        """1、进入我的界面； 2、点击显示的昵称，进入到编辑—昵称修改； 3、按规定输入10个字，其他正确输入，点击保存"""
        result = self.wyt.nickname_10()
        assert result == True

    @allure.story("昵称-输入11个字")
    def test_nickname_11(self):
        """1、进入我的界面；2、点击显示的昵称，进入到编辑—昵称修改；3、按规定输入11个字符，其他正确输入，点击保存"""
        result = self.wyt.nickname_11()
        assert result == True

    @allure.story("昵称-不输入")
    def test_nickname_not_enter(self):
        """1、进入我的界面；2、点击显示的昵称，进入到编辑—昵称修改；3、不输入，直接点击保存"""
        result = self.wyt.nickname_not_enter()
        assert result == True

    @allure.story("昵称-输入特殊符号")
    def test_nickname_symbol(self):
        """1、进入我的界面；2、点击显示的昵称，进入到编辑—昵称修改；3、输入特殊字符，点击保存"""
        result = self.wyt.nickname_symbol()
        assert result == True

    @allure.story("昵称-输入159")
    def test_nickname_159(self):
        """1、进入我的界面；2、点击显示的昵称，进入到编辑—昵称修改；3、输入159，点击保存"""
        result = self.wyt.nickname_159()
        assert result == True

    @allure.story("昵称-取消")
    def test_nickname_cancel(self):
        """1、进入我的界面；2、点击显示的昵称，进入到编辑—昵称修改；3、点击取消"""
        result = self.wyt.nickname_cancel()
        assert result == True

    @allure.story("年龄-1")
    def test_age_1(self):
        """1、进入我的界面；2、点击年龄字段；3、输入1，点击保存"""
        result = self.wyt.age_1()
        assert result == True

    @allure.story("年龄-0")
    def test_age_0(self):
        """1、进入我的界面；2、点击年龄字段；3、输入0，点击保存"""
        result = self.wyt.age_0()
        assert result == True

    @allure.story("年龄-99")
    def test_age_99(self):
        """1、进入我的界面；2、点击年龄字段；3、输入99，点击保存"""
        result = self.wyt.age_99()
        assert result == True

    @allure.story("年龄-18")
    def test_age_18(self):
        """1、进入我的界面；2、点击年龄字段；3、输入18，点击保存"""
        result = self.wyt.age_18()
        assert result == True

    @allure.story("年龄-不输入")
    def test_age_not_enter(self):
        """1、进入我的界面；2、点击年龄字段；3、不输入，直接点击保存"""
        result = self.wyt.age_not_enter()
        assert result == True

    @allure.story("年龄-取消")
    def test_age_cancel(self):
        """1、进入我的界面；2、点击年龄字段；3、点击取消"""
        result = self.wyt.age_cancel()
        assert result == True

    @allure.story("性别-男")
    def test_man(self):
        """1、进入我的界面；2、点击性别字段；3、选择男"""
        result = self.wyt.man()
        assert result == True

    @allure.story("性别-女")
    def test_woman(self):
        """1、进入我的界面；2、点击性别字段；3、选择女"""
        result = self.wyt.woman()
        assert result == True

    @allure.story("性别-取消")
    def test_gender_cancel(self):
        """1、进入我的界面；2、点击性别字段；3、点击取消"""
        result = self.wyt.gender_cancel()
        assert result == True

    @allure.story("年级-不选择")
    def test_uncheck(self):
        """1、进入我的信息设置；2、点击年级输入框；3、不选择年级，直接点点击确定"""
        result = self.wyt.uncheck()
        assert result == True

    @allure.story("年级-幼儿园小班")
    def test_primary_class(self):
        """1、进入我的信息设置；2、点击年级输入框；3、选择幼儿园小班 4、点击确定"""
        result = self.wyt.primary_class()
        assert result == True

    @allure.story("年级-大学四年级")
    def test_senior(self):
        """1、进入我的信息设置；2、点击年级输入框；3、选择大学四年级 4、点击确定"""
        result = self.wyt.senior()
        assert result == True

    @allure.story("=年级-小学五年级")
    def test_fifth_grade(self):
        """1、进入我的信息设置；2、点击年级输入框；3、选择小学五年级 4、点击确定"""
        result = self.wyt.fifth_grade()
        assert result == True
