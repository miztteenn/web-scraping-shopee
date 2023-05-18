from selenium import webdriver
from selenium.webdriver.common.by import By
import re


# Configure Selenium webdriver

driver = webdriver.Chrome()  # Replace with the path to your ChromeDriver executable
driver.get('https://shopee.co.th/nppbox')
thai_button = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button")


thai_button.click()

# Find Item_id the div elements and extract the href values
div_elements = driver.find_elements(By.CLASS_NAME ,"shop-search-result-view__item.col-xs-2-4")

href_values = []
for element in div_elements:
    xxx = element.find_element(By.CSS_SELECTOR ,"a")
    yyy = xxx.get_attribute('href')
    r = re.search(r"i\.(\d+)\.(\d+)", yyy)
    shop_id, item_id = r[1], r[2]
    href_values.append(item_id)
    print(shop_id, item_id )

print(len(href_values))
driver.quit()