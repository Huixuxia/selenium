from selenium import webdriver
#   Wework类提供了driver的初始化过程
from selenium.webdriver.common.by import By


class Wework:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver.implicitly_wait(2)
        url = "https://work.weixin.qq.com/wework_admin/frame"
        self.driver.get(url)
        cookies = {
            "wwrtx.vst": "HQNcas2JZ68NSvc3MBTNy9VTFiTkrGkaR_LdfhHeTV0w8NkyMnf4D56IZZ7YY9UwkLPI-N6OBB0OfOUidvXH3Y6YttwrSeiPX93af_eG9yxxdmjqkvYXZbFzuIDI0UMLfzWBopv3Iay65nm6UTFTK3N139YQmy2Yvizb9xodKERRKRin-yizOdRzlom5gVPxE2kAGTlQBL-5NSlmQQRyWpQthIrm5-PxOKm7DPx9lJRoVXR8dQXfhxa5V1dLqY3eBhBtcW0BTpzdmrloDOINvw",
            "wwrtx.ltype": "1",
            "wxpay.vid": "1688853402934970",
            "wwrtx.d2st": "a3407383",
            "wxpay.corpid": "1970324957083409",
            "wwrtx.sid": "5wYZc9lIOWLsomT2zVjMF2Y6IrB2yUSAMWw5efub9ZLSG3jukwwQeoJPpSAdkCN8"
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.implicitly_wait(1)
        self.driver.get(url)
        self.driver.implicitly_wait(1)

    def quit(self):
        self.driver.quit()
