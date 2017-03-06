# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from lib.Pil import get_sceent_shot
import unittest, time, re


class BugfreeLogin1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_bugfree_login1(self):

     """测试管理员用户是否成功登录"""
     try:
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)
        get_sceent_shot(u'2.main_page')
        driver.find_element_by_link_text('退出').click()
     except Exception as e:
         get_sceent_shot(u'Exception_test_login')



    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()