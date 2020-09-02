from common.baseapp import BaseApp
from time import sleep
import os
import allure

class Bookrack(BaseApp):
    """书架"""

    #元素定位
    loc_shujia = ("xpath", "//*[@text='书架' and @resource-id='com.viaton.wyt:id/page_bookshelf']")  #书架
    loc_sousuokuang = ("id", "com.viaton.wyt:id/cet_keyword")  #搜索框
    loc_sousuo_anniu = ("id", "com.viaton.wyt:id/iv_search")  #搜索按钮
    loc_dy_soudaotushu = ("xpath", "//*[@text='缓存到笔']")  #断言是否搜到书
    loc_quanbu = ("id", "com.viaton.wyt:id/tv_grade_right")  #全部
    loc_youeryuan = ("xpath", "//*[@text='幼儿园']")  #幼儿园
    loc_yinianji = ("xpath", "//*[@text='一年级']")  #一年级
    loc_chusan = ("xpath", "//*[@text='初三']")  #初三
    loc_gaoer = ("xpath", "//*[@text='高二']")  #高二
    loc_nianji_quanbu = ("xpath", "//*[@text='全部']")  #全部
    loc_quanbu_zhichi = ("xpath", "//*[@text='全部' and @resource-id='com.viaton.wyt:id/tab_item_textview']") #支持-全部
    loc_zhichipeiyinxiu = ("xpath", "//*[@text='支持配音秀']")  #支持配音秀
    loc_zhichikouyupingce = ("xpath", "//*[@text='支持口语评测']")  #支持口语评测
    loc_zhichiyinpindainbo = ("xpath", "//*[@text='支持音频点播']")  #支持音频点播
    loc_sanheng = ("id", "com.viaton.wyt:id/iv_book_menu")  #右上角全部下面的三横
    loc_quanbu_sanhengxiade = ("xpath", "//*[@resource-id='com.viaton.wyt:id/tab_item_textview' and @instance='5']")  #全部-三横下拉框中的
    loc_keben = ("xpath", "//*[@text='课本']")  #课本
    loc_huiben = ("xpath", "//*[@text='绘本']")  #绘本
    loc_jiaofu = ("xpath", "//*[@text='教辅']")  #教辅
    loc_qita = ("xpath", "//*[@text='其他']")  #其他
    loc_huancundaobi = ("xpath", "//*[@text='缓存到笔' and @instance='6']")  #缓存到笔，一年级下册
    loc_tuisongbofang = ("xpath", "//*[@text='推送播放' and @instance='7']")  #推送播放
    loc_quedin_bofang = ("id", "com.viaton.wyt:id/tv_confirm")  #确定播放
    loc_dy_yingyumoerduo_1 = ("xpath", "//*[@text='英语磨耳朵']")  #断言进入英语磨耳朵
    loc_xiayishou = ("id", "com.viaton.wyt:id/iv_next_on_demand")  #下一首
    loc_shangyishou = ("id", "com.viaton.wyt:id/iv_last_on_demand")  #上一首
    loc_bofang_zanting = ("id", "com.viaton.wyt:id/iv_play_on_demand")  #播放/暂停
    loc_dy_yingyumoerduo_2 = ('xpath', "//*[@text='英语（新标准）一年级起点一年级下册']")  #断言退出英语磨耳朵
    loc_xuexi = ("id", "com.viaton.wyt:id/page_study")  #学习
    loc_xuexijilu = ("xpath", "//*[@text='学习记录']")  #学习记录
    loc_wode = ("id", "com.viaton.wyt:id/page_my")  #我的

    @allure.step("书架-搜索")
    def search(self):
        "书架-搜索"

        #点击书架
        self.click_(self.loc_shujia)

        #点击搜索
        cmd = "adb shell input tap 1030 165"
        os.system(cmd)

        #休眠5秒
        sleep(5)

        #输入“a”
        self.send_Keys(self.loc_sousuokuang, "a")

        #点击搜索按钮
        self.click_(self.loc_sousuo_anniu)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("书架-模糊搜索")
    def fuzzy_search(self):
        "书架-模糊搜索"

        #清空输入框
        self.clear_(self.loc_sousuokuang)

        #输入“a_Going”
        self.send_Keys(self.loc_sousuokuang, "a_Going")

        #点击搜索按钮
        self.click_(self.loc_sousuo_anniu)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("搜索-数字")
    def search_number(self):
        "搜索-数字"

        #清空输入框
        self.clear_(self.loc_sousuokuang)

        #输入数字“10”
        self.send_Keys(self.loc_sousuokuang, "10")

        #点击搜索按钮
        self.click_(self.loc_sousuo_anniu)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("搜索-特殊符号")
    def search_symbol(self):
        "搜索-特殊符号"

        #清空输入框
        self.clear_(self.loc_sousuokuang)

        #输入特殊符号“_”
        self.send_Keys(self.loc_sousuokuang, "_")

        #点击搜索按钮
        self.click_(self.loc_sousuo_anniu)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("年级选择-幼儿园")
    def select_kindergarten(self):
        "年级选择-幼儿园"

        #回退
        self.driver.press_keycode(4)

        #点击搜索按钮下面的全部
        self.click_(self.loc_quanbu)

        #点击幼儿园
        self.click_(self.loc_youeryuan)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("年级选择-一年级")
    def select_first_grade(self):
        "年级选择-一年级"

        #点击搜索按钮下面的全部
        self.click_(self.loc_quanbu)

        #点击一年级
        self.click_(self.loc_yinianji)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("年级选择-初三")
    def select_junior_three(self):
        "年级选择-初三"

        #点击搜索按钮下面的全部
        self.click_(self.loc_quanbu)

        #点击初三
        self.click_(self.loc_chusan)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("年级选择-高二")
    def select_senior_two(self):
        "年级选择-高二"

        #点击搜索按钮下面的全部
        self.click_(self.loc_quanbu)

        #点击高二
        self.click_(self.loc_gaoer)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("年级选择-全部")
    def select_all(self):
        "年级选择-全部"

        #点击搜索按钮下面的全部
        self.click_(self.loc_quanbu)

        #点击全部
        self.click_(self.loc_nianji_quanbu)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("支持配音秀")
    def select_dubbing_show(self):
        "支持配音秀"

        #点击支持配音秀
        self.click_(self.loc_zhichipeiyinxiu)

        #休眠2秒
        sleep(2)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        #休眠2秒，等待页面跳转
        sleep(2)

        if book_list:
            return True
        else:
            return False

    @allure.step("支持口语评测")
    def select_evaluating(self):
        "支持口语评测"

        #点击支持口语评测
        self.click_(self.loc_zhichikouyupingce)

        #休眠2秒
        sleep(2)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("支持音频点播")
    def select_audio(self):
        "支持音频点播"

        #点击支持音频点播
        self.click_(self.loc_zhichipeiyinxiu)

        #休眠2秒
        sleep(2)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        #休眠2秒，等待页面跳转
        sleep(2)

        #点击支持口语评测
        self.click_(self.loc_zhichikouyupingce)

        #休眠2秒
        sleep(2)

        #点击支持配音秀
        self.click_(self.loc_zhichipeiyinxiu)

        #休眠2秒
        sleep(2)

        #点击全部
        self.click_(self.loc_quanbu_zhichi)

        #休眠2秒
        sleep(2)

        if book_list:
            return True
        else:
            return False

    @allure.step("课本")
    def select_textbook_learning(self):
        "课本"

        #点击右上角全部下面的三横
        self.click_(self.loc_sanheng)

        #休眠2秒，等待页面跳转
        sleep(2)

        #点击课本
        self.click_(self.loc_keben)

        #休眠2秒
        sleep(2)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("绘本")
    def select_picture_book(self):
        "绘本"

        #点击绘本
        self.click_(self.loc_huiben)

        #休眠2秒，等待页面跳转
        sleep(2)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("教辅")
    def select_assistants(self):
        "教辅"

        #点击教辅
        self.click_(self.loc_jiaofu)

        #休眠2秒，等待页面跳转
        sleep(2)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        if book_list:
            return True
        else:
            return False

    @allure.step("其他")
    def select_else(self):
        "其他"

        #点击其他
        self.click_(self.loc_qita)

        #休眠2秒，等待页面跳转
        sleep(2)

        #find_Elements返回list，如果没有搜到书，则返回空列表
        book_list = self.find_Elements(self.loc_dy_soudaotushu)

        #点击全部，回到全部
        self.click_(self.loc_quanbu_sanhengxiade)

        #点击三横，收回三横下的内容
        self.click_(self.loc_sanheng)

        if book_list:
            return True
        else:
            return False

    @allure.step("缓存到笔")
    def cache(self):
        "缓存到笔,为了代码能循环跑，需要在缓存管理中删除该资源"

        #休眠5秒
        sleep(5)

        try:
            #点击缓存到笔
            self.click_(self.loc_huancundaobi)

            #休眠3秒
            sleep(3)

            return True
        except:
            return False


    @allure.step("推送播放")
    def push_to_play(self):
        "推送播放"

        #点击推送播放
        self.click_(self.loc_tuisongbofang)

        #点击确定
        self.click_(self.loc_quedin_bofang)

        #点击音乐图标
        cmd = "adb shell input tap 952 2051"
        os.system(cmd)
        sleep(5)

        #判断是否调到英语磨耳朵页面，返回Bool
        result = self.is_element_Exist(self.loc_dy_yingyumoerduo_1)

        #休眠10秒
        sleep(10)

        #点击下一首
        self.click_(self.loc_xiayishou)

        #休眠5秒
        sleep(5)

        #点击上一首
        self.click_(self.loc_shangyishou)

        #休眠5秒
        sleep(5)

        #点击暂停
        self.click_(self.loc_bofang_zanting)

        #休眠5秒
        sleep(5)

        #回退
        self.driver.press_keycode(4)

        #刷新页面
        self.swipeDown()

        #休眠2秒
        sleep(2)

        #点击学习，保准每个用例集的起点一致
        self.click_(self.loc_xuexi)

        #点击学习记录，保准每个用例集的起点一致
        self.click_(self.loc_xuexijilu)

        #休眠5秒
        sleep(5)

        return result
