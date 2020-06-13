from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


options = Options()
options.add_argument("--disable-notifications")  # 取消所有的alert彈出視窗

browser = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=options)

browser.get("https://rent.591.com.tw/")

area = browser.find_element_by_id("area-box-close")
area.click()  # 取消「選擇縣市」的div視窗

for page in range(1, 3):  # 執行1~2頁

    soup = BeautifulSoup(browser.page_source, "html.parser")

    # 取得所有class為pull-left infoContent的<li>標籤
    elements = soup.find_all("li", {"class": "pull-left infoContent"})

    print(f"==========第{str(page)}頁==========")
    for element in elements:
        # 取得<li>標籤下的<h3>標籤，再取得<h3>標籤下的<a>標籤文字，並且去掉空白
        title = element.find("h3").find("a").getText().strip()
        print(title)

    page_next = browser.find_element_by_class_name("pageNext")
    page_next.click()  # 點擊下一頁按鈕

    time.sleep(10)  # 暫停10秒
