import pytest
from page.chat_assistant import Chat_Assistant
import allure

@allure.feature("聊天")
@pytest.mark.run(order=14)
class Test_Chat_Assistant():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        print("开始自动化测试用例")
        self.wyt = Chat_Assistant(driver)

    @allure.story("发送消息成功")
    def test_fasongxiaoxi_207(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.按住说话"""
        result = self.wyt.message_5s()
        assert result == True

    @allure.story("按住61s发送消息")
    def test_fasongxiaoxi_61s_208(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.按住说话61秒"""
        result = self.wyt.message_60s()
        assert result == True

    @allure.story("向上滑动取消发送")
    def test_fasongxiaoxi_shibai(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.按住说话  4.向上滑动取消发送"""
        result = self.wyt.message_cancel()
        assert result == False

    @allure.story("设置")
    def test_setting(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置"""
        result = self.wyt.setting()
        assert result == True

    @allure.story("添加")
    def test_add(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击添加"""
        result = self.wyt.add()
        assert result == True

    @allure.story("分享-微信")
    def test_wechat_1(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击添加  5、点击分享  6、点击微信"""
        result = self.wyt.wechat_1()
        assert result == True

    @allure.story("分享-微信朋友圈")
    def test_friends_1(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击添加  5、点击分享  6、点击微信朋友圈"""
        result = self.wyt.friends_1()
        assert result == True

    @allure.story("分享-取消分享")
    def test_cancel_1(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击添加  5、点击分享  6、点击取消分享"""
        result = self.wyt.cancel_1()
        assert result == True

    @allure.story("移除")
    def test_remove(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击移除"""
        result = self.wyt.remove()
        assert result == True

    @allure.story("聊天群名称-不输入")
    def test_group_name(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击聊天群名称  5、点击确认"""
        result = self.wyt.group_name_no()
        assert result == True

    @allure.story("聊天群名称-1位数")
    def test_group_name_1(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击聊天群名称  5、输入1位数  6、点击确认"""
        result = self.wyt.group_name_1()
        assert result == True

    @allure.story("聊天群名称-14位数")
    def test_group_name_14(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击聊天群名称  5、输入14位数  6、点击确认"""
        result = self.wyt.group_name_14()
        assert result == True

    @allure.story("聊天群名称-15位数")
    def test_group_name_15(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击聊天群名称  5、输入15位数  6、点击确认"""
        result = self.wyt.group_name_15()
        assert result == True

    @allure.story("聊天群名称-特殊符号")
    def test_group_name_symbol(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击聊天群名称  5、输入特殊符号  6、点击确认"""
        result = self.wyt.group_name_symbol()
        assert result == True

    @allure.story("聊天群名称-qinneng_group")
    def test_group_name_qinneng_group(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击聊天群名称  5、输入qinneng_group  6、点击确认"""
        result = self.wyt.group_name_qinneng_group()
        assert result == True

    @allure.story("我的昵称-不输入")
    def test_my_nickname_no(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击我的昵称  5、点击确认"""
        result = self.wyt.my_nickname_no()
        assert result == True

    @allure.story("我的昵称-1位数")
    def test_my_nickname_1(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击我的昵称  5、输入1位数  6、点击确认"""
        result = self.wyt.my_nickname_1()
        assert result == True

    @allure.story("我的昵称-10位数")
    def test_my_nickname_10(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击我的昵称  5、输入10位数  6、点击确认"""
        result = self.wyt.my_nickname_10()
        assert result == True

    @allure.story("我的昵称-11位数")
    def test_my_nickname_11(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击我的昵称  5、输入11位数  6、点击确认"""
        result = self.wyt.my_nickname_11()
        assert result == True

    @allure.story("我的昵称-特殊符号")
    def test_my_nickname_symbol(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击我的昵称  5、输入特殊符号  6、点击确认"""
        result = self.wyt.my_nickname_symbol()
        assert result == True

    @allure.story("我的昵称-qinneng")
    def test_my_nickname_qinneng(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击我的昵称  5、输入qinneng  6、点击确认"""
        result = self.wyt.my_nickname_qinneng()
        assert result == True

    @allure.story("邀请家庭成员一起加入")
    def test_invite(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击邀请家庭成员一起加入"""
        result = self.wyt.invite()
        assert result == True

    @allure.story("分享-微信")
    def test_wechat_2(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击邀请家庭成员一起加入  5、点击分享  6、点击微信"""
        result = self.wyt.wechat_2()
        assert result == True

    @allure.story("分享-微信朋友圈")
    def test_friends_2(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击邀请家庭成员一起加入  5、点击分享  6、点击微信朋友圈"""
        result = self.wyt.friends_2()
        assert result == True

    @allure.story("分享-取消分享")
    def test_cancel_2(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击邀请家庭成员一起加入  5、点击分享  6、点击取消分享"""
        result = self.wyt.cancel_2()
        assert result == True

    @allure.story("智能笔上线提醒")
    def test_remind(self):
        """1.绑定V10笔  2.进入智能笔聊天助手  3.点击右上角设置  4、点击智能笔上线提醒"""
        result = self.wyt.remind()
        assert result == True
