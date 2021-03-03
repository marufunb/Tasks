from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "standard_user"
password = "secret_sauce"
firstName = "Md Mahbubur"
lastName = "Rahman"
postal = "E3B4C3"
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
element = driver.find_element_by_id("user-name")
element.send_keys(user_name)
element = driver.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[3]/button")
element.click()
element = driver.find_element_by_id("shopping_cart_container")
element.click()
element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/a[2]")
element.click()
element = driver.find_element_by_id("first-name")
element.send_keys(firstName)
element = driver.find_element_by_id("last-name")
element.send_keys(lastName)
element = driver.find_element_by_id("postal-code")
element.send_keys(postal)
element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/form/div[2]/input")
element.click()
element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div[3]/div[2]/a/div").text
assert element == "Sauce Labs Backpack"
driver.close()
