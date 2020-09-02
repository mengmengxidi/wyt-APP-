import pytest
import allure
from page.learning_record import Learning_Record

@allure.feature("学习-学习记录")
@pytest.mark.run(order=2)
class Test_Learning_Record():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = Learning_Record(driver)

    @allure.story("头像显示")
    def test_picture_shows(self):
        """1.我的界面修改头像, 2.修改成功后 ,3. 进入学习"""
        result =self.wyt.picture_shows()
        assert result == True

    @allure.story("名称显示")
    def test_display_name(self):
        """1.我的界面修改昵称, 2.修改成功后, 3.进入学习"""
        resule = self.wyt.display_name()
        assert resule == True

    @allure.story("学习打卡时长")
    def test_learning_to_clock_in(self):
        """1.登录APP, 2.进入学习, 3.学习打卡显示"""
        result = self.wyt.learning_to_clock_in()
        assert result == True

    @allure.story("行动力占比值")
    def test_action_force_ratio(self):
        """1.登录APP, 2.进入学习, 3.行动力占比值"""
        result = self.wyt.action_force_ratio()
        assert result == True

    @allure.story("累计学习")
    def test_cumulative_learning(self):
        """1.登录APP, 2.进入学习, 3.累计学习天数"""
        result = self.wyt.cumulative_learning()
        assert result == True

    @allure.story("课本点读时长")
    def test_read_textbooks_point(self):
        """1.登录APP, 2.进入学习, 3.课本点读时长"""
        result = self.wyt.read_textbooks_point()
        assert result == True

    @allure.story("口语评测时长")
    def test_duration_of_oral_evaluation(self):
        """1.登录APP, 2.进入学习, 3.口语评测时长"""
        result = self.wyt.duration_of_oral_evaluation()
        assert result == True

    @allure.story("配音秀课本")
    def test_dubbing_show(self):
        """1.登录APP, 2.显示配音秀"""
        result = self.wyt.dubbing_show()
        assert result == True

    @allure.story("查看全部配音秀")
    def test_full_dubbing_show(self):
        """1.登录APP, 2.点击查看全部配音秀"""
        result = self.wyt.full_dubbing_show()
        assert result == True

    @allure.story("今日学习-学习时长")
    def test_learning_time(self):
        """1.进入学习界面, 2.今日学习时长统计, 3.进入跳转到我的学情"""
        result = self.wyt.learning_time()
        assert result == True

    @allure.story("今日学习-学习的图书")
    def test_learning_books(self):
        """绑定笔-点读图书封面-学习界面刷新"""
        result = self.wyt.learning_books()
        assert result == True

    @allure.story("今日学习-课本点读")
    def test_read_textbooks_point(self):
        """1.进入学习界面, 2.课本点读时长统计, 3.进入课本点读纪录"""
        result = self.wyt.read_textbooks_point()
        assert result == True

    @allure.story("今日学习-口语评测")
    def test_oral_english_testing(self):
        """1.进入学习界面, 2.口语评测时长统计, 3.进入口语评测纪录"""
        result = self.wyt.oral_english_testing()
        assert result == True

    @allure.story("今日学习-历史记录")
    def test_history(self):
        "1.进入学习界面, 2.点击历史记录, 3.进入历史记录页面"
        result = self.wyt.history()
        assert result == True

    @allure.story("周报-周报列表")
    def test_week_lists(self):
        """1.学情统计, 2.学情周报 3.日期列表展示正常"""
        result = self.wyt.week_lists()
        assert result == True

    @allure.story("周报-Week榜单")
    def test_week_list(self):
        """1.学情统计, 2.学情周报, 3.日期列表, 4.进入某一周学情统计, 5.Week榜单"""
        result = self.wyt.week_list()
        assert result == True

    @allure.story("周报-学习时长")
    def test_week_learning_time(self):
        """1.学情统计, 2.学情周报, 3.日期列表, 4.进入某一周学情统计, 5.本周学习时间"""
        result = self.wyt.week_learning_time()
        assert result == True

    # @allure.story("周报-口语评测时长")
    # def test_week_evaluating(self):
    #     """1.学情统计, 2.学情周报, 3.日期列表, 4.进入某一周学情统计, 5.本周口语练习"""
    #     result = self.wyt.week_evaluating()
    #     assert result == True

    @allure.story("周报-点读记录时长")
    def test_week_record(self):
        """1.学情统计, 2.学情周报, 3.日期列表, 4.进入某一周学情统计, 5.点读记录时长"""
        result = self.wyt.week_record()
        assert result == True

    @allure.story("分享-微信")
    def test_wechat(self):
        """1、进入我的界面, 2、选择中勋章，点击佩戴, 3、点击分享（手机无安装qq，微信）"""
        result = self.wyt.wechat()
        assert result == True

    @allure.story("分享-微信朋友圈")
    def test_wechat_friends(self):
        """1、进入我的界面, 2、选择中勋章，点击佩戴, 3、点击分享（手机无安装qq，微信）"""
        result = self.wyt.wechat_friends()
        assert result == True

    @allure.story("分享-QQ-取消")
    def test_QQ_cancel(self):
        """1、分享进入授权界面后点左上角取消/返回分享"""
        result = self.wyt.QQ_cancel()
        assert result == True

    @allure.story("分享-QQ-发送")
    def test_QQ_send(self):
        """1、进入我的界面, 2、选择中勋章，点击佩戴, 3、点击分享，跳转到第三方社交软件进行分享"""
        result = self.wyt.QQ_send()
        assert result == True

    @allure.story("分享-QQ朋友圈-取消")
    def test_QQ_interspace_cancel(self):
        """1、分享进入授权界面后点左上角取消/返回分享"""
        result = self.wyt.QQ_interspace_cancel()
        assert result == True

    def test_QQ_interspace_publish(self):
        """1、进入我的界面, 2、选择中勋章，点击佩戴, 3、点击分享，跳转到第三方社交软件进行分享"""
        result = self.wyt.QQ_interspace_publish()
        assert result == True

    def test_cancel(self):
        """1、进入我的界面, 2、选择中勋章，点击佩戴, 3、点击分享  4.点击取消分享"""
        result = self.wyt.cancel()
        assert result == True