# 텍스트 데이터 가져오기

import requests
resData = requests.get("http://api.aoikujira.com/time/get.php")

#텍스트 형식으로 추출하기
txt = resData.text

print(txt)

# 바이너리 형식으로 데이터 추출하기
bin =resData.content
print(bin)

