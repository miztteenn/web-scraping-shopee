import json
import re
import requests
import math


url = 'https://shopee.co.th/buyer/4063632/rating?fbclid=IwAR1coO1VteGayciH4-L-WPL1e9RCRxx7dICU8lQcX4vzL778Q26df38IGbg'
user_id = url.split('/')[4]
print(user_id)


url_shop = "https://shopee.co.th/api/v2/user/profile/get/?userid="+str(user_id)

payload_shop = {}
headers_shop = {
    'authority': 'shopee.co.th',
    'accept': '*/*',
    'accept-language': 'th-TH,th;q=0.9,en;q=0.8,ja;q=0.7',
    'if-none-match-': '55b03-87a2546cbc99e79bda7ac88f70f254b6',
    'referer': 'https://shopee.co.th/buyer/4063632/rating?fbclid=IwAR1coO1VteGayciH4-L-WPL1e9RCRxx7dICU8lQcX4vzL778Q26df38IGbg',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'x-api-source': 'pc',
    'x-requested-with': 'XMLHttpRequest',
    'x-shopee-language': 'th',
    # 'Cookie': 'REC_T_ID=49898375-edb9-11ed-941a-5e329f4b8c3b; SPC_F=ZmhBT4i0wHqdcIaRK37w6NFLRzHeak2g; SPC_R_T_ID=pQCPbb4H9aLDKEXUGvv1XG9YS3QxijVgy+USsACVpA54g5bpGAUk/gIcbzY0zdFLwE+WE0qaO6jc80/uFMnWi2u+UjTtuCA/tYHkL2y2MUanYZaNOWhCYEpCmUyIiG0LhYqQjzLTnkO/xQV0kkUnejGt1Ne1dEHoVLLVYzJQL8Y=; SPC_R_T_IV=V3RvdmZBUElITnZUakNJTg==; SPC_SI=zMRIZAAAAABaNzZkYkJJcQamsAAAAAAASThZeEJrenM=; SPC_T_ID=pQCPbb4H9aLDKEXUGvv1XG9YS3QxijVgy+USsACVpA54g5bpGAUk/gIcbzY0zdFLwE+WE0qaO6jc80/uFMnWi2u+UjTtuCA/tYHkL2y2MUanYZaNOWhCYEpCmUyIiG0LhYqQjzLTnkO/xQV0kkUnejGt1Ne1dEHoVLLVYzJQL8Y=; SPC_T_IV=V3RvdmZBUElITnZUakNJTg=='
}

response = requests.request(
    "GET", url_shop, headers=headers_shop, data=payload_shop)
shop_detail = response.json()
shop_detail_id = shop_detail['data']['shopid']


# Get summary review
url_summary = "https://shopee.co.th/api/v2/user/get_rating_summary?userid=" + \
    str(user_id)

payload_summary = {}
headers_summary = {
    'authority': 'shopee.co.th',
    'accept': '*/*',
    'accept-language': 'th-TH,th;q=0.9,en;q=0.8,ja;q=0.7',
    'if-none-match-': '55b03-87a2546cbc99e79bda7ac88f70f254b6',
    'referer': 'https://shopee.co.th/buyer/4063632/rating?fbclid=IwAR1coO1VteGayciH4-L-WPL1e9RCRxx7dICU8lQcX4vzL778Q26df38IGbg',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'x-api-source': 'pc',
    'x-requested-with': 'XMLHttpRequest',
    'x-shopee-language': 'th',
    'Cookie': 'REC_T_ID=49898375-edb9-11ed-941a-5e329f4b8c3b; SPC_F=ZmhBT4i0wHqdcIaRK37w6NFLRzHeak2g; SPC_R_T_ID=pQCPbb4H9aLDKEXUGvv1XG9YS3QxijVgy+USsACVpA54g5bpGAUk/gIcbzY0zdFLwE+WE0qaO6jc80/uFMnWi2u+UjTtuCA/tYHkL2y2MUanYZaNOWhCYEpCmUyIiG0LhYqQjzLTnkO/xQV0kkUnejGt1Ne1dEHoVLLVYzJQL8Y=; SPC_R_T_IV=V3RvdmZBUElITnZUakNJTg==; SPC_SI=zMRIZAAAAABaNzZkYkJJcQamsAAAAAAASThZeEJrenM=; SPC_T_ID=pQCPbb4H9aLDKEXUGvv1XG9YS3QxijVgy+USsACVpA54g5bpGAUk/gIcbzY0zdFLwE+WE0qaO6jc80/uFMnWi2u+UjTtuCA/tYHkL2y2MUanYZaNOWhCYEpCmUyIiG0LhYqQjzLTnkO/xQV0kkUnejGt1Ne1dEHoVLLVYzJQL8Y=; SPC_T_IV=V3RvdmZBUElITnZUakNJTg=='
}

