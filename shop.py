from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://shopee.co.th/nppbox'

# Create a new instance of the Firefox driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    options=options, executable_path="path/to/executable")

# Navigate to the URL
driver.get(url)

# Wait for the page to load and the products to become visible
wait = WebDriverWait(driver, 10)
thai_button = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button")


thai_button.click()
product_elements = wait.until(
    EC.visibility_of_all_elements_located((By.CLASS_NAME, 'O6wiAW')))

# Extract the names of the products
product_names = [product_element.text for product_element in product_elements]

# Close the browser
driver.quit()

# Print the product names
for product_name in product_names:
    print(product_name)
