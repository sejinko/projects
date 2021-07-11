﻿from bs4 import BeautifulSoup
import urllib.request as req

#웹문서 가져오기
url = "http://info.finance.naver.com/marketindex/"

res = req.urlopen(url)


soup = BeautifulSoup(res, 'html.parser')

price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)
