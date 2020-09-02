import pytest
import allure
from page.bookrack import Bookrack

@allure.feature("书架")
@pytest.mark.run(order=6)
class Test_Bookrack():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = Bookrack(driver)

    @allure.story("搜索")
    def test_search(self):
        """1.进入书架界面， 2.点击搜索输入框， 3.输入b"""
        result =self.wyt.search()
        assert result == True

    @allure.story("搜索-模糊搜索")
    def test_fuzzy_search(self):
        """1.进入书架界面, 2.点击搜索输入框, 3.输入英语"a_Going"""
        result = self.wyt.fuzzy_search()
        assert result == True

    @allure.story("搜索-数字")
    def test_search_number(self):
        """1.进入书架界面, 2.点击搜索输入框, 3.输入数字"""
        result = self.wyt.search_number()
        assert result == True

    @allure.story("搜索-特殊符号")
    def test_search_symbol(self):
        """1.进入书架界面, 2.点击搜索输入框, 3.输入“-”"""
        result = self.wyt.search_symbol()
        assert result == True

    @allure.story("年级选择-幼儿园")
    def test_select_kindergarten(self):
        """1.进入书架页面, 2.进入年级选择框, 3.选择幼儿园"""
        result = self.wyt.select_kindergarten()
        assert result == True

    @allure.story("年级选择-一年级")
    def test_select_first_grade(self):
        """1.进入书架页面, 2.进入年级选择框, 3.选择一年级"""
        result = self.wyt.select_first_grade()
        assert result == True

    @allure.story("年级选择-初三")
    def test_select_junior_three(self):
        """1.进入书架页面, 2.进入年级选择框, 3.选择初三"""
        result = self.wyt.select_junior_three()
        assert result == True

    @allure.story("年级选择-高二")
    def test_select_senior_two(self):
        """1.进入书架页面, 2.进入年级选择框, 3.选择高二"""
        result = self.wyt.select_senior_two()
        assert result == True

    @allure.story("年级选择-全部")
    def test_select_all(self):
        """1.进入书架页面, 2.进入年级选择框, 3.选择全部"""
        result = self.wyt.select_all()
        assert result == True

    @allure.story("书架筛选-支持配音秀")
    def test_select_dubbing_show(self):
        """1.进入书架页面, 2.选择支持配音秀"""
        result = self.wyt.select_dubbing_show()
        assert result == True

    @allure.story("书架筛选-支持口语评测")
    def test_select_evaluating(self):
        """1.进入书架页面, 2.选择支持口语评测"""
        result = self.wyt.select_evaluating()
        assert result == True

    @allure.story("书架筛选-支持音频点播")
    def test_select_audio(self):
        """1.进入书架页面, 2.选择支持音频点播"""
        result = self.wyt.select_audio()
        assert result == True

    @allure.story("课本")
    def test_select_textbook_learning(self):
        """1.进入书架页面, 2.选择课本"""
        result = self.wyt.select_textbook_learning()
        assert result == True

    @allure.story('绘本')
    def test_select_picture_book(self):
        """1.进入书架页面, 2.选择绘本"""
        result = self.wyt.select_picture_book()
        assert result == True

    @allure.story("教辅")
    def test_select_assistants(self):
        """1.进入书架页面, 2.选择教辅"""
        result = self.wyt.select_assistants()
        assert  result == True

    @allure.story("其他")
    def test_select_else(self):
        """1.进入书架页面, 2.选择其他"""
        result = self.wyt.select_else()
        assert result == True

    @allure.story('缓存到笔')
    def test_cache(self):
        """1.点击图片进入该资源，点击缓存到笔"""
        result = self.wyt.cache()
        assert result == True

    @allure.story("推送播放")
    def test_push_to_play(self):
        """1.进入书架页面, 2.点击推送播放"""
        result = self.wyt.push_to_play()
        assert result == True
