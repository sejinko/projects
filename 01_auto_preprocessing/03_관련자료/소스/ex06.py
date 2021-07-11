from bs4 import BeautifulSoup

html="""
<html><body>
  <h1 id="title">BeautifulSoup 사용방법</h1>
  <p id="subTitle">스크레이핑 연습하기</p>
  <p>원하는 데이터 추출하기</p>
</body></html>
"""

# html분석하기
soup = BeautifulSoup(html, 'html.parser')


#find() 메서드를 이용한 데이터 추출하기
title = soup.find(id="title")
subTitle = soup.find(id="subTitle")

print("title = " + title.string)
print("subTitle = " +subTitle.string) 