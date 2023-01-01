from time import sleep
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Facebook.Bases_Test.forgot_password_location import *

forgot = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from selenium.webdriver.common.by import By


def test_forgot_password():
    forgot.get("https://www.facebook.com/")
    forgot.find_element(By.XPATH,forgot_password).click()
    sleep(1)


    forgot.find_element(By.ID,email).send_keys(phone)
    sleep(2)

    forgot.find_element(By.XPATH,Search).click()
    sleep(2)

    texts = forgot.find_element(By.XPATH, Tag1).text
    assert texts == "Reset Your Password"

    forgot.find_element(By.XPATH,contenue).click()
    sleep(2)

    forgot.find_element(By.XPATH,cancel).click()
    sleep(2)
