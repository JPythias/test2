# JawnPythias
# date:04/02/2024
# import requests
# # head将爬虫程序伪装成正常浏览器请求
# head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
# response = requests.get("http://books.toscrape.com/")
# print(response)
# print(response.status_code)
# if response.ok:
#     print(response.text)
# else:
#     print("requests failed")

from bs4 import BeautifulSoup
import requests
content = requests.get("http://books.toscrape.com/").text
soup = BeautifulSoup(content, "html.parser")
all_prices = soup.findAll("p", attrs={"class": "price_color"})
# 根据特定的attr筛选p中信息，返回一个可迭代对象
for price in all_prices:
    print(price.string[2:])# .string方法，返回标签包围的文字
# 寻找书名
all_titles = soup.findAll("h3")
for title in all_titles:
    all_links = title.findAll("a")
    for link in all_links:
        print(link.string)