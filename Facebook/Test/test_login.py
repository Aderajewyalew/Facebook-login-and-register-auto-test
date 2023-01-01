from time import sleep
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from selenium.webdriver.common.by import By
from Facebook.Bases_Test.login_location import *
import pytest


driver.get("https://en-gb.facebook.com/")

def test_login_correct_input():
    username = driver.find_element(By.XPATH,f"{username_correct}")
    time.sleep(2)
    username.clear()
    username.send_keys("0534714275")
    time.sleep(2)
    password = driver.find_element(By.XPATH,f"{pasword_correct}")
    password.clear()
    password.send_keys("ade2013yal")
    time.sleep(2)
    driver.find_element(By.XPATH,f"{login_button}").click()
    time.sleep(2)
    # driver.find_element(By.XPATH,f"{vedio}").click()
    # time.sleep(5)
    Url = driver.current_url
    assert Url == "https://www.facebook.com/"




def test_login_incorrct_email():
    usernamel = driver.find_element(By.XPATH,f"{username_correct}")
    usernamel.clear()
    usernamel.send_keys("00000000000")
    time.sleep(2)
    paswordl = driver.find_element(By.XPATH,f"{pasword_correct}")
    paswordl.clear()
    paswordl.send_keys("ade2013yal")
    driver.find_element(By.XPATH,f"{login_button}").click()
    time.sleep(2)
    Url = driver.current_url
    assert Url == "https://www.facebook.com/"

def test_login_incorrect_pasword():
    username = driver.find_element(By.XPATH,f"{username_correct}")
    username.clear()
    username.send_keys("0534714275")
    time.sleep(2)
    password = driver.find_element(By.XPATH,f"{pasword_correct}")
    password.click()
    password.send_keys("aaaaaa")
    time.sleep(2)
    driver.find_element(By.XPATH,f"{login_button}").click()
    time.sleep(2)
    Url = driver.current_url
    assert Url == "https://www.facebook.com/"


def test_login_incorrect_pasword_email():
    Username = driver.find_element(By.XPATH,f"{username_correct}")
    Username.clear()
    Username.send_keys("123456789")
    time.sleep(2)
    pasword = driver.find_element(By.XPATH,f"{pasword_correct}")
    pasword.clear()
    pasword.send_keys("xxxxxxx")
    time.sleep(2)
    driver.find_element(By.XPATH,
                        f"{login_button}").click()
    time.sleep(2)
    Url = driver.current_url
    assert Url == "https://www.facebook.com/"



