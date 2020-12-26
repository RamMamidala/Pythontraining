from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time

browser=webdriver.Chrome()
browser.get('http://gmail.com')
browser.implicitly_wait(10)
browser.find_element_by_xpath("//input[@id='identifierId']").send_keys("saisriiram")
browser.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc']").click()
browser.implicitly_wait(15)
#browser.find_element_by_xpath("//input[@name='password']").send_keys("mssr1234")
#browser.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']").click()

