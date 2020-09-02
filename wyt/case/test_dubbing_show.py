import pytest
import allure
from page.dubbing_show import Dubbing_Show

@allure.feature("配音秀")
@pytest.mark.run(order=7)
class Test_Dubbing_Show():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = Dubbing_Show(driver)

    @allure.story("目录")
    def test_catalog(self):
        """1.进入书架界面  2.点击一起一下  3.点击目录"""
        result = self.wyt.catalog()
        assert result == True

    @allure.story("角色扮演-中途退出")
    def test_role_play_quit(self):
        """1.进入书架界面， 2.点击一起一下， 3.点击继续配音  4.角色扮演过程中退出"""
        result =self.wyt.role_play_quit()
        assert result == True

    @allure.story("角色扮演")
    def test_role_play(self):
        """1.进入书架界面， 2.点击一起一下， 3.点击继续配音"""
        result =self.wyt.role_play_succeed()
        assert result == True

    @allure.story("分享到朋友圈")
    def test_circle_of_friends(self):
        """1.进入书架界面  2.点击一起一下  3.点击继续配音  4配音完成后分享到朋友圈"""
        result = self.wyt.circle_of_friends()
        assert result == True

    @allure.story("分享到微信好友")
    def test_friend(self):
        """1.进入书架界面  2.点击一起一下  3.点击继续配音  4配音完成后分享到微信好友"""
        result = self.wyt.friend()
        assert result == True

    @allure.story("分享到QQ空间-中途取消")
    def test_QQ_space_cancel(self):
        """1.进入书架界面  2.点击一起一下  3.点击继续配音  4配音完成后分享到QQ空间  5.分享过程中取消"""
        result = self.wyt.QQ_space_cancel()
        assert result == True

    @allure.story("分享到QQ空间")
    def test_QQ_space(self):
        """1.进入书架界面  2.点击一起一下  3.点击继续配音  4配音完成后分享到QQ空间"""
        result = self.wyt.QQ_space()
        assert result == True

    @allure.story("分享到QQ-中途取消")
    def test_QQ_cancel(self):
        """1.进入书架界面  2.点击一起一下  3.点击继续配音  4配音完成后分享到QQ  5.发送过程中取消"""
        result = self.wyt.QQ_cancel()
        assert result == True

    @allure.story("分享到QQ")
    def test_QQ(self):
        """1.进入书架界面  2.点击一起一下  3.点击继续配音  4配音完成后分享到QQ"""
        result = self.wyt.QQ()
        assert result

    @allure.story("保存本地")
    def test_save(self):
        """1.进入书架界面  2.点击一起一下  3.点击继续配音  4配音完成后保存本地"""
        result = self.wyt.save()
        assert result == True

    @allure.story("重新挑战")
    def test_challenge(self):
        """1.进入书架界面  2.点击一起一下  3.点击继续配音  4配音完成后重新挑战"""
        result = self.wyt.challenge()
        assert result == True

    @allure.story("历史配音记录")
    def test_history(self):
        """1.进入书架界面  2.点击一起一下  3.角色扮演"""
        result = self.wyt.history()
        assert result == True

    @allure.story("视频播放和点赞")
    def test_play_and_like(self):
        """1.进入书架界面  2.点击一起一下  3.排行榜中视频播放和点赞"""
        result = self.wyt.play_and_like()
        assert result == True

    @allure.story("排行榜")
    def test_ranking_list(self):
        """1.进入书架界面  2.点击一起一下  3.排行榜"""
        result = self.wyt.ranking_list()
        assert result == True

    @allure.story("看视频")
    def test_watch_video(self):
        """1.进入书架界面  2.点击一起一下  3.点击看视频"""
        result = self.wyt.watch_video()
        assert result == True

    @allure.story("听课文")
    def test_listen_text(self):
        """1.进入书架界面  2.点击一起一下  3.点击听课文"""
        result = self.wyt.listen_text()
        assert result == True
