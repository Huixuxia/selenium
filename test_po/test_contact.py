from time import time, sleep

from test_po.contact_page import ContactPage
from test_po.wework_index import Wework

# 通讯录的业务测试用例


class TestContact:

    def setup(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver.implicitly_wait(2)
        # 再次优化单个测试用例的contact = ContactPage(self.work)取出
        self.work=Wework()
        self.contact = ContactPage(self.work)

    def teardown(self):
        sleep(2)
        self.work.quit()

    def test_add_member(self):
        # contact = ContactPage(self.work)
        self.contact.add_member("name2", "name2", "6", "18210290066")
        assert self.contact.get_tips() == "ok"

    def test_add_member_chinese(self):
        self.contact.add_member("思涵", "李杨", "4", "18210290064")
        assert self.contact.get_tips() == "ok"

    def test_delete_member(self):
        udid= str(time())
        # 删除之前先新增一条，并给这条新增记录添加时间戳
        self.contact.add_member("思涵"+udid, "李杨"+udid, "4"+udid, "18210290065")
        self.contact.search("思涵"+udid).delete_member()

    def test_update_profile(self):
        self.contact.search("name").update_member(upname=r"D:\PycharmProjects\Appium\images\oasis_1080.jpg")

    def test_disable(self):
        self.contact.search("思涵").disable_member()

    def test_enable(self):
        self.contact.search("思涵").enable_member()