response = requests.request(
    "GET", url_summary, headers=headers_summary, data=payload_summary)

shop_summary = response.json()
review_summary = shop_summary['data']['seller_rating_summary']['rating_total']
# print(shop_summary)
print(review_summary)
# 200/page
page = math.ceil(review_summary/200)
print(page)

# Get Review
url = "https://shopee.co.th/api/v4/seller_operation/get_shop_ratings?limit=6&offset=0&shop_id=" + \
    str(shop_detail_id)+"&user_id="+str(user_id)

payload_review = {}
headers_review = {
    'authority': 'shopee.co.th',
    'accept': '*/*',
    'accept-language': 'th-TH,th;q=0.9,en;q=0.8,ja;q=0.7',
    'referer': 'https://shopee.co.th/buyer/4063632/rating?fbclid=IwAR1coO1VteGayciH4-L-WPL1e9RCRxx7dICU8lQcX4vzL778Q26df38IGbg',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'x-api-source': 'pc',
    'x-requested-with': 'XMLHttpRequest',
    'x-shopee-language': 'th',
    #   'Cookie': 'REC_T_ID=49898375-edb9-11ed-941a-5e329f4b8c3b; SPC_F=ZmhBT4i0wHqdcIaRK37w6NFLRzHeak2g; SPC_R_T_ID=pQCPbb4H9aLDKEXUGvv1XG9YS3QxijVgy+USsACVpA54g5bpGAUk/gIcbzY0zdFLwE+WE0qaO6jc80/uFMnWi2u+UjTtuCA/tYHkL2y2MUanYZaNOWhCYEpCmUyIiG0LhYqQjzLTnkO/xQV0kkUnejGt1Ne1dEHoVLLVYzJQL8Y=; SPC_R_T_IV=V3RvdmZBUElITnZUakNJTg==; SPC_SI=zMRIZAAAAABaNzZkYkJJcQamsAAAAAAASThZeEJrenM=; SPC_T_ID=pQCPbb4H9aLDKEXUGvv1XG9YS3QxijVgy+USsACVpA54g5bpGAUk/gIcbzY0zdFLwE+WE0qaO6jc80/uFMnWi2u+UjTtuCA/tYHkL2y2MUanYZaNOWhCYEpCmUyIiG0LhYqQjzLTnkO/xQV0kkUnejGt1Ne1dEHoVLLVYzJQL8Y=; SPC_T_IV=V3RvdmZBUElITnZUakNJTg=='
}

response = requests.request(
    "GET", url, headers=headers_review, data=payload_review)

shop_review = response.json()
# print(shop_review)


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


# url = "https://shopee.co.th/api/v4/seller_operation/get_shop_ratings?limit=6&offset=22518&shop_id=4062349&user_id=4063632"

