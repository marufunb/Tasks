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
item_names = []
try:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    titles = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='inventory_item_name']")))
    for title in titles:
        item_names.append(title.text)
except:
    pass
for item_name in item_names:
    print(item_name)
driver.quit()