from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
with webdriver.Chrome() as browser:
    browser.get("https://www.moneycontrol.com/")
    browser.implicitly_wait(10)
    marketAction=browser.find_element(By.XPATH,"//h2[@class='sub_title FL']")
    message1=marketAction.get_attribute("class")
    print(message1)
    globalMarkets=browser.find_element(By.XPATH,"//h3[@class='tplhead MB5']")
    message2=globalMarkets.value_of_css_property("color")
    print(message2)
    mostActive=browser.find_element(By.XPATH,"//a[@title='Most Active']")
    message3=mostActive.get_attribute("class")
    print(message3)