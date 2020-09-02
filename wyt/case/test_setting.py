import pytest
from page.setting import Setting
import allure

@allure.feature("设置")
@pytest.mark.run(order=17)
class Test_Setting():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = Setting(driver)

    @allure.story("设置")
    def test_Setting(self):
        """1.点击我的  2.点击设置"""
        result = self.wyt.setting()
        assert result == True

    @allure.story("检查升级")
    def test_upgrade(self):
        """1.点击我的  2.点击设置  3.点击检查升级"""
        result = self.wyt.upgrade()
        assert result == True

    @allure.story("清除缓存-取消")
    def test_clear_cache_cancel(self):
        """1.点击我的  2.点击设置  3.点击清除缓存  4.点击取消"""
        result = self.wyt.clear_cache_cancel()
        assert result == True

    @allure.story("清除缓存")
    def test_clear_cache(self):
        """1.点击我的  2.点击设置  3.点击清除缓存  4.点击确定"""
        result = self.wyt.clear_cache()
        assert result == True

    @allure.story("蓝牙连接模式")
    def test_bluetooth_mode(self):
        """1.点击我的  2.点击设置  3.点击蓝牙连接模式"""
        result = self.wyt.bluetooth_mode()
        assert result == True

    @allure.story("蓝牙连接模式-BLE")
    def test_bluetooth_mode_BLE(self):
        """1.点击我的  2.点击设置  3.点击蓝牙连接模式  4.点击BLE"""
        result = self.wyt.bluetooth_mode_BLE()
        assert result == True

    @allure.story("蓝牙连接模式-经典蓝牙")
    def test_bluetooth_mode_classic(self):
        """1.点击我的  2.点击设置  3.点击蓝牙连接模式  4.点击经典蓝牙"""
        result = self.wyt.bluetooth_mode_classic()
        assert result == True

    @allure.story("关于我们")
    def test_about_us(self):
        """1.点击我的  2.点击设置  3.点击关于我们"""
        result = self.wyt.about_us()
        assert result == True

    @allure.story("隐私说明")
    def test_privacy(self):
        """1.点击我的  2.点击设置  3.点击隐私说明"""
        result = self.wyt.privacy()
        assert result == True

    @allure.story("护眼模式")
    def test_eyeshield(self):
        """1.点击我的  2.点击设置  3.点击护眼模式按钮"""
        result = self.wyt.eyeshield()
        assert result == True

    @allure.story("消息推送")
    def test_push_notification(self):
        """1.点击我的  2.点击设置  3.点击消息推送按钮"""
        result = self.wyt.push_notification()
        assert result == True

    @allure.story("使用帮助")
    def test_usinghelp(self):
        """1.点击我的  2.点击设置  3.点击使用帮助"""
        result = self.wyt.usinghelp()
        assert result == True

    @allure.story("使用帮助-第1项")
    def test_usinghelp_1(self):
        """1.点击我的  2.点击设置  3.点击使用帮助  4.点击第1项"""
        result = self.wyt.usinghelp_1()
        assert result == True

    @allure.story("使用帮助-第3项")
    def test_usinghelp_3(self):
        """1.点击我的  2.点击设置  3.点击使用帮助  4.点击第3项"""
        result = self.wyt.usinghelp_3()
        assert result == True

    @allure.story("使用帮助-第4项")
    def test_usinghelp_4(self):
        """1.点击我的  2.点击设置  3.点击使用帮助  4.点击第4项"""
        result = self.wyt.usinghelp_4()
        assert result == True

    @allure.story("使用帮助-第5项")
    def test_usinghelp_5(self):
        """1.点击我的  2.点击设置  3.点击使用帮助  4.点击第5项"""
        result = self.wyt.usinghelp_5()
        assert result == True

    @allure.story("使用帮助-第6项")
    def test_usinghelp_6(self):
        """1.点击我的  2.点击设置  3.点击使用帮助  4.点击第6项"""
        result = self.wyt.usinghelp_6()
        assert result == True

    @allure.story("使用帮助-第7项")
    def test_usinghelp_7(self):
        """1.点击我的  2.点击设置  3.点击使用帮助  4.点击第7项"""
        result = self.wyt.usinghelp_7()
        assert result == True

    @allure.story("使用帮助-第8项")
    def test_usinghelp_8(self):
        """1.点击我的  2.点击设置  3.点击使用帮助  4.点击第8项"""
        result = self.wyt.usinghelp_8()
        assert result == True

    @allure.story("使用帮助-第9项")
    def test_usinghelp_9(self):
        """1.点击我的  2.点击设置  3.点击使用帮助  4.点击第9项"""
        result = self.wyt.usinghelp_9()
        assert result == True

    @allure.story("使用帮助-第10项")
    def test_usinghelp_10(self):
        """1.点击我的  2.点击设置  3.点击使用帮助  4.点击第10项"""
        result = self.wyt.usinghelp_10()
        assert result == True

    @allure.story("使用帮助-第11项")
    def test_usinghelp_11(self):
        """1.点击我的  2.点击设置  3.点击使用帮助  4.点击第11项"""
        result = self.wyt.usinghelp_11()
        assert result == True

    @allure.story("使用帮助-第12项")
    def test_usinghelp_12(self):
        """1.点击我的  2.点击设置  3.点击使用帮助  4.点击第12项"""
        result = self.wyt.usinghelp_12()
        assert result == True

    @allure.story("使用手册-VT-10")
    def test_handbook_vt_10(self):
        """1.点击我的  2.点击设置  3.点击使用手册  4.点击VT-10笔"""
        result = self.wyt.handbook_vt_10()
        assert result == True

    @allure.story("使用手册-VT-9")
    def test_handbook_vt_9(self):
        """1.点击我的  2.点击设置  3.点击使用手册  4.点击VT-9笔"""
        result = self.wyt.handbook_vt_9()
        assert result == True

    @allure.story("使用手册-VT-8")
    def test_handbook_vt_8(self):
        """1.点击我的  2.点击设置  3.点击使用手册  4.点击VT-8笔"""
        result = self.wyt.handbook_vt_8()
        assert result == True

    @allure.story("意见反馈-只输入意见或建议")
    def test_feedback_1(self):
        """1.点击我的  2.点击设置  3.点击意见反馈  4.只输入意见或建议,点提交"""
        result = self.wyt.feedback_1()
        assert result == False

    @allure.story("意见反馈-只输入联系方式")
    def test_feedback_2(self):
        """1.点击我的  2.点击设置  3.点击意见反馈  4.只输入联系方式,点提交"""
        result = self.wyt.feedback_2()
        assert result == True

    @allure.story("意见反馈-意见反馈-意见和联系方式都正确输入")
    def test_feedback_3(self):
        """1.点击我的  2.点击设置  3.点击意见反馈  4.意见和联系方式都正确输入,点提交"""
        result = self.wyt.feedback_3()
        assert result == False

    @allure.story("客服电话")
    def test_service_tel(self):
        """1.点击我的  2.点击设置  3.点击客服电话"""
        result = self.wyt.service_tel()
        assert result == True

    @allure.story("修改密码")
    def test_change_password(self):
        """1.点击我的  2.点击设置  3.点击修改密码"""
        result = self.wyt.change_password()
        assert result == True

    @allure.story("了解智能点读笔")
    def test_learn_read_pen(self):
        """1.点击我的  2.点击了解智能点读笔"""
        result = self.wyt.learn_read_pen()
        assert result == True
