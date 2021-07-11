# 파이썬에서 바이너리 파일 만들기

filename = "a.bin" #bin :binary
value = 100

#파일 쓰기모드로 열어서 만들기

with open(filename, "wb") as f : #wb : write binary약자
 f.write(bytearray([value]))