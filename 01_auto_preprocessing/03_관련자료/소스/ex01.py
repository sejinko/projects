# 웹상의 정보를 추출하기 위한 라이브러리 불러오기
# urllib 라이브러리 : Http나 FTP를 사용해서 데이터를 다운로드 할 때 사용하는 라이브러리
# urllib : URL을 다루는 모듈을 모아 놓은 패키지 
# urllib패키지에 있는 모듈 중에서 request모듈을 이용하는데 request모듈안에 urlretrieve()함수를 사용한다.


#파이썬에서 모듈을 불러올 때는 import 명령을 사용한다.

import urllib.request

url = "https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png"
imgName = "h:\pySrc\daum.png"


urllib.request.urlretrieve(url, imgName) #urlretrieve(URL, 저장할파일경로)
print("다운로드 완료 되었습니다")