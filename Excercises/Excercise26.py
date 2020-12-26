from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

with webdriver.Chrome() as driver:
    driver.get("https://www.training-support.net/selenium/iframes")
    wait=WebDriverWait(driver,10)
    driver.switch_to.frame(0)
    frame1=driver.find_element(By.XPATH,"//div[@class='content']")
    print(frame1.text)
    button=driver.find_element(By.ID,"actionButton")
    buttonColor=button.value_of_css_property("color")
    buttonBg=button.value_of_css_property("background-color")
    buttonText=button.text
    print(buttonColor)
    print(buttonBg)
    print(buttonText)
    button.click()
    buttonColor2=button.value_of_css_property("color")
    buttonBg2=button.value_of_css_property("background-color")
    buttonText2=button.text
    print(buttonColor2)
    print(buttonBg2)
    print(buttonText2)
    driver.switch_to.default_content()
    driver.switch_to.frame(1)
    button2=driver.find_element(By.ID,"actionButton")
    button2Color=button2.value_of_css_property("color")
    button2Bg=button2.value_of_css_property("background-color")
    buttonText=button2.text
    print(button2Color)
    print(button2Bg)
    print(buttonText)
    button2.click()
    button2Color2=button2.value_of_css_property("color")
    button2Bg2=button2.value_of_css_property("background-color")
    buttonText2=button2.text
    print(button2Color2)
    print(button2Bg2)
    print(buttonText2)
    time.sleep(7)

