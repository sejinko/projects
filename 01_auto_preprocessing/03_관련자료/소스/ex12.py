from bs4 import BeautifulSoup

fp = open("book.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

#print(soup.select_one("#DataScience").string)
#print(soup.select_one("li#DataScience").string)
#print(soup.select_one("ul > li#DataScience").string)
#print(soup.select_one("#itBook > #DataScience").string)
#print(soup.select_one("#itBook #DataScience").string)
#print(soup.select_one("ul#itBook > li#DataScience").string)
#print(soup.select_one("li[id='DataScience']").string)
#print(soup.select_one("li:nth-of-type(3)").string)

#print(soup.select("li")[2].string)
print(soup.find_all("li")[2].string)
