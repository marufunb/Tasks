from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "invalid"
password = "invalid"
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
element = driver.find_element_by_id("user-name")
element.send_keys(user_name)
element = driver.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/h3").text
assert element == "Epic sadface: Username and password do not match any user in this service"
driver.close()
