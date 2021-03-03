from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
user_name = "standard_user"
password = "secret_sauce"
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
element = driver.find_element_by_id("user-name")
element.send_keys(user_name)
element = driver.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
item_prices = []
try:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    prices = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='inventory_item_price']")))
    for price in prices:
        item_prices.append(price.text)
except:
    pass
for item_price in item_prices:
    print(item_price[1:])

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/a/div").click()
element = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[3]").text
assert element == item_prices[0]
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/button").click()

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/a/div").click()
element = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[3]").text
assert element == item_prices[1]
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/button").click()

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[3]/div[2]/a/div").click()
element = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[3]").text
assert element == item_prices[2]
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/button").click()

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[4]/div[2]/a/div").click()
element = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[3]").text
assert element == item_prices[3]
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/button").click()

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[5]/div[2]/a/div").click()
element = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[3]").text
assert element == item_prices[4]
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/button").click()

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[6]/div[2]/a/div").click()
element = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[3]").text
assert element == item_prices[5]

driver.quit()