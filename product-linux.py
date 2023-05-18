from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import bs4

# import pandas as pd
import csv
import time
import io
import re

from flask import Flask, request, send_file, make_response, Response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


def thai_number_to_int(value):
    if value != "":
        thai_numbers = {
            "ศูนย์": 0,
            "หนึ่ง": 1,
            "สอง": 2,
            "สาม": 3,
            "สี่": 4,
            "ห้า": 5,
            "หก": 6,
            "เจ็ด": 7,
            "แปด": 8,
            "เก้า": 9,
            "สิบ": 10,
            "ร้อย": 100,
            "พัน": 1000,
            "หมื่น": 10000,
            "แสน": 100000,
            "ล้าน": 1000000,
        }
        int_value = 0
        # Split the input value into its components
        if value.find(".") > 0:
            intNum, point = value.split(".")
            value = "." + point
            if "พัน" in value:
                int_value = (
                    int(intNum) * thai_numbers["พัน"]
                    + float(value.replace("พัน", "")) * thai_numbers["พัน"]
                )
            elif "หมื่น" in value:
                int_value = (
                    int(intNum) * thai_numbers["หมื่น"]
                    + float(value.replace("หมื่น", "")) * thai_numbers["หมื่น"]
                )
            elif "แสน" in value:
                int_value = (
                    int(intNum) * thai_numbers["แสน"]
                    + float(value.replace("แสน", "")) * thai_numbers["แสน"]
                )
            elif "ล้าน" in value:
                int_value = (
                    int(intNum) * thai_numbers["ล้าน"]
                    + float(value.replace("ล้าน", "")) * thai_numbers["ล้าน"]
                )

        else:
            if "พัน" in value:
                int_value = int(value.replace("พัน", "")) * thai_numbers["พัน"]
            elif "หมื่น" in value:
                int_value = int(value.replace("หมื่น", "")) * thai_numbers["หมื่น"]
            elif "แสน" in value:
                int_value = int(value.replace("แสน", "")) * thai_numbers["แสน"]
            elif "ล้าน" in value:
                int_value = int(value.replace("ล้าน", "")) * thai_numbers["ล้าน"]
            else:
                int_value = value
        return int_value
    else:
        return 0


# driver = webdriver.Chrome(
#     executable_path=r'D:\Work Dev\makewebbkk\scraping shoppee\chromedriver_win32\chromedriver')


@app.route("/", methods=["GET"])
def home():
    return "Hello word"


@app.route("/product", methods=["GET"])
def getData():
    link = request.args.get("link")
    product = request.args.get("product")
    price = request.args.get("price")
    sale = request.args.get("sale")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get(link)

    delay = 3  # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, "main"))
        )
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    # เลือกภาษาไทย
    thai_button = driver.find_element(
        By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button"
    )

    thai_button.click()


    product_id_list = []
    product_name_list = []
    product_price_list = []
    product_sale_list = []

    driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
    driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
    driver.execute_script("document.body.style.zoom='10%'")
    data = driver.page_source  # ดึงข้อมูลจากหน้าเว็บ
    soup = bs4.BeautifulSoup(data)  # จัดในรูปแบบ BeautifulSoup
    time.sleep(6)
    total_pages_element = int(
        soup.find("span", {"class": "shopee-mini-page-controller__total"}).text
    )
    print(total_pages_element)

    check_btn_next = 0
    while check_btn_next < total_pages_element:
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        # driver = webdriver.Chrome(
        #     options=options, executable_path="path/to/executable")
        page_url = f"{link}?page={check_btn_next}"
        print(f"https://shopee.co.th/nppbox?page={check_btn_next}")
        driver.get(page_url)
        time.sleep(5)
        try:
            myElem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.ID, "main"))
            )
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")


        # Find Item_id the div elements and extract the href values
        if check_btn_next < total_pages_element :
            # print("if")
            div_elements = driver.find_elements(By.CLASS_NAME ,"shop-search-result-view__item.col-xs-2-4")
            for element in div_elements:
                xxx = element.find_element(By.CSS_SELECTOR ,"a")
                yyy = xxx.get_attribute('href')
                r = re.search(r"i\.(\d+)\.(\d+)", yyy)
                shop_id, item_id = r[1], r[2]
                product_id_list.append(item_id)
                # print(shop_id, item_id )
            print(len(div_elements))

        if check_btn_next == total_pages_element-1 :
            # print("else")
            div_elements = driver.find_elements(By.CLASS_NAME ,"shop-collection-view__item.col-xs-2-4")
            for element in div_elements:
                xxx = element.find_element(By.CSS_SELECTOR ,"a")
                yyy = xxx.get_attribute('href')
                r = re.search(r"i\.(\d+)\.(\d+)", yyy)
                shop_id, item_id = r[1], r[2]
                product_id_list.append(item_id)
            print(len(div_elements))

        driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
        driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
        driver.execute_script("document.body.style.zoom='5%'")
        time.sleep(5)
        data = driver.page_source  # ดึงข้อมูลจากหน้าเว็บ
        soup = bs4.BeautifulSoup(data)  # จัดในรูปแบบ BeautifulSoup

        all_product = soup.find_all("div", {"class": product})
        all_product_price = soup.find_all("div", {"class": price})
        all_product_sale = soup.find_all("div", {"class": sale})

        # print(all_product_sale)
        print(len(all_product))
        print(len(all_product_price))
        print(len(all_product_sale))

        for x in range(len(all_product)):
            if x > 5:
                product_name_list.append(all_product[x].text)

        for x in range(len(all_product_price)):
            if x > 5:
                product_price_list.append(all_product_price[x].text)
        for x in range(len(all_product_sale)):
            if x > 5:
                product_sale_list.append(all_product_sale[x].text)

        check_btn_next += 1

    driver.quit()
    print(len(product_id_list))
    print(len(product_name_list))
    print(len(product_price_list))
    print(len(product_sale_list))
    header = ["product_id","name", "price", "sale"]
    data_csv = []

    with open("shopee.csv", "w", encoding="UTF8") as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        for i in range(len(product_name_list)):
            data_csv = []
            data_csv.append(product_id_list[i])
            data_csv.append(product_name_list[i])
            data_csv.append(product_price_list[i].replace("฿", ""))
            data_csv.append(
                thai_number_to_int(
                    (product_sale_list[i].replace("ขายแล้ว ", "").replace(" ชิ้น", ""))
                )
            )
            writer.writerow(data_csv)

    # return send_file('shopee.csv',mimetype='text/csv',as_attachment=True, ="data.csv")
    # output = io.StringIO()
    # writer2 = csv.writer(output)
    # line = ["product_id","name,price,sale"]
    # writer2.writerow(line)

    # for i in range(len(product_name_list)):
    #     line = [
    #         product_id_list[i] 
    #         + ","
    #         + product_name_list[i]
    #         + ","
    #         + product_price_list[i].replace("฿", "")
    #         + ","
    #         + str(
    #             thai_number_to_int(
    #                 (product_sale_list[i].replace("ขายแล้ว ", "").replace(" ชิ้น", ""))
    #             )
    #         )
    #     ]
    #     writer2.writerow(line)

    # return Response(
    #     output,
    #     mimetype="text/csv",
    #     headers={"Content-Disposition": "attachment;filename=report.csv"},
    # )
    return send_file("shopee.csv", as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
