# YAML 데이터를 파이썬으로 읽어오기
import yaml

#yaml 데이터 정의

yaml_data = """
date: 2017-01-01 
productList:
   - 
     id: 100
     name: banana
     color: yellow
     price: 1000
   -
     id: 200
     name: orange
     color: orange
     price: 700
   -
     id: 300
     name: apple
     color: red
     price: 1200
"""

data = yaml.load(yaml_data)

#이름과 컬러를 출력
for prod in data["productList"]:
  print(prod["name"], prod["price"])