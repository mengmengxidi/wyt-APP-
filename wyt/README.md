#### 项目描述

此项目为Android***自动化代码，使用python+appium+pytest+allure编写，基本覆盖***Android APP全部功能，可用作回归测试，确保APP基本流程可以走通

#### 版本说明

python3.6、jdk1.8.0、node.js10.2.0、NET Framework4.5、sdk24.4.1、appium1.7.1、appium-python-client0.26、pytest4.5.0、allure2.13.0

#### 依赖包

使用豆瓣源下载：pip install -i https://pypi.douban.com/simple -r requirements.txt

#### 执行

1、cd到case目录，进入cmd

2、生成报告：pytest --alluredir ../report/allure_raw --clear

3、查看报告：allure serve ../report/allure_raw

#### 说明

测试手机为华为青春10，如相机、相册用到华为自带的APP，在其他手机执行时，部分用例会失败

#### jenkins持续集成

构建地址：<http://129.211.9.9:8080/jenkins/>       账号：admin      密码：123456

Allure报告：<http://129.211.9.9:8080/jenkins/job/wyt_automation_code/39/allure/> 

