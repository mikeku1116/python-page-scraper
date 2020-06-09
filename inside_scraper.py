from bs4 import BeautifulSoup
import requests

for page in range(1, 4):  # 執行1~3頁

    # 連結網站
    response = requests.get(
        "https://www.inside.com.tw/tag/AI?page=" + str(page))

    # HTML原始碼解析
    soup = BeautifulSoup(response.text, "html.parser")

    # 取得所有class為post_title的<h3>
    titles = soup.find_all("h3", {"class": "post_title"})

    print(f"====================第{str(page)}頁====================")
    for title in titles:
        print(title.select_one("a").getText())  # 取得連結的標題文字
