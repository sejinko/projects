import requests

# 보통 웹API의 결과는 JSON형식이나 XML형식 리턴을 한다. openweathermap에서는 JSON 형식으로 리턴한다.
# 따라서, JSON형식의 데이터를 파이썬 데이터형식으로 변환해줘야 하는데 이때 json모듈이 필요함.
import json 

# API키를 지정한다. 여러분들의 API키를 사용
apikey="여러분의 발급 받은 키"

city_list = ["Seoul,KR", "Tokyo,JP", "New York,US"]

#API 지정
api="http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 켈빈 온도를 섭씨 온도로 변환하는 함수
k2C = lambda k: k - 273.15

#각 도시의 정보를 추출하기
for name in city_list:
  
#API의 URL 구성하기
 url = api.format(city=name, key=apikey)

#API요청을 보내 날씨 정보를 가져오기
 res = requests.get(url)

#JSON형식의 데이터를 파이썬형으로 변환한다.
 data = json.loads(res.text)

#결과를 출력해보기

 print("** 도시 = ", data["name"])
 print("| 날씨 = ", data["weather"][0]["description"])
 print("| 최저 기온 =", k2C(data["main"]["temp_min"]))
 print("| 최고 기온 =", k2C(data["main"]["temp_max"]))
 print("| 습도 = ", data["main"]["humidity"])
 print("| 기압 = ", data["main"]["pressure"])
 print("| 풍향 = ", data["wind"]["deg"])
 print("| 풍속 = ", data["wind"]["speed"])
 print(" ")













