# request.urlopen() 함수 사용하기

# urlretrieve()함수는 파일로 곧바로 저장을 하지만, 

# urlopen()함수는 파일로 바로 저장하지 않고 메모리에 로딩을 한다.



import urllib.request


url = "https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png"
imgPath = "h:\pySrc\daum2.png"


downImg = urllib.request.urlopen(url).read()

# 파일로 저장하는 과정
# f = open("a.txt", "w")
# f.write("테스트로 파일에 내용을 적습니다")
# f.close()

# 위의 과정을 with 문으로 간단하게 표현한다.

# with open("a.txt", "w") as f:
# f.write("테스트로 파일에 내용을 적습니다")


with open(imgPath, "wb") as f:  # w는 쓰기모드, b는 바이너리모드(이미지)
	f.write(downImg)

print("이미지 다운로드 완료")
