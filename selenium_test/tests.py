from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


class AdminLoginTests(LiveServerTestCase):

    def test_admin_login_success(self):
        driver.get('http://127.0.0.1:8000/admin/')
        time.sleep(1)
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        time.sleep(1)
        #Xpath 
        submit = driver.find_element(By.XPATH, "//form/div[@class='submit-row']/input[1]")
        username.send_keys('admin@user.com')
        password.send_keys('Welcome@12345')
        submit.send_keys(Keys.RETURN)
        time.sleep(5)
        assert 'log out' in driver.page_source

""" class LoginFormTest(LiveServerTestCase):

    def testform(self):
        #driver = webdriver.chrome()
        driver.get('http://127.0.0.1:8000/admin/')
        time.sleep(3)
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        time.sleep(3)
        #Xpath 
        submit = driver.find_element(By.XPATH, "//form/div[@class='submit-row']/input[1]")
        username.send_keys('admin@user.com')
        password.send_keys('Welcome@12345')
        submit.send_keys(Keys.RETURN) 
        from selenium_test.tests import *
        test = LoginFormTest()
        test.testform()
        """