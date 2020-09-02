import allure
from page.assign_homework import Assign_Homework
import pytest


@allure.feature("教师端布置作业")
@pytest.mark.run(order=1)
class Test_Assign_Homework():
    """该条测试用例为老师端提前布置，然后在学生端有作业完成，保证代码重复运行，该条用例为A开头，先启动教师端布置完作业，再启动学生端完成用例"""

    @allure.story("布置作业")
    def test_assign_homework(self):
        """老师端布置作业"""
        homework = Assign_Homework()
        result = homework.assign_homework()
        assert result == True
