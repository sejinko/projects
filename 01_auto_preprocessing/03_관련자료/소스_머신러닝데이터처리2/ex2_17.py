import csv, codecs

fileName = "test.csv"
fp = codecs.open(fileName, "r", "euc_kr")


reader = csv.reader(fp, delimiter=",", quotechar='"')

for field in reader:
  print(field[1], field[2])