# payload = {}
# headers = {
#     'authority': 'shopee.co.th',
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.9',
#     'cookie': '__LOCALE__null=TH; csrftoken=TgbYNeRShWBiFM6TNjE4uXESfP3JX55r; _gcl_au=1.1.1916097180.1683578272; REC_T_ID=33cf12e7-ede0-11ed-93e1-ccbbfedf25ac; SPC_R_T_ID=RmM44YAHSxujY+5xxucLV8X6ZDFYxLMW//6YmKieBW46bvJgH1aWORMsJ3JCVuu+9KCP57MvdmLfqcFPBK04hCU0ZVOJElBY+XYhppODI2UYZZw4+0ErcDBieZN5HanJ0C8YoaistXVbEJBLkMuaCYuQj/JPP8o8CuYnm8d9/X8=; SPC_R_T_IV=ZHJxZGtkR2JqZ2VGZnh4Vw==; SPC_T_ID=RmM44YAHSxujY+5xxucLV8X6ZDFYxLMW//6YmKieBW46bvJgH1aWORMsJ3JCVuu+9KCP57MvdmLfqcFPBK04hCU0ZVOJElBY+XYhppODI2UYZZw4+0ErcDBieZN5HanJ0C8YoaistXVbEJBLkMuaCYuQj/JPP8o8CuYnm8d9/X8=; SPC_T_IV=ZHJxZGtkR2JqZ2VGZnh4Vw==; SPC_SI=n2dHZAAAAABOVGtieFU4MVp5zQAAAAAAd0t6OUJCeDA=; SPC_F=28w9zv0bpN0jxCoiwNMhAYCOH91Caz8h; _fbc=fb.2.1683578272144.IwAR1coO1VteGayciH4-L-WPL1e9RCRxx7dICU8lQcX4vzL778Q26df38IGbg; _fbp=fb.2.1683578272145.964183387; _QPWSDCXHZQA=86aa0d26-7f06-4399-b1a8-ec332f6b0dd8; shopee_webUnique_ccd=KcEIaOMJEGoXsyaDIhSPaQ%3D%3D%7C9EUmh%2BWCwE%2Be8zJ9HrvzQG5eKiZw%2Bkp73VAnOJj6iDwR%2B%2Bflpz%2Fh9UHGqH3a5WrzrnJZV2DMI93ZA4rfX3Esy%2Bkz0tLyIgcH7g%3D%3D%7C6Kbk09b1fZNAHac7%7C06%7C3; ds=45acffe1be48186cdb0b4d995ff450e9; _ga_L4QXS6R7YG=GS1.1.1683578272.1.1.1683578274.58.0.0; language=th; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.3.316184629.1683578273; _gid=GA1.3.2108211066.1683578274; REC_T_ID=49898375-edb9-11ed-941a-5e329f4b8c3b; SPC_F=ZmhBT4i0wHqdcIaRK37w6NFLRzHeak2g; SPC_R_T_ID=RmM44YAHSxujY+5xxucLV8X6ZDFYxLMW//6YmKieBW46bvJgH1aWORMsJ3JCVuu+9KCP57MvdmLfqcFPBK04hCU0ZVOJElBY+XYhppODI2UYZZw4+0ErcDBieZN5HanJ0C8YoaistXVbEJBLkMuaCYuQj/JPP8o8CuYnm8d9/X8=; SPC_R_T_IV=ZHJxZGtkR2JqZ2VGZnh4Vw==; SPC_SI=n2dHZAAAAABOVGtieFU4MVp5zQAAAAAAd0t6OUJCeDA=; SPC_T_ID=RmM44YAHSxujY+5xxucLV8X6ZDFYxLMW//6YmKieBW46bvJgH1aWORMsJ3JCVuu+9KCP57MvdmLfqcFPBK04hCU0ZVOJElBY+XYhppODI2UYZZw4+0ErcDBieZN5HanJ0C8YoaistXVbEJBLkMuaCYuQj/JPP8o8CuYnm8d9/X8=; SPC_T_IV=ZHJxZGtkR2JqZ2VGZnh4Vw==',
#     'if-none-match-': '55b03-cd72a0691d7aaec866c27272656fb28e',
#     'referer': 'https://shopee.co.th/buyer/4063632/rating?fbclid=IwAR1coO1VteGayciH4-L-WPL1e9RCRxx7dICU8lQcX4vzL778Q26df38IGbg',
#     'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
#     'x-api-source': 'pc',
#     'x-requested-with': 'XMLHttpRequest',
#     'x-shopee-language': 'th'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)


url = "https://shopee.vn/-Mã-FASHIONT4MA2-giảm-10K-đơn-50K-Áo-thun-nam-nữ-form-rộng-Yinxx-áo-phông-tay-lỡ-ATL43-i.14746382.6519318270"

r = re.search(r"i\.(\d+)\.(\d+)", url)
shop_id, item_id = r[1], r[2]
ratings_url = "https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid={item_id}&limit=20&offset={offset}&shopid={shop_id}&type=0"
offset = 0
d = {"username": [], "rating": [], "comment": []}
while True:
    data = requests.get(
        ratings_url.format(shop_id=shop_id, item_id=item_id, offset=offset)
    ).json()
    print(ratings_url.format(shop_id=shop_id, item_id=item_id, offset=offset))

    # uncomment this to print all data:
    # print(json.dumps(data, indent=4))
    # leng enumerate tra ket qua duoi dang liet ke
    i = 1
    for i, rating in enumerate(data["data"]["ratings"], 1):
        d["username"].append(rating["author_username"])
        d["rating"].append(rating["rating_star"])
        d["comment"].append(rating["comment"])

        print(rating["author_username"])
        print(rating["rating_star"])
        print(rating["comment"])
        print("-" * 100)

    if i % 20:
        break

    offset += 20
