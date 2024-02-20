# JawnPythias
# date:04/02/2024
import requests
from bs4 import BeautifulSoup
# 在网页-检查中寻找header信息，user-agent中的内容
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
for start_num in range(0, 250, 25):
    # 加入header(s)参数！
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    # 状态码为418 I'm a teapot,服务器拒绝服务
    # print(response.status_code)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")# 传入构造函数
    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)
            # 测试
