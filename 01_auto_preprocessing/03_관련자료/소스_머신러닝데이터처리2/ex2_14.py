#파이썬 데이터를 YAML로 쓰기

#yaml.load(str) : str(YAML)을 파이썬 데이터로 변환
#yaml.dump(value): value(파이썬데이터)를 YAML 형식으로 출력

import yaml

person =[
  {"name":"HongGilDong", "age":"30", "gender":"man"},
  {"name":"KimMiSun", "age":"25", "gender":"woman"},
  {"name":"KangGilDong", "age":"40", "gender":"man"}
]

yaml_data = yaml.dump(person)
print(yaml_data)

print("--------------------")

#YAML데이터를 파이썬 데이터로 변환하기
data = yaml.load(yaml_data)

for person in data:
 print(person["name"])