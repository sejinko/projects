import openpyxl

fileName = "stat_104102.xlsx"

book = openpyxl.load_workbook(fileName)

# 첫번 째 시트를 추출하기
sheet = book.worksheets[0]

#시트의 행을 순서대로 추출하기
excel_record = []

for record in sheet.rows:
  excel_record.append([
    record[0].value,
    record[10].value
  ])

del excel_record[0]
del excel_record[0]
del excel_record[0]
del excel_record[0]
del excel_record[17]
del excel_record[17]

#for data in excel_record:
#  print(data)

for data in excel_record:
   data[1]=data[1].replace(',','')
   data[1]=int(data[1])

# 데이터를 인구순으로 정렬하기 위한 값을 선택
excel_record = sorted(excel_record, key=lambda x:x[1])

for data in excel_record:
  print(data)

#하위 5개의 지역을 추출한다.
print("------------하위 5개지역---------------")

# enumerate메소드는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력 받아 인덱스 값을 포함하는
# enumerate 객체를 리턴하는 메소드이다.

for i, name in enumerate(excel_record):
  if (i >=5): break
  print(i+1, name[0], name[1])





