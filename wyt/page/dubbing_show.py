from common.baseapp import BaseApp
from time import sleep
import os
import allure


class Dubbing_Show(BaseApp):
    """配音秀"""
    loc_shujia = ("xpath", "//*[@text='书架' and @resource-id='com.viaton.wyt:id/page_bookshelf']")  #书架
    loc_jixupeiyin = ("xpath", "//*[@instance='8' and @resource-id='com.viaton.wyt:id/tv_dubbing']")  #继续配音
    loc_xuanze_shipin = ("xpath", "//*[contains(@text, 'Listen, point and say')]")  #选中一个视频
    loc_juesebanyan_jixupeiyin = ("id", "com.viaton.wyt:id/tv_start_dubbing")  #继续配音
    loc_mulu_1 = ("id", "com.viaton.wyt:id/tv_catalog")  #目录
    loc_dy_diandu_1 = ("id", "com.viaton.wyt:id/pw_main")  #断言显示课本
    loc_juesebanyan_2 = ("id", "com.viaton.wyt:id/tv_cosplay")  #角色扮演
    loc_kanshipin_3 = ("id", "com.viaton.wyt:id/tv_watch")  #看视频
    loc_tingkewen_4 = ("id", "com.viaton.wyt:id/tv_listen")  #听课文
    loc_dianjihuatong = ("id", "com.viaton.wyt:id/iv_start_record")  #点击话筒，开始配音
    loc_tuichu = ("id", "com.viaton.wyt:id/iv_back")  #配音过程中退出
    loc_xiayiju = ("id", "com.viaton.wyt:id/tv_next_question")  #下一句
    loc_tijiao = ("id", "com.viaton.wyt:id/tv_next_question")  #提交
    loc_gameover_play = ("id", "com.viaton.wyt:id/iv_cover")  #播放
    loc_dy_juesebanyan_1 = ("xpath", "//*[@text='角色扮演']")  #断言角色扮演成功-角色扮演
    loc_dy_juesebanyan_2 = ("id", "com.viaton.wyt:id/tv_score")  #断言角色扮演成功-分数
    loc_dy_juesebanyan_3 = ("id", "com.viaton.wyt:id/tv_ranking")  #断言角色扮演成功-排名
    loc_dy_juesebanyan_4 = ("id", "com.viaton.wyt:id/tv_share_note")  #断言角色扮演成功-分享到
    loc_pengyouquan = ("xpath", "//*[@text='朋友圈']")  #朋友圈
    loc_weixinhaoyou = ("xpath", "//*[@text='微信好友']")  #微信好友
    loc_QQkongjian = ("xpath", "//*[@text='QQ空间']")  #QQ空间
    loc_QQkongjian_quxiao = ("id", "com.tencent.mobileqq:id/ivTitleBtnLeft")  #取消发送
    loc_fabiao = ("id", "com.tencent.mobileqq:id/mpb")  #发表
    loc_QQ = ("xpath", "//*[@text='QQ']")  #QQ
    loc_wodediannao = ("xpath", "//*[@text='我的电脑']")  #我的电脑
    loc_QQ_quxiao = ("id", "com.tencent.mobileqq:id/dialogLeftBtn")  #取消
    loc_guanbi = ("id", "com.tencent.mobileqq:id/ivTitleBtnLeftButton")  #关闭
    loc_fabiao_QQ = ("id", "com.tencent.mobileqq:id/dialogRightBtn")  #发表
    loc_dy_fenxiangchenggong = ("id", "com.tencent.mobileqq:id/dialogText")  #分享成功
    loc_fanhuiwaiyantong = ("xpath", "//*[@text='返回外研通']")  #返回外研通
    loc_baocunbendi = ("id", "com.viaton.wyt:id/tv_save")  #保存本地
    loc_chongxintiaozhan = ("xpath", "//*[@text='重新挑战']")  #重新挑战
    loc_dy_lishijilu_1 = ("id", "com.viaton.wyt:id/tv_dub_note")  #断言历史配音记录-历史配音记录
    loc_dy_lishijilu_2 = ("xpath", "//*[@text='159']")  #断言历史配音记录-159
    loc_1 = ("xpath", "//*[@text='1']")  #1
    loc_dy_play_and_like_1 = ("id", "com.viaton.wyt:id/tv_title")  #断言-title
    loc_dy_play_and_like_2 = ("id", "com.viaton.wyt:id/tv_score")  #断言-分数
    loc_dy_play_and_like_3 = ("id", "com.viaton.wyt:id/iv_head_photo")  #断言-头像
    loc_dy_play_and_like_4 = ("id", "com.viaton.wyt:id/tv_name")  #断言-名称
    loc_dy_play_and_like_5 = ("id", "com.viaton.wyt:id/tv_time")  #断言-时间
    loc_dy_play_and_like_6 = ("id", "com.viaton.wyt:id/tv_play_num")  #断言-播放次数
    loc_dy_play_and_like_7 = ("id", "com.viaton.wyt:id/iv_cover")  #断言-视频显示
    loc_dy_play_and_like_8 = ("id", "com.viaton.wyt:id/tv_like_num")  #断言-点赞显示
    loc_dy_paihangbang_1 = ("id", "com.viaton.wyt:id/iv_top_icon")  #排行榜-排行榜图片
    loc_dy_paihangbang_2 = ('xpath', "//*[@text='50']")  #排行榜-第50位同学
    loc_houdong1_1 = ("xpath", "//*[@text='活动1' and @instance='2']")  #活动1-1
    loc_houdong2_1 = ("xpath", "//*[@text='活动2' and @instance='7']")  #活动2-1
    loc_shangyiju_tingkewen = ("id", "com.viaton.wyt:id/iv_last")  #上一句
    loc_xiayiju_tingkewen = ("id", "com.viaton.wyt:id/iv_next")  #下一句
    loc_bofang_zanting = ("id", "com.viaton.wyt:id/iv_play")  #播放暂停
    loc_shipin_diyige = ("xpath", "//*[@resource-id='com.viaton.wyt:id/iv_book_icon' and @instance='2']")
    loc_mulu5 = ("xpath", "//*[@text='Module 5']")  #目录5
    loc_mulu10 = ("xpath", "//*[@text='Module 10']")  #目录10
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习
    loc_xuexijilu = ("xpath", "//*[@text='学习记录']")  #学习记录

    loc_111 = ("id", "com.viaton.wyt:id/tv_grade_right")
    loc_222 = ("xpath", "//*[@text='全部']")
    @allure.step("目录")
    def catalog(self):
        "目录"

        #点击书架
        self.click_(self.loc_shujia)

        #点击一起一下继续配音
        self.click_(self.loc_jixupeiyin)

        #休眠5秒
        sleep(5)

        #点击目录
        self.click_(self.loc_mulu_1)

        #休眠3秒
        sleep(3)

        #点击目录5
        self.click_(self.loc_mulu5)

        #休眠3秒
        sleep(3)

        #点击目录
        self.click_(self.loc_mulu_1)

        #向上滑半个屏幕
        self.swipeUp()

        #休眠3秒
        sleep(3)

        #点击目录10
        self.click_(self.loc_mulu10)

        #休眠3秒
        sleep(3)

        #判断回到点读页面
        result = self.is_element_Exist(self.loc_mulu_1)

        return result

    @allure.step("角色扮演-中途退出")
    def role_play_quit(self):
        "配音秀-角色扮演-中途退出"

        #点击角色扮演
        self.click_(self.loc_juesebanyan_2)

        #休眠5秒，等待页面加载完成
        sleep(5)

        #点击视频“Listen, point and say”
        self.click_(self.loc_xuanze_shipin)

        #休眠5秒
        sleep(5)

        #点击继续配音
        self.click_(self.loc_juesebanyan_jixupeiyin)

        #休眠18秒，等待动画播放完成
        sleep(18)

        #点击“点击话筒 开始配音”
        self.click_(self.loc_dianjihuatong)

        #休眠10秒，等待录音完成
        sleep(10)

        #后退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #点击确定
        cmd = "adb shell input tap 790 1357"
        os.system(cmd)

        #判断回到继续配音页面
        result = self.is_element_Exist(self.loc_juesebanyan_jixupeiyin)

        return result

    @allure.step("角色扮演-成功")
    def role_play_succeed(self):
        "配音秀-角色扮演-成功"

        #休眠3秒
        sleep(3)

        #点击继续配音
        self.click_(self.loc_juesebanyan_jixupeiyin)

        #休眠18秒，等待动画播放完成
        sleep(18)

        #点击“点击话筒，开始配音”
        self.click_(self.loc_dianjihuatong)

        #休眠10秒，等待录音完成
        sleep(10)

        #点击下一句
        self.click_(self.loc_xiayiju)

        #休眠18秒，等待动画播放完成
        sleep(18)

        #点击“点击话筒，开始配音”
        self.click_(self.loc_dianjihuatong)

        #休眠10秒，等待录音完成
        sleep(10)

        #点击提交
        self.click_(self.loc_tijiao)

        #休眠30秒，等待视频合成完成
        sleep(30)

        #如果角色扮演、分数、排名、分享到都显示就返回True
        result_1 = self.is_element_Exist(self.loc_dy_juesebanyan_1)

        result_2 = self.is_element_Exist(self.loc_dy_juesebanyan_2)

        result_3 = self.is_element_Exist(self.loc_dy_juesebanyan_3)

        result_4 = self.is_element_Exist(self.loc_dy_juesebanyan_4)

        if result_1 and result_2 and result_3 and result_4:
            return True
        else:
            return False

    @allure.step("角色扮演-朋友圈")
    def circle_of_friends(self):
        "角色扮演-朋友圈"

        #休眠3秒
        sleep(3)

        #点击朋友圈
        self.click_(self.loc_pengyouquan)

        #断言"分享到"还在该页面
        result = self.is_element_Exist(self.loc_dy_juesebanyan_4)

        return result

    @allure.step("角色扮演-微信好友")
    def friend(self):
        "角色扮演-微信好友"

        #点击微信好友
        self.click_(self.loc_weixinhaoyou)

        #断言"分享到"还在该页面
        result = self.is_element_Exist(self.loc_dy_juesebanyan_4)

        return result

    @allure.step("角色扮演-QQ空间-取消发表")
    def QQ_space_cancel(self):
        "角色扮演-QQ空间-取消发表"

        #点击QQ空间
        self.click_(self.loc_QQkongjian)

        #点击后退取消发送
        self.click_(self.loc_QQkongjian_quxiao)

        #取消分享到QQ空间后，断言"分享到"还在该页面
        result = self.is_element_Exist(self.loc_dy_juesebanyan_4)

        return result

    @allure.step("角色扮演-QQ空间")
    def QQ_space(self):
        "角色扮演-QQ空间"

        #休眠5秒
        sleep(5)

        #点击QQ空间
        self.click_(self.loc_QQkongjian)

        #点击分享
        self.click_(self.loc_fabiao)

        #发表完成后，回到分享页面，断言"分享到"还在该页面
        result = self.is_element_Exist(self.loc_dy_juesebanyan_4)

        return result

    @allure.step("角色扮演-QQ-取消发送")
    def QQ_cancel(self):
        "角色扮演-QQ-取消发送"

        #休眠5秒
        sleep(5)

        #点击QQ
        self.click_(self.loc_QQ)

        #休眠3秒
        sleep(3)

        #点击我的电脑
        self.click_(self.loc_wodediannao)

        #休眠3秒
        sleep(3)

        #点击取消
        self.click_(self.loc_QQ_quxiao)

        #点击关闭
        self.click_(self.loc_guanbi)

        #取消发送后，回到分享页面，断言"分享到"还在该页面
        result = self.is_element_Exist(self.loc_dy_juesebanyan_4)

        return result

    @allure.step("角色扮演-QQ")
    def QQ(self):
        "角色扮演-QQ"

        #休眠5秒
        sleep(5)

        #点击QQ
        self.click_(self.loc_QQ)

        #休眠3秒
        sleep(3)

        #点击我的电脑
        self.click_(self.loc_wodediannao)

        #休眠3秒
        sleep(3)

        #点击发表
        self.click_(self.loc_fabiao_QQ)

        #休眠3秒
        sleep(3)

        #判断分享成功弹窗
        result = self.is_element_Exist(self.loc_dy_fenxiangchenggong)

        #休眠3秒
        sleep(3)

        #点击返回外研通
        self.click_(self.loc_fanhuiwaiyantong)

        #休眠3秒
        sleep(3)

        return result

    @allure.step("角色扮演-保存本地")
    def save(self):
        "角色扮演-保存本地"

        #休眠5秒
        sleep(5)

        #点击保存本地
        self.click_(self.loc_baocunbendi)

        #保存不稳定，有时需要时间较长，这里休眠20秒,等待保存成功
        sleep(20)

        #发表完成后，回到分享页面，断言"分享到"还在该页面
        result = self.is_element_Exist(self.loc_dy_juesebanyan_1)

        return result

    @allure.step("角色扮演-重新挑战")
    def challenge(self):
        "角色扮演-重新挑战"

        #休眠3秒
        sleep(3)

        #点击重新挑战
        self.click_(self.loc_chongxintiaozhan)

        #判断是否重新开始挑战，点击话筒，开始挑战是否在页面中
        result = self.is_element_Exist(self.loc_dianjihuatong)

        #休眠3秒
        sleep(3)

        #回退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #点击确定
        cmd = "adb shell input tap 790 1357"
        os.system(cmd)

        return result

    @allure.step("角色扮演-历史配音记录")
    def history(self):
        "历史配音记录"

        #休眠5秒
        sleep(5)

        #判断历史配音记录、159是否在页面中
        result_1 = self.is_element_Exist(self.loc_dy_lishijilu_1)
        result_2 = self.is_element_Exist(self.loc_dy_lishijilu_2)

        if result_1 and result_2:
            return True
        else:
            return False

    @allure.step("角色扮演-视频播放和点赞")
    def play_and_like(self):
        "视频播放和点赞"

        #休眠5秒
        sleep(5)

        #点击第一位同学
        self.click_(self.loc_1)

        #判断1.title  2.分数  3.图片  4.名称  5.时间  6.播放次数,是否在页面中
        result_1 = self.is_element_Exist(self.loc_dy_play_and_like_1)
        result_2 = self.is_element_Exist(self.loc_dy_play_and_like_2)
        result_3 = self.is_element_Exist(self.loc_dy_play_and_like_3)
        result_4 = self.is_element_Exist(self.loc_dy_play_and_like_4)
        result_5 = self.is_element_Exist(self.loc_dy_play_and_like_5)
        result_6 = self.is_element_Exist(self.loc_dy_play_and_like_6)
        result_7 = self.is_element_Exist(self.loc_dy_play_and_like_7)
        result_8 = self.is_element_Exist(self.loc_dy_play_and_like_8)

        #回退
        self.driver.press_keycode(4)

        if result_1 and result_2 and result_3 and result_4 and result_5 and result_6 and result_7 and result_8:
            return True
        else:
            return False

    @allure.step("角色扮演-排行榜")
    def ranking_list(self):
        "排行榜"

        #休眠3秒
        sleep(3)

        #判断排行榜图片是否能正常显示
        result_1 = self.is_element_Exist(self.loc_dy_paihangbang_1)

        #向上滑到底
        self.swipeUp(n=9)

        #判断第50位同学是否能正常显示
        result_2 = self.is_element_Exist(self.loc_dy_paihangbang_2)

        #回退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #回退
        self.driver.press_keycode(4)

        if result_1 and result_2:
            return True
        else:
            return False

    @allure.step("看视频")
    def watch_video(self):
        "看视频"

        #休眠3秒
        sleep(3)

        #点击看视频图标
        self.click_(self.loc_kanshipin_3)

        #休眠3秒，等待页面加载
        sleep(3)

        #点击第一个视频
        self.click_(self.loc_shipin_diyige)

        #休眠5秒
        sleep(5)

        #回退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #回退
        self.driver.press_keycode(4)

        #判断回到点读页面
        result = self.is_element_Exist(self.loc_dy_diandu_1)

        return result

    @allure.step("听课文")
    def listen_text(self):
        "听课文"

        #休眠3秒
        sleep(3)

        #点击听课文图标
        self.click_(self.loc_tingkewen_4)

        #休眠5秒，等待页面加载
        sleep(5)

        #点击活动1
        self.click_(self.loc_houdong1_1)

        #休眠5秒
        sleep(5)

        #点击第一模块 第二单元 活动2
        self.click_(self.loc_houdong2_1)

        #休眠10秒
        sleep(10)

        #点击下一句,视频播放过程中，定位下一句和上一句不稳定
        self.click_(self.loc_xiayiju_tingkewen)

        #休眠10秒
        sleep(10)

        #点击上一句,视频播放过程中，定位下一句和上一句不稳定
        self.click_(self.loc_shangyiju_tingkewen)

        #休眠10秒
        sleep(10)

        #播放中暂停
        self.click_(self.loc_bofang_zanting)

        #休眠5秒
        sleep(5)

        #暂停后播放
        self.click_(self.loc_bofang_zanting)

        #休眠3秒
        sleep(3)

        #回退
        self.driver.press_keycode(4)

        #判断回到点读页面
        result = self.is_element_Exist(self.loc_dy_diandu_1)

        #回退
        self.driver.press_keycode(4)

        #休眠3秒
        sleep(3)

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        #点击学习记录，保准每个用例集的起点一致
        self.click_(self.loc_xuexijilu)

        return result
