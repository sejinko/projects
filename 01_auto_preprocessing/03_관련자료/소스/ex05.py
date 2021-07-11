# BeautifulSoup 라이브러리 사용예

from bs4 import BeautifulSoup


html = """
<html><body>
  <h1>스크레이핑 연습</h1>
  <p>웹페이지를 분석해보기</p>
  <p>데이터 정제하기..</p>	
</body>
</html>
"""

#html 분석하기
soup = BeautifulSoup(html, 'html.parser')


#원하는 요소 접근하기
h1 = soup.html.body.h1 
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

#원하는 요소의 내용을 추출하기
print("h1="+h1.string)
print("p="+p1.string)
print("p="+p2.string)