import pytest
import allure
from page.pen_setting import Pen_Setting

@allure.feature("点读笔设置")
@pytest.mark.run(order=13)
class Test_Pen_Setting():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = Pen_Setting(driver)

    @allure.story("点读笔显示")
    def test_display(self):
        """1、进入我的界面  2、进入点读笔设置"""
        result = self.wyt.display()
        assert result == True

    @allure.story("断开连接-取消")
    def test_disconnect_cancel(self):
        """1、进入我的界面  2、进入点读笔设置  3、断开连接  4、点击取消"""
        result = self.wyt.disconnect_cancel()
        assert result == True

    @allure.story("断开连接-确定")
    def test_disconnect(self):
        """1、进入我的界面  2、进入点读笔设置  3、断开连接  4、点击确定"""
        result = self.wyt.disconnect()
        assert result == False

    @allure.story("连接-确定")
    def test_connect(self):
        """1、进入我的界面  2、进入点读笔设置  3、连接  4、点击确定"""
        result = self.wyt.connect()
        assert result == True

    @allure.story("wifi")
    def test_wifi(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击wi-fi设置"""
        result = self.wyt.wifi()
        assert result == True

    @allure.story("刷新")
    def test_refresh(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击wi-fi设置  4、点击刷新"""
        result = self.wyt.refresh()
        assert result == True

    @allure.story("添加网络")
    def test_add_networking(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击wi-fi设置  4、点击添加网络"""
        result = self.wyt.add_networking()
        assert result == True

    @allure.story("缓存管理")
    def test_cache(self):
        """1、进入我的界面  2、进入点读笔设置  3、缓存管理"""
        result = self.wyt.cache()
        assert result == True

    @allure.story("删除缓存-取消")
    def test_delete_cache_cancel(self):
        """1、进入我的界面  2、进入点读笔设置  3、缓存管理  4、删除缓存  5、取消删除"""
        result = self.wyt.delete_cache_cancel()
        assert result == True

    @allure.story("删除缓存-成功")
    def test_delete_cache(self):
        """1、进入我的界面  2、进入点读笔设置  3、缓存管理  4、删除缓存  5、确定删除"""
        result = self.wyt.delete_cache()
        assert result == True

    @allure.story("固件升级")
    def test_upgrade(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击固件升级"""
        result = self.wyt.upgrade()
        assert result == True

    @allure.story("蓝牙音箱")
    def test_bluetooth_speaker(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击蓝牙音箱"""
        result = self.wyt.bluetooth_speaker()
        assert result == True

    @allure.story("蓝牙音箱-刷新")
    def test_bluetooth_speaker_refresh(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击蓝牙音箱  4、点击刷新"""
        result = self.wyt.bluetooth_speaker_refresh()
        assert result == True

    @allure.story("自动下载")
    def test_automatic_download(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击自动下载"""
        result = self.wyt.automatic_download()
        assert result == True

    @allure.story("自动下载-禁用")
    def test_forbidden(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击自动下载  4、点击禁用"""
        result = self.wyt.forbidden()
        assert result == True

    @allure.story("自动下载-开启")
    def test_open(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击自动下载  4、点击开启"""
        result = self.wyt.open()
        assert result == True

    @allure.story("休眠时间设置")
    def test_sleep_time(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击休眠时间"""
        result = self.wyt.sleep_time()
        assert result == True

    @allure.story("休眠时间设置-5分钟")
    def test_sleep_time_5(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击休眠时间  3、点击5分钟"""
        result = self.wyt.sleep_time_5()
        assert result == True

    @allure.story("休眠时间设置-10分钟")
    def test_sleep_time_10(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击休眠时间  3、点击10分钟"""
        result = self.wyt.sleep_time_10()
        assert result == True

    @allure.story("休眠时间设置-30分钟")
    def test_sleep_time_30(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击休眠时间  3、点击30分钟"""
        result = self.wyt.sleep_time_30()
        assert result == True

    @allure.story("休眠时间设置-永不")
    def test_sleep_time_perpetual(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击休眠时间  3、点击永不"""
        result = self.wyt.sleep_time_perpetual()
        assert result == True

    @allure.story("自动关机")
    def test_automatic_shut(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击自动关机"""
        result = self.wyt.automatic_shut()
        assert result == True

    @allure.story("自动关机-30分钟")
    def test_automatic_shut_30(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击自动关机  4、点击30分钟"""
        result = self.wyt.automatic_shut_30()
        assert result == True

    @allure.story("自动关机-60分钟")
    def test_automatic_shut_60(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击自动关机  4、点击60分钟"""
        result = self.wyt.automatic_shut_60()
        assert result == True

    @allure.story("自动关机-120分钟")
    def test_automatic_shut_120(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击自动关机  4、点击120分钟"""
        result = self.wyt.automatic_shut_120()
        assert result == True

    @allure.story("自动关机-永不")
    def test_automatic_shut_perpetual(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击自动关机  4、点击永不"""
        result = self.wyt.automatic_shut_perpetual()
        assert result == True

    @allure.story("本机信息")
    def test_device_info(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息"""
        result = self.wyt.device_info()
        assert result == True

    @allure.story("修改昵称-直接点击保存")
    def test_change_nickname_save(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击屏幕显示昵称  5、直接点击保存"""
        result = self.wyt.change_nickname_save()
        assert result == True

    @allure.story("修改昵称-输入1位数")
    def test_change_nickname_1(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击屏幕显示昵称  5、输入“1”  6、点击保存"""
        result = self.wyt.change_nickname_1()
        assert result == True

    @allure.story("修改昵称-输入10位数")
    def test_change_nickname_10(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击屏幕显示昵称  5、输入“abc1234ABC”  6、点击保存"""
        result = self.wyt.change_nickname_10()
        assert result == True

    @allure.story("修改昵称-输入11位数")
    def test_change_nickname_11(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击屏幕显示昵称  5、输入“0.12ABCBabc”  6、点击保存"""
        result = self.wyt.change_nickname_11()
        assert result == True

    @allure.story("修改昵称-输入特殊符号")
    def test_change_nickname_symbol(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击屏幕显示昵称  5、输入“~!@#$%^&*()”  6、点击保存"""
        result = self.wyt.change_nickname_symbol()
        assert result == True

    @allure.story("修改昵称-输入159")
    def test_change_nickname_159(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击屏幕显示昵称  5、输入“159”  6、点击保存"""
        result = self.wyt.change_nickname_159()
        assert result == True

    @allure.story("学习账号")
    def test_learning_account(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击学习账号"""
        result = self.wyt.learning_account()
        assert result == True

    @allure.story("移除绑定-取消")
    def test_remove_binding_cancel(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击学习账号  5、点击移除绑定  6、点击取消"""
        result = self.wyt.remove_binding_cancel()
        assert result == True

    @allure.story("移除绑定-成功")
    def test_remove_binding(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击学习账号  5、点击移除绑定  6、点击确定"""
        result = self.wyt.remove_binding()
        assert result == False

    @allure.story("绑定学习账号")
    def test_binding_study_account(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击学习账号"""
        result = self.wyt.binding_study_account()
        assert result == True

    @allure.story("绑定新笔-取消")
    def test_binding_new_pen_cancel(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击绑定新笔  5、点击取消"""
        result = self.wyt.binding_new_pen_cancel()
        assert result == True

    @allure.story("绑定新笔-成功")
    def test_binding_new_pen(self):
        """1、进入我的界面  2、进入点读笔设置  3、点击本机信息  4、点击绑定新笔  5、点击确定"""
        result = self.wyt.binding_new_pen()
        assert result == True
