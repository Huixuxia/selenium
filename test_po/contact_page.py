from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from test_po.base_page import BasePage
from test_po.profile_page import ProfilePage


class ContactPage(BasePage):
    _username = (By.NAME, "username")
    _alias = (By.NAME, "english_name")
    _accid = (By.NAME, "acctid")
    _mobile = (By.NAME, "mobile")
    _contact = (By.ID, "menu_contacts")
    _cancel = (By.CSS_SELECTOR, ".js_btn_cancel")
    _leave = (By.LINK_TEXT, "离开此页")
    _search = (By.ID, "memberSearchInput")
    _save = (By.CSS_SELECTOR, ".js_btn_save")

    def __init__(self, wework):
        self.driver = wework.driver
    #  def __init__(self, work):
    #    self.driver: WebDriver = work.driver
    #    第一阶段self.driver在这里定义,第二阶段继承BasePage类

    # def click_by_js(self, by, locator):
    #    self.driver.execute_script("arguments[0].click();",
    #                              self.driver.find_element(by, locator)
    #                               )
    #    优化到公共类BasePage，同样继承于公共类

    def add_member(self, name, alias, id,  mobile, **kwargs):
        # todo：find()方法未生效
        self.driver.find_element(*self._contact).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".js_has_member .js_add_member"))
        )
        sleep(2)
        self.click_by_js(By.CSS_SELECTOR, ".js_has_member .js_add_member")
        # todo:偶尔出现无法识别用户名的情况
        self.driver.find_element(*self._username).send_keys(name)
        self.driver.find_element(*self._alias).send_keys(alias)
        self.driver.find_element(*self._accid).send_keys(id)
        self.driver.find_element(*self._mobile).send_keys(mobile)
        #  *self用法，是find_element方法传递的是两个参数，用*将_id = (By.NAME, "acctid")元组拆分
        #  self.driver.find_element(*self._cancel).click()
        self.driver.implicitly_wait(2)
        # todo:两个click无效
        self.driver.find_element(*self._save).click()
        # self.driver.find_element(By.XPATH, "//*[text(),'离开此页']").click()
        # self.driver.find_element(*self._leave).click()

    def search(self, key):
        self.driver.find_element(*self._contact).click()
        self.driver.find_element(*self._search).clear()
        self.driver.find_element(*self._search).send_keys(key)
        return ProfilePage(self.driver)

    def delete(self):
        self.click_by_js(By.CSS_SELECTOR, "js_del_member")

    def update(self):
        pass

    def get_tips(self):
        return "ok"
