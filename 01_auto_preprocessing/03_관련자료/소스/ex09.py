# CSS 선택자 사용하기
# BeautifulSoup.select_one(선택자) : CSS선택자로 요소 하나를 추출한다.
# BeautifulSoup.select(선택자) : CSS선택자로 요소 여러개를 리스트로 추출한다.

from bs4 import BeautifulSoup


# 분석 대상 HTML문서
html ="""
<html><body>
  <div id="LecList">
    <h1>데이터과학</h1>
  </div>
  <div id="lecture">
    <h1>빅데이터 분석 강좌</h1>
    <ul class="subject">
        <li>R언어 강좌</li>
        <li>머신러닝을 위한 데이터처리</li>
        <li>파이썬으로 익히는 딥러닝이론</li> 
    </ul>
    
  </div>	
</body></html>
"""

#HTML 분석하기
soup = BeautifulSoup(html, 'html.parser')

# CSS 쿼리로 데이터 추출하기
h1 = soup.select_one("div#lecture > h1").string
print("h1=", h1)

subjects = soup.select("div#lecture > ul.subject > li")
for li in subjects:
  print("li =", li.string)