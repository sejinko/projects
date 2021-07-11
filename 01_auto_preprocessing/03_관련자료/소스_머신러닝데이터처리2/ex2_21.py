import pandas as pd

fileName = "stat_104102.xlsx"
sheet_name = "Sheet0"

book = pd.read_excel(fileName, sheetname=sheet_name, header=2)

book=book.sort_values(by="2016", ascending=False)

print(book)