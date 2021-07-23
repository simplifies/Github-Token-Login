from selenium import webdriver
from selenium.webdriver.common.keys import Keys

inputtedSession = input("User Session Cookie: ")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get("https://github.com")
driver.add_cookie({'name': 'user_session', 'value': f'{inputtedSession}', 'domain': 'github.com'})
driver.get("https://github.com")