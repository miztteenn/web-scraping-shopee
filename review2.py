from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4
# import pandas as pd
import csv
from selenium.webdriver import FirefoxOptions
import time


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


driver.get('https://shopee.co.th/buyer/4063632/rating?fbclid=IwAR1coO1VteGayciH4-L-WPL1e9RCRxx7dICU8lQcX4vzL778Q26df38IGbg')


# เลือกภาษาไทย
# thai_button = driver.find_element(
#     '/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
thai_button = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button")

thai_button.click()

next_btn = driver.find_element(
    By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[2]/section[1]/div/div/div[2]/div[2]/button[8]')
i = 1
while i <= 10:
    next_btn.click()
    i += 1


driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
driver.execute_script("document.body.style.zoom='50%'")
# data = driver.page_source  # ดึงข้อมูลจากหน้าเว็บ
# soup = bs4.BeautifulSoup(data)  # จัดในรูปแบบ BeautifulSoup
# product_name_list = []
# product_price_list = []
# product_sale_list = []
# # all_product = soup.find_all(
# #     'div', {'class': 'shopee-product-rating__content'})
# all_product = soup.find_all(
#     "a", {"class": "shopee-product-rating__author-name"})

# print(len(all_product))
# print(all_product)
# for product in all_product:
#     print(product.text)
#     product_name_list.append(product.text)

# all_product_price = soup.find_all('div', {'class': "gGA8qL xrd7nf"})

# for product in all_product_price:
#     # print(product.text)
#     product_price_list.append(product.text)


# all_product_sale = soup.find_all('div', {'class': "BUP03F hynaVT"})

# for product in all_product_sale:
#     # print(product.text)
#     product_sale_list.append(product.text)

# print(product_detail_list)


# with open('review.txt', 'w', encoding="utf-8") as f:
#     for i in range(len(product_name_list)):
#         # f.write(product_name_list[i]+"," +
#         #         product_price_list[i]+","+product_sale_list[i])
#         f.write(product_name_list[i])
#         f.write('\n')


# header = ['name', 'price', 'sale']
# data_csv = []

# with open('shopee.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     for i in range(len(product_name_list)):
#         data_csv = []
#         data_csv.append(product_name_list[i])
#         data_csv.append(product_price_list[i])
#         data_csv.append(product_sale_list[i])
#         writer.writerow(data_csv)
