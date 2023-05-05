from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4
# import pandas as pd
import csv


# driver = webdriver.Chrome(
#     executable_path=r'D:\Work Dev\makewebbkk\scraping shoppee\chromedriver_win32\chromedriver')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(
    options=options, executable_path="path/to/executable")

driver.get('https://shopee.co.th/hairstylishs?fbclid=IwAR3m5WrV-KOiLqfWwUmwqikcFB-jCK_Hk6dCvIqKN0rVwSb-YlFsqqDAC7o#product_list')


# เลือกภาษาไทย
# thai_button = driver.find_element(
#     '/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
thai_button = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button")

thai_button.click()

driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
driver.execute_script("document.body.style.zoom='50%'")
data = driver.page_source  # ดึงข้อมูลจากหน้าเว็บ
soup = bs4.BeautifulSoup(data)  # จัดในรูปแบบ BeautifulSoup
product_name_list = []
product_price_list = []
product_sale_list = []

all_product = soup.find_all('div', {'class': 'yHMIkf kSBby7 AHoc+o'})
print(len(all_product))

for product in all_product:
    # print(product.text)
    product_name_list.append(product.text)

all_product_price = soup.find_all('div', {'class': "gGA8qL xrd7nf"})

for product in all_product_price:
    # print(product.text)
    product_price_list.append(product.text)


all_product_sale = soup.find_all('div', {'class': "BUP03F hynaVT"})

for product in all_product_sale:
    # print(product.text)
    product_sale_list.append(product.text)

# print(product_detail_list)


with open('shopee.txt', 'w', encoding="utf-8") as f:
    for i in range(len(product_name_list)):
        f.write(product_name_list[i]+"," +
                product_price_list[i]+","+product_sale_list[i])
        f.write('\n')