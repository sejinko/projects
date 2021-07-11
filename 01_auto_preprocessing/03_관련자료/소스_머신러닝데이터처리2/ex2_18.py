import openpyxl

#엑셀파일 열기
fileName ="stat_106001.xlsx"

# 엑셀 파일을 불러오기 : load_workbook(파일명)
book =openpyxl.load_workbook(fileName)

# 엑셀 파일에서 원하는 sheet를 추출하기
# worksheets[인덱스] : 인덱스가 0, 1 ,2~ 배열처럼 인덱스 사용

sheet = book.worksheets[0] #첫번째 시트를 가져온다.

# 시트의 각 행을 순서대로 추출해보기

excel_data = [] #엑셀의 각 행을 담기위한 리스트

for row in sheet.rows:
  excel_data.append([
   row[0].value,
   row[12].value
  ])

#필요없는 행(헤더) 제거하기
#del excel_data[0]

for data in excel_data:
  print(data)



