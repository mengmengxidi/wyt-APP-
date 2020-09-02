import pytest
import allure
from page.read_evaluation import Read_Evaluation

@allure.feature("学习-阅读评测")
@pytest.mark.run(order=4)
class Test_Read_Evaluation():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver):
        self.wyt = Read_Evaluation(driver)

    @allure.story("我的等级")
    def test_grade(self):
        """1.进入学习， 2.阅读评测， 3.我的等级"""
        result =self.wyt.grade()
        assert result == True

    @allure.story("查看成长轨迹")
    def test_growth_process(self):
        """1.进入学习， 2.阅读评测， 3.查看成长轨迹"""
        result = self.wyt.growth_process()
        assert result == True

    @allure.story("我能阅读几级读物")
    def test_read(self):
        """1.进入学习， 2.阅读评测， 3.我能阅读几级读物"""
        result = self.wyt.read()
        assert result == True

    @allure.story("可用12次")
    def test_usable_number(self):
        """1.绑定笔, 2.返回到我的界面, 3.提示：赠送12次口语评测"""
        result = self.wyt.usable_number()
        assert result == True

    @allure.story("开始评测")
    def test_review_began(self):
        """1.进入学习, 2.阅读评测, 3.开始测试, 4.提交"""
        result = self.wyt.review_began()
        assert result == True

    @allure.story("模拟测试")
    def test_simulation(self):
        """1.进入学习, 2.阅读评测, 3.模拟测试"""
        result = self.wyt.simulation()
        assert result == True

    @allure.story("购买记录")
    def test_record(self):
        """1.进入学习, 2.点击阅读评测, 3.选择购买次数, 4.点击记录"""
        result = self.wyt.record()
        assert result == True

    @allure.story("服务协议")
    def test_agreement(self):
        """1.进入学习, 2.进入阅读评测, 3.购买次数, 4.进入用户协议"""
        result = self.wyt.agreement()
        assert result == True

    @allure.story("隐私条款")
    def test_privacy_policy(self):
        """1.进入学习, 2.进入阅读评测, 3.购买次数, 4.进入隐私条款"""
        result = self.wyt.privacy_policy()
        assert result == True

    @allure.story("支付宝支付")
    def test_alipay(self):
        """1.进入学习, 2.点击阅读评测, 3.选择购买次数, 4.点击立即购买, 5.选择支付宝支付"""
        result = self.wyt.alipay()
        assert result == True

    @allure.story("微信支付")
    def test_wechat(self):
        """1.进入学习, 2.点击阅读评测, 3.选择购买次数, 4.点击立即购买, 5.选择微信支付"""
        result = self.wyt.wechat()
        assert result == True
