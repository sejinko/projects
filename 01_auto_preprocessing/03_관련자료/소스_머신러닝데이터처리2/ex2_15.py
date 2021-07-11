import codecs

fileName = "prod_list.csv"
csv = codecs.open(fileName, "r", "euc_kr").read()

data = []
records = csv.split("\r\n") #\r:CR \n:LF(new line)

for rec in records:
  if rec =="": continue
  fields = rec.split(",")
  data.append(fields)

for field in data:
  print(field[1], field[2])