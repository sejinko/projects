# 웹스크레이핑의 순서
# 1. 웹스크레이핑 대상 설정 : URL 할당
# 2. 웹 문서 추출 : htmlParse()
# 3. 특정태그의 데이터 추출 : xpathSApply()
# 4. 데이터 정제(불필요한 특수문자, 공백문자 제거) : gsub('\n','',name)
#                             name에서 '\n' 문자를 제거하겠다는 명령 
# 5. 데이터프레임 만들기 : data.frame()
# 6. 데이터를 정렬


# XML 패키지 : XML문서나 Html문서를 만들거나 읽을 때 사용한다.
#            : XPath(XML Path Language) 기술을 포함한다.

install.packages("XML")

library(XML)
url<- "http://www.coupang.com/np/categories/197400?listSize=60&brand=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page=1&channel=user&fromComponent=Y&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=197300&rating=0"
doc <- htmlParse(url, encoding ="UTF-8")

# //는 중간단계를 건너뛴다.
prodName <- xpathSApply(doc,"//ul[@id='productList']//div[@class='name']",xmlValue)

prodName

prodName <-gsub('\n','',prodName)
prodName


prodName <-gsub(' ','',prodName)
prodName

price <- xpathSApply(doc,"//ul[@id='productList']//strong[@class='price-value']",xmlValue)
price


df <- data.frame(상품명=prodName, 가격=price)
df

df$상품명 <-format(df$상품명, justify="left")
df

df$가격 <-format(df$가격, justify="right")
df
