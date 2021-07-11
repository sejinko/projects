#파이썬으로 json분석하기

import urllib.request as req
import os.path
import json

#json데이터 다운로드하기
url ="https://api.github.com/repositories"
fileName = "rep.json"

if not os.path.exists(url):
  req.urlretrieve(url, fileName)

jsonData = open(fileName, "r", encoding="utf-8").read()

data = json.loads(jsonData)


for dat in data:
  print(dat["name"] + " - "+dat["owner"]["login"])	