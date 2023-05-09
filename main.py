from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4
# import pandas as pd
import csv
from selenium.webdriver import FirefoxOptions


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

# driver = webdriver.Chrome(
#     executable_path=r'D:\Work Dev\makewebbkk\scraping shoppee\chromedriver_win32\chromedriver')


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    options=options, executable_path="path/to/executable")

# options = FirefoxOptions()
# options.add_argument("--headless")
# options.binary_location = r''
# # browser = webdriver.Firefox(options=options)

# driver = webdriver.Firefox(executable_path=r'/Users/tharintantayothin/Desktop/Nut/makeWebBkk/Shopee_repo/web-scraping-shopee/geckodriver.exe', options=options)


driver.get('https://shopee.co.th/nppbox')

delay = 3  # seconds
try:
    myElem = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.ID, 'main')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
# เลือกภาษาไทย
# thai_button = driver.find_element(
#     '/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
thai_button = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button")


thai_button.click()
product_name_list = []
product_price_list = []
product_sale_list = []


driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
driver.execute_script("document.body.style.zoom='10%'")
data = driver.page_source  # ดึงข้อมูลจากหน้าเว็บ
soup = bs4.BeautifulSoup(data)  # จัดในรูปแบบ BeautifulSoup


all_product = soup.find_all('div', {'class': 'VptMHK Odl6HA GO6iCi'})
print(len(all_product))

for product in all_product:
    # print(product.text)
    product_name_list.append(product.text)

all_product_price = soup.find_all('div', {'class': "uwSW-2 qljqDx"})

for product in all_product_price:
    # print(product.text)
    product_price_list.append(product.text)


all_product_sale = soup.find_all('div', {'class': "ZjwhVB YpOBv3"})

for product in all_product_sale:
    # print(product.text)
    product_sale_list.append(product.text)

# print(product_detail_list)

# /html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[3]/button[7]


check_btn_next = True
while check_btn_next:
    try:
        # driver.find_element(
        # By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[3]/button[7]")
        btn_next = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[3]/button[7]")
        print(btn_next)
        btn_next.click()
        driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
        driver.execute_script(
            'document.body.style.MozTransformOrigin = "0 0";')
        driver.execute_script("document.body.style.zoom='10%'")
        data = driver.page_source  # ดึงข้อมูลจากหน้าเว็บ
        soup = bs4.BeautifulSoup(data)  # จัดในรูปแบบ BeautifulSoup

        all_product = soup.find_all('div', {'class': 'VptMHK Odl6HA GO6iCi'})
        print(len(all_product))

        for product in all_product:
            # print(product.text)
            product_name_list.append(product.text)

        all_product_price = soup.find_all('div', {'class': "uwSW-2 qljqDx"})

        for product in all_product_price:
            # print(product.text)
            product_price_list.append(product.text)

        all_product_sale = soup.find_all('div', {'class': "ZjwhVB YpOBv3"})

        for product in all_product_sale:
            # print(product.text)
            product_sale_list.append(product.text)
    except NoSuchElementException:
        print("errro")
        check_btn_next = False


header = ['name', 'price', 'sale']
data_csv = []

with open('shopee.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(product_name_list)):
        data_csv = []
        data_csv.append(product_name_list[i])
        data_csv.append(product_price_list[i])
        data_csv.append(product_sale_list[i])
        writer.writerow(data_csv)


# with open('shopee.txt', 'w', encoding="utf-8") as f:
#     for i in range(len(product_name_list)):
#         f.write(product_name_list[i]+"," +
#                 product_price_list[i]+","+product_sale_list[i])
#         f.write('\n')
