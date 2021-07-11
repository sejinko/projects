from bs4 import BeautifulSoup
fp = open("fruit_vegetable.html", encoding="utf-8")

soup = BeautifulSoup(fp, "html.parser")

#파프리카 추출
print(soup.select_one("li:nth-of-type(6)").string)

print(soup.select_one("#vegetable > li.red").string)

print(soup.select_one("#vegetable > li:nth-of-type(2)").string)

print(soup.select("#vegetable > li.green")[1].string)


print(soup.select_one("li:nth-of-type(4)").string)
print(soup.select_one("#fruits > li.yellow").string)
print(soup.select("#fruits > li.yellow")[1].string)


print(soup.select_one("li.green").string)
print(soup.select("li.green")[2].string)


#find 메서드를 이용해서 추출하기
condition = {"data-lo":"us", "class":"red"}
print(soup.find("li", condition).string)

print(soup.find(id="vegetable").find("li",condition).string)