import json

#json 데이터 

price ={
 "time":"17-01-02",
 "price":{
    "apple": 1000,
    "banana":3000,
    "orange":2000	
  }
}

#json.dumps메소드는 json형식으로 출력한다.
jsonData = json.dumps(price)

print(jsonData)