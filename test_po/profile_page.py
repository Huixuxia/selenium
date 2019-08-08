from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver 继承于父类暂不需要
# profile类是通讯录-个人信息页面提供的方法的封装，包括编辑、启用、禁用、删除、置顶等方法
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.base_page import BasePage


class ProfilePage(BasePage):
    # def __init__(self, driver):
    #     self.driver: WebDriver = driver

    # def click_by_js(self, by, locator):
    #     self.driver.execute_script("arguments[0].click();",
    #                                self.driver.find_element(by, locator)
    #                                )
    # self.driver的初始化和click方法，从BasePage类继承

    def update_member(self, **kwargs):
        self.click_by_js(By.CSS_SELECTOR, ".js_edit")
        element=self.driver.find_element(By.NAME, "username")
        element.clear()
        element.send_keys("upname")
        self.click_by_js(By.CSS_SELECTOR, ".js_save")
        # todo:添加隐式等待，保存成功消失
        WebDriverWait(self.driver, 2).until(
            expected_conditions.invisibility_of_element((By.CSS_SELECTOR, ".js_tips"))
        )

    def disable_member(self):
        self.click_by_js(By.CSS_SELECTOR, ".js_disable")
        self.click_by_js(By.LINK_TEXT, "确认")
    # todo:启用方法

    def enable_member(self):
        self.click_by_js(By.CSS_SELECTOR, ".js_disable")

    def move_top(self):
        self.click_by_js(By.CSS_SELECTOR, ".js_move_top")

    def delete_member(self):
        self.click_by_js(By.CSS_SELECTOR, ".js_del_member")
        self.click_by_js(By.LINK_TEXT, "确认")
        # self.click_by_js(By.LINK_TEXT, "取消")
        # self.driver.find_element(By.CSS_SELECTOR, ".a[d_ck*='cancel']")



