from common.baseapp import BaseApp
from time import sleep
import os
import allure

class Learning_Record(BaseApp):
    """学习-学习记录"""

    #元素定位
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习
    loc_xuexijilu = ("xpath", "//*[@text='学习记录']")  #学习记录
    loc_touxiangxianshi = ("id", "com.viaton.wyt:id/iv_head")  #头像显示
    loc_mingchengxianshi = ("xpath", "//*[@text='159']")  #名称显示
    loc_xuexidaka = ("xpath", "//*[contains(@text,'学习打卡')]")  #学习打卡
    loc_xuexidaka_tianshu = ("id", "com.viaton.wyt:id/tv_day")  #学习打卡天数
    loc_xingdongli = ("xpath", "//*[contains(@text,'行动力超越')]")  #行动力超越
    loc_xingdingli_zhanbizhi = ("id", "com.viaton.wyt:id/tv_surpass_num")  #行动力占比
    loc_xingdongli_detongxue = ("xpath", "//*[contains(@text,'的同学')]")  #的同学
    loc_leijixuexi_1 = ("xpath", "//*[@text='累计学习']")  #累计学习
    loc_leijixuexi_2 = ("id", "com.viaton.wyt:id/tv_learning_day")  #累计学习天数
    loc_leijixuexi_3 = ("xpath", "//*[@text='天']")   #累计学习天
    loc_kebendiandu_1 = ("xpath", "//*[@text='课本点读']")  #课本点读
    loc_kebendiandu_2 = ("id", "com.viaton.wyt:id/tv_book_study_time")  #课本点读时长
    loc_kebendiandu_3 = ("xpath", "//*[@text='小时']")   #课本点读小时
    loc_kouyupingce_1 = ("xpath", "//*[@text='口语评测']")  #口语评测
    loc_kouyupingce_2 = ("id", "com.viaton.wyt:id/tv_spoken_time")  #口语评测时长
    loc_kouyupingce_3 = ("xpath", "//*[@text='分钟']")   #口语评测分钟
    loc_diandubi_lianjie = ("id", "com.viaton.wyt:id/banner_image")  #外研通点读笔链接
    loc_dy_diandubi_lianjie = ("id", "com.android.browser:id/topbar")  #断言点击链接跳转
    loc_peiyinxiu = ("xpath", "//*[@text='英语（新标准）一年级起点二年级下册']")  #配音秀课本
    loc_dy_peiyinxiu = ("xpath", "//*[contains(@text,'配音秀')]")   #断言配音秀
    loc_chakanquanbu = ("xpath", "//*[@text='查看全部']")  #查看全部配音秀
    loc_dy_chakanquanbu = ("xpath", "//*[@text='配音秀历史记录']")  #断言进入查看全部页面
    loc_jinri_xuexishichang = ("xpath", "//*[@text='学习时长']")  #今日学习时长
    loc_xuexidetushu = ("xpath", "//*[@text='学习的图书']")  #今日学习的图书
    loc_dy_jinri_xuexishichang = ("xpath", "//*[@text='我的学情']")  #断言进入我的详情页面
    loc_kebendiandu = ("xpath", "//*[@text='课本点读']")  #今日课本点读
    loc_dy_kebendiandu = ("xpath", "//*[@text='课本点读记录']")  #断言进入课本点读记录页面
    loc_kouyupince = ("xpath", "//*[@text='口语评测']")  #口语评测
    loc_dy_kouyupince = ("xpath", "//*[@text='口语评测记录']")  #断言进入口语评测记录页面
    loc_jinri_lishijilu = ("id", "com.viaton.wyt:id/cv_learn_history")  #历史记录
    loc_dy_lishijilu = ("xpath", "//*[@text='学习动态']")  #断言进入历史记录页面
    loc_shangzhouxueqing = ("id", "com.viaton.wyt:id/tv_last_week_time")  #周报
    loc_week_zhoubaoliebiao = ("xpath", "//*[@text='Yd2JbWR2h63YX0m0PhzJ7RLwIlU7Q0EgNVqoBi6BepUAxsu9wH8TPv4ZcTcXQAAAABJRU5ErkJggg==']")  #周报列表
    loc_dy_week_zhoubaoliebia_1 = ("xpath", "//*[@text='5月份学情周报']")  #断言进入周报列表,5月份学情周报
    loc_dy_week_zhoubaoliebia_2 = ("xpath", "//*[@text='最多显示最近半年数据']")  #断言进入周报列表,最多显示最近半年数据
    loc_5yuefenzhoubaoxiangqing = ("xpath", "//*[@text='5月份学情周报']")  #5月份学情周报
    loc_5yuefendiyicizhoubaoxiangqing = ("xpath", "//*[@text='05月第一次学情周报']")  #05月第一次学情周报
    loc_dy_week_benzhoupaiming = ("xpath", "//*[contains(@text, '本周排名')]")  #断言Week榜单
    loc_dy_week_xuexishichang = ("xpath", "//*[@text='学习时长（分钟）']")  #断言学习时长
    loc_dy_week_kouyupingce = ("xpath", "//*[contains(@text, '口语评测')]")  #断言口语评测
    loc_dy_week_diandujilu = ("xpath", "//*[contains(@text, '英语')]")  #断言点读纪录
    loc_fenxiang = ("xpath", "//*[@text='EO0npagIAtiRbvjHTa8cAAAAASUVORK5CYII=']")  #分享
    loc_fenxiang_weixin =("xpath", "//*[@text='微信']")  #分享微信
    loc_fenxiang_weixinpengyouquan =("xpath", "//*[@text='微信朋友圈']")  #分享微信朋友圈
    loc_fenxiang_QQ =("xpath", "//*[@text='QQ']")  #分享QQ
    loc_wodediannao = ("xpath", "//*[@text='我的电脑']")  #选择我的电脑
    loc_wodediannao_quxiao = ("id", "com.tencent.mobileqq:id/dialogLeftBtn")  #取消
    loc_quxiao_guanbi = ("id", "com.tencent.mobileqq:id/ivTitleBtnLeftButton")  #关闭
    loc_wodediannao_fasong = ("xpath", "//*[@text='发送']")  #发送
    loc_dy_fenxiangchenggong = ("xpath", "//*[@text='分享成功']")  #断言分享成功
    loc_fanhuiwanyantong = ("xpath", "//*[@text='返回外研通']")  #返回外研通
    loc_quxiaofenxiang = ("xpath", "//*[@text='取消分享']")  #取消分享
    loc_fenxiang_QQkongjian =("xpath", "//*[@text='QQ空间']")  #分享QQ空间
    loc_qqkongjian_quxiao = ("xpath", "//*[@text='取消']")  #取消
    loc_qqkongjian_fangqi = ("xpath", "//*[@text='放弃上传']")  #放弃上传
    loc_qqkongjian_fabiao = ("xpath", "//*[@text='发表']")  #发表
    loc_fenxiang_quxiaofenxiang =("xpath", "//*[@text='取消分享']")  #取消分享
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的

    @allure.step("头像显示")
    def picture_shows(self):
        "头像显示"

        #点击学习
        self.click_(self.loc_xuexi)

        #向下滑半个屏幕，刷新页面，避免页面未加载出来
        self.swipeDown()

        #休眠8秒
        sleep(8)

        #判断头像是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_touxiangxianshi)

        return result

    @allure.step("名称显示")
    def display_name(self):
        "名称显示"

        #判断名称是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_mingchengxianshi)

        return result

    @allure.step("学习打卡时长")
    def learning_to_clock_in(self):
        "学习打卡时长"

        #判断学习打卡时长是否正确显示，返回Bool
        result_1 = self.is_element_Exist(self.loc_xuexidaka)
        result_2 = self.is_element_Exist(self.loc_xuexidaka_tianshu)

        if result_1 and result_2:
            return True
        else:
            return False

    @allure.step("行动力占比值")
    def action_force_ratio(self):
        "行动力占比值"

        #判断行动力占比值是否正确显示，返回Bool
        result_1 = self.is_element_Exist(self.loc_xingdongli)
        result_2 = self.is_element_Exist(self.loc_xingdingli_zhanbizhi)
        result_3 = self.is_element_Exist(self.loc_xingdongli_detongxue)

        if result_1 and result_2 and result_3:
            return True
        else:
            return False

    @allure.step("累计学习时长")
    def cumulative_learning(self):
        "累计学习时长"

        #判断累计学习时长是否正确显示，返回Bool
        result_1 = self.is_element_Exist(self.loc_leijixuexi_1)
        result_2 = self.is_element_Exist(self.loc_leijixuexi_2)
        result_3 = self.is_element_Exist(self.loc_leijixuexi_3)

        if result_1 and result_2 and result_3:
            return True
        else:
            return False

    @allure.step("课本点读时长")
    def read_textbooks_point(self):
        "课本点读时长"

        #判断课本点读时长是否正确显示，返回Bool
        result_1 = self.is_element_Exist(self.loc_kebendiandu_1)
        result_2 = self.is_element_Exist(self.loc_kebendiandu_2)
        result_3 = self.is_element_Exist(self.loc_kebendiandu_3)

        if result_1 and result_2 and result_3:
            return True
        else:
            return False

    @allure.step("口语评测时长")
    def duration_of_oral_evaluation(self):
        "口语评测时长"

        #判断口语评测时长是否正确显示，返回Bool
        result_1 = self.is_element_Exist(self.loc_kouyupingce_1)
        result_2 = self.is_element_Exist(self.loc_kouyupingce_2)
        result_3 = self.is_element_Exist(self.loc_kouyupingce_3)

        if result_1 and result_2 and result_3:
            return True
        else:
            return False

    @allure.step("显示配音秀")
    def dubbing_show(self):
        "显示配音秀"

        #判断配音秀是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_peiyinxiu)

        return result

    @allure.step("点击查看全部配音秀，进入配音秀历史记录")
    def full_dubbing_show(self):
        "点击查看全部配音秀，可以进入对应页面"

        #点击查看全部
        self.click_(self.loc_chakanquanbu)

        #判断配音秀历史记录页面是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_chakanquanbu)

        #休眠5秒
        sleep(5)

        #回退
        self.driver.press_keycode(4)

        #向上划半个屏幕
        self.swipeUp()

        #休眠5秒，等待页面加载，避免因网络情况导致页面加载慢而出错
        sleep(5)

        return result

    @allure.step("今日学习-学习时长")
    def learning_time(self):
        "今日学习-学习时长"

        #点击学习时长
        self.click_(self.loc_jinri_xuexishichang)

        #休眠5秒，等待页面加载，避免因网络情况导致页面加载慢而出错
        sleep(5)

        #判断我的详情页面是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_jinri_xuexishichang)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("今日学习-学习的图书")
    def learning_books(self):

        #判断学习的图书是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_xuexidetushu)

        return result

    @allure.step("今日学习-课本点读")
    def read_textbooks_point(self):
        "今日学习-课本点读"

        #点击课本点读
        self.click_(self.loc_kebendiandu)

        #休眠5秒
        sleep(5)

        #判断课本点读记录页面是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_kebendiandu)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("今日学习-口语评测")
    def oral_english_testing(self):
        "今日学习-口语评测"

        #点击口语评测
        self.click_(self.loc_kouyupince)

        #休眠5秒
        sleep(5)

        #判断口语评测记录页面是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_kouyupince)

        #回退
        self.driver.press_keycode(4)

        return result

    @allure.step("今日学习-历史记录")
    def history(self):
        "今日学习-历史记录"

        #点击今日历史记录
        self.click_(self.loc_jinri_lishijilu)

        #休眠5秒
        sleep(5)

        #判断历史记录页面是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_lishijilu)

        #后退
        self.driver.press_keycode(4)

        return result

    @allure.step("周报-周报列表")
    def week_lists(self):
        "周报-周报列表"

        #点击上周学情
        self.click_(self.loc_shangzhouxueqing)

        #休眠5秒
        sleep(5)

        #点击周报列表
        self.click_(self.loc_week_zhoubaoliebiao)

        #判断周报列表是否正确显示，返回Bool
        result_1 = self.is_element_Exist(self.loc_dy_week_zhoubaoliebia_1)
        result_2 = self.is_element_Exist(self.loc_dy_week_zhoubaoliebia_2)

        #休眠3秒
        sleep(3)

        if result_1 and result_2:
            return True
        else:
            return False

    @allure.step("周报-Week榜单")
    def week_list(self):
        "周报-Week榜单"

        #点击5月份学情周报
        self.click_(self.loc_5yuefenzhoubaoxiangqing)

        #点击05月第一次学情周报
        self.click_(self.loc_5yuefendiyicizhoubaoxiangqing)

        #判断全国Week榜单是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_week_benzhoupaiming)

        return result

    @allure.step("周报-学习时长")
    def week_learning_time(self):
        "周报-学习时长"

        #判断学习时长是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_week_xuexishichang)

        return result

    @allure.step("周报-口语评测时长")
    def week_evaluating(self):
        "周报-口语评测时长"

        #向上滑半个屏幕
        self.swipeUp()

        #判断口语评测时长是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_week_kouyupingce)

        return result

    @allure.step("周报-点读记录时长")
    def week_record(self):
        "周报-点读纪录时长"

        #向上滑半个屏幕
        self.swipeUp()

        #判断点读纪录时长是否正确显示，返回Bool
        result = self.is_element_Exist(self.loc_dy_week_diandujilu)

        return result

    @allure.step("分享-微信")
    def wechat(self):
        "分享-微信"

        #向下滑动一个屏幕
        self.swipeDown(n=2)

        #休眠2秒
        sleep(2)

        #点击分享
        self.click_(self.loc_fenxiang)

        #休眠2秒
        sleep(2)

        #点击微信
        self.click_(self.loc_fenxiang_weixin)

        #未安装微信，判断是否回到一周回顾页面，返回Bool
        result = self.is_element_Exist(self.loc_fenxiang)

        return result

    @allure.step("分享-微信朋友圈")
    def wechat_friends(self):
        "分享-微信朋友圈"

        #休眠2秒
        sleep(2)

        #点击分享
        self.click_(self.loc_fenxiang)

        #休眠2秒
        sleep(2)

        #点击微信朋友圈
        self.click_(self.loc_fenxiang_weixinpengyouquan)

        #未安装微信，判断是否回到一周回顾页面，返回Bool
        result = self.is_element_Exist(self.loc_fenxiang)

        return result

    @allure.step("分享-QQ-取消")
    def QQ_cancel(self):
        "分享-QQ-取消"

        #休眠2秒
        sleep(2)

        #点击分享
        self.click_(self.loc_fenxiang)

        #休眠2秒
        sleep(2)

        #点击QQ
        self.click_(self.loc_fenxiang_QQ)

        #休眠5秒
        sleep(5)

        #点击“我的电脑”
        self.click_(self.loc_wodediannao)

        #休眠2秒
        sleep(2)

        #点击取消
        self.click_(self.loc_wodediannao_quxiao)

        #休眠2秒
        sleep(2)

        #点击关闭
        self.click_(self.loc_quxiao_guanbi)

        #休眠2秒
        sleep(2)

        #取消分享，判断是否回到一周回顾页面，返回Bool
        result = self.is_element_Exist(self.loc_fenxiang)

        return result

    @allure.step("分享-QQ-发送")
    def QQ_send(self):
        "分享-QQ-发送"

        #休眠2秒
        sleep(2)

        #点击分享
        self.click_(self.loc_fenxiang)

        #休眠2秒
        sleep(2)

        #点击QQ
        self.click_(self.loc_fenxiang_QQ)

        #休眠5秒
        sleep(5)

        #点击“我的电脑”
        self.click_(self.loc_wodediannao)

        #休眠2秒
        sleep(2)

        #点击发送
        self.click_(self.loc_wodediannao_fasong)

        #休眠2秒
        sleep(2)

        #判断分享成功弹窗是否弹出，返回Bool
        result = self.is_element_Exist(self.loc_dy_fenxiangchenggong)

        #点击返回外研通
        self.click_(self.loc_fanhuiwanyantong)

        return result

    @allure.step("分享-QQ空间-取消")
    def QQ_interspace_cancel(self):
        "分享-QQ空间-取消"

        #休眠2秒
        sleep(2)

        #点击分享
        self.click_(self.loc_fenxiang)

        #休眠2秒
        sleep(2)

        #点击QQ空间
        self.click_(self.loc_fenxiang_QQkongjian)

        #休眠2秒
        sleep(2)

        #点击取消
        self.click_(self.loc_qqkongjian_quxiao)

        #休眠2秒
        sleep(2)

        #点击放弃上传
        self.click_(self.loc_qqkongjian_fangqi)

        #休眠2秒
        sleep(2)

        #取消分享，判断是否回到一周回顾页面，返回Bool
        result = self.is_element_Exist(self.loc_fenxiang)

        return result

    @allure.step('分享-QQ空间-发表')
    def QQ_interspace_publish(self):
        "分享-QQ空间-发表"

        #休眠2秒
        sleep(2)

        #点击分享
        self.click_(self.loc_fenxiang)

        #休眠2秒
        sleep(2)

        #点击QQ空间
        self.click_(self.loc_fenxiang_QQkongjian)

        #休眠2秒
        sleep(2)

        #点击发表
        self.click_(self.loc_qqkongjian_fabiao)

        #休眠2秒
        sleep(2)

        #发表成功，判断是否回到一周回顾页面，返回Bool
        result = self.is_element_Exist(self.loc_fenxiang)

        return result

    @allure.step("分享-取消分享")
    def cancel(self):
        "分享-取消分享"

        #休眠2秒
        sleep(2)

        #点击分享
        self.click_(self.loc_fenxiang)

        #休眠2秒
        sleep(2)

        #点击取消分享
        self.click_(self.loc_quxiaofenxiang)

        #取消分享，判断是否回到一周回顾页面，返回Bool
        result = self.is_element_Exist(self.loc_fenxiang)

        #回退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #后退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #后退
        self.driver.press_keycode(4)

        #休眠5秒，等待页面加载完成
        sleep(5)

        return result