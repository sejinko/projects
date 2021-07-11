from bs4 import BeautifulSoup

html = """
  <html>
    <body>
       <ul>
          <li><a href="http://www.naver.com">네이버</a></li>
          <li><a href="http://www.daum.net">다음</a></li>
       </ul>
    </body>	
  </html>
"""

#html 분석하기
soup = BeautifulSoup(html, 'html.parser')

#find_all() 메서드를 사용
links = soup.find_all("a")


for a in links:
   href = a.attrs['href']
   text = a.string
   print(text, ">", href)