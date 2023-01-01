from time import sleep
# import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Facebook.Bases_Test.regstor_location import *
# service=ChromeService(ChromeDriverManager().install())
registor = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
def test_registor_correctly():
    registor.get(
        "https://www.facebook.com/")
    sleep(2)
    registor.find_element(By.XPATH,create).click()
    sleep(3)
    registor.find_element(By.NAME,fname).send_keys("David")
    sleep(2)
    registor.find_element(By.NAME,lname).send_keys("israel")
    sleep(2)
    registor.find_element(By.XPATH,phone).send_keys("0533863205")
    sleep(2)
    registor.find_element(By.ID,pasword).send_keys("ade2013yal")
    sleep(2)
    registor.find_element(By.NAME,Month).click()
    sleep(2)
    registor.find_element(By.XPATH,Months).click()
    sleep(2)

    registor.find_element(By.NAME,Day).click()
    sleep(2)
    registor.find_element(By.XPATH,Days).click()
    sleep(2)

    registor.find_element(By.NAME,Year).click()
    sleep(2)
    registor.find_element(By.XPATH,Years).click()
    sleep(2)

    registor.find_element(By.XPATH,Male).click()
    sleep(2)

    registor.find_element(By.XPATH,sign_in).click()
    sleep(2)

def test_facebook_registorS_correctly():
    registor.get(
        "https://www.facebook.com/")

    sleep(2)
    registor.find_element(By.XPATH,create).click()
    sleep(3)
    registor.find_element(By.NAME,fname).send_keys("Aderajew")
    sleep(2)
    registor.find_element(By.NAME,lname).send_keys("Yalew")
    sleep(2)
    registor.find_element(By.XPATH,phone).send_keys("0533863205")
    sleep(2)
    registor.find_element(By.ID,pasword).send_keys("ade2013yal")
    sleep(2)
    registor.find_element(By.NAME,Month).click()
    sleep(2)
    registor.find_element(By.XPATH,Months).click()
    sleep(2)

    registor.find_element(By.NAME,Day).click()
    sleep(2)
    registor.find_element(By.XPATH,Days).click()
    sleep(2)

    registor.find_element(By.NAME,Year).click()
    sleep(2)
    registor.find_element(By.XPATH,Years).click()
    sleep(2)

    registor.find_element(By.XPATH,Male).click()
    sleep(2)

    registor.find_element(By.XPATH,sign_in).click()
    sleep(2)

def test_regstor_incorrect_phone():

    registor.get(
        "https://www.facebook.com/")

    sleep(2)
    registor.find_element(By.XPATH,create).click()
    sleep(3)
    registor.find_element(By.NAME,fname).send_keys("Aderajew")
    sleep(2)
    registor.find_element(By.NAME,lname).send_keys("Yalew")
    sleep(2)
    registor.find_element(By.XPATH,phone).send_keys("0533863205")
    sleep(2)
    registor.find_element(By.ID,pasword).send_keys("ade2013yal")
    sleep(2)
    registor.find_element(By.NAME,Month).click()
    sleep(2)
    registor.find_element(By.XPATH,Months).click()
    sleep(2)

    registor.find_element(By.NAME,Day).click()
    sleep(2)
    registor.find_element(By.XPATH,Days).click()
    sleep(2)

    registor.find_element(By.NAME,Year).click()
    sleep(2)
    registor.find_element(By.XPATH,Years).click()
    sleep(2)

    registor.find_element(By.XPATH,Male).click()
    sleep(2)

    registor.find_element(By.XPATH,sign_in).click()
    sleep(2)


def test_rgistor_incorrect_year():
    registor.get(
        "https://www.facebook.com/")

    sleep(2)
    registor.find_element(By.XPATH,create).click()
    sleep(3)
    registor.find_element(By.NAME,fname).send_keys("Aderajew")
    sleep(2)
    registor.find_element(By.NAME,lname).send_keys("Yalew")
    sleep(2)
    registor.find_element(By.XPATH,phone).send_keys("0533863205")
    sleep(2)
    registor.find_element(By.ID,pasword).send_keys("ade2013yal")
    sleep(2)
    registor.find_element(By.NAME,Month).click()
    sleep(2)
    registor.find_element(By.XPATH,Months).click()
    sleep(2)

    registor.find_element(By.NAME,Day).click()
    sleep(2)
    registor.find_element(By.XPATH,Days).click()
    sleep(2)

    registor.find_element(By.NAME,Year).click()
    sleep(2)
    registor.find_element(By.XPATH,Years).click()
    sleep(2)

    registor.find_element(By.XPATH,Male).click()
    sleep(2)

    registor.find_element(By.XPATH,sign_in).click()
    sleep(2)

def test_rgistor_incorrect_password():
    registor.get(
        "https://www.facebook.com/")

    sleep(2)
    registor.find_element(By.XPATH,create).click()
    sleep(3)
    registor.find_element(By.NAME,fname).send_keys("Aderajew")
    sleep(2)
    registor.find_element(By.NAME,lname).send_keys("Yalew")
    sleep(2)
    registor.find_element(By.XPATH,phone).send_keys("0533863205")
    sleep(2)
    registor.find_element(By.ID,pasword).send_keys("adddear")
    sleep(2)
    registor.find_element(By.NAME,Month).click()
    sleep(2)
    registor.find_element(By.XPATH,Months).click()
    sleep(2)

    registor.find_element(By.NAME,Day).click()
    sleep(2)
    registor.find_element(By.XPATH,Days).click()
    sleep(2)

    registor.find_element(By.NAME,Year).click()
    sleep(2)
    registor.find_element(By.XPATH,Years).click()
    sleep(2)

    registor.find_element(By.XPATH,Male).click()
    sleep(2)

    registor.find_element(By.XPATH,sign_in).click()
    sleep(2)
