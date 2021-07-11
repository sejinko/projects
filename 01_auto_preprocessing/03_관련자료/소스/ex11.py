from bs4 import BeautifulSoup
import urllib.request as req

url="https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%ED%95%9C%EC%9A%A9%EC%9A%B4"
res = req.urlopen(url)
soup = BeautifulSoup(res,'html.parser')

list = soup.select("#mw-content-text > div > ul > li > a")

for a in list:
  name = a.string
  print("*", name)


