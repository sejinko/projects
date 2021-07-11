import openpyxl

fileName = "stat_104102.xlsx"
book = openpyxl.load_workbook(fileName)

sheet = book.active #활성화되어있는 시트를 가져온다.

# 서울과 계에 해당하는 값을 제외한 인구수 합산하기

for i in range(0, 10):
  totalValue = sheet[str(chr(i+66))+"4"].value.replace(',','')
  total = int(totalValue)
  seoulValue= sheet[str(chr(i+66))+"5"].value.replace(',','')
  seoul = int(seoulValue)

  result = format(total-seoul, ',')

  print("서울을 제외한 인구 : ", result)

# 필요없는 데이터 지우기
  sheet[str(chr(65))+"22"].value="서울을 제외한 인구합계"  
  sheet[str(chr(i+65))+"23"].value=""
   
  sheet[str(chr(i+66))+"22"].value=result  
  cell = sheet[str(chr(i+66))+"22"]

  cell.font = openpyxl.styles.Font(size=14, color="FF0000")

# 엑셀 파일에 결과를 쓰기    
fileName="excel_Res.xlsx"
book.save(fileName)
print("파일이 저장되었습니다!!")

 



