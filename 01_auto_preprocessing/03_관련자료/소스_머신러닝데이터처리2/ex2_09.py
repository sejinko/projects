from bs4 import BeautifulSoup
import urllib.request as req

import os.path

#XML 다운로드
url ="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

fileName = "forecast.xml"

if not os.path.exists(fileName):
 req.urlretrieve(url, fileName)

# 다운받은 파일을 분석하기

xml_data = open(fileName, "r", encoding="utf-8").read()

soup = BeautifulSoup(xml_data, 'html.parser')

# 각 지역 확인하기
info = {}
for location in soup.find_all("location"):
  cityName = location.find("city").string
  weather = location.find("wf").string
  
  if not (weather in info):
    info[weather] = []
  
  info[weather].append(cityName)  

# 지역의 날씨를 구분해서 분류하기

for weather in info.keys():
  print("**", weather)
  for name in info[weather]: 
    print(" - ", name) 
