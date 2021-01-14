from bs4 import BeautifulSoup
import requests

import sqlite3

response = requests.get("https://www.inside.com.tw/tag/AI")

soup = BeautifulSoup(response.content, "lxml")

cards = soup.find_all("div", {"class": "post_list_item"})

results = []
for card in cards:
    title = card.find("h3", {"class": "post_title"})
    published = card.find("li", {"class": "post_date"})

    print(f"標題：{title.getText().strip()}")
    print(f"日期：{published.getText().strip()}")
    results.append((title.getText().strip(),) + (published.getText().strip(),))

    # print(f"標題：{title.getText().strip()}")
    # print(f"日期：{published.getText().strip()}")


conn = sqlite3.connect("inside.db")  # 連接資料庫
cursor = conn.cursor()
sql = "INSERT INTO post(title, published)VALUES(?, ?)"  # 寫入資料的SQL指令

for result in results:
    cursor.execute(sql, result)  # 執行寫入資料的SQL指令
conn.commit()  # 儲存