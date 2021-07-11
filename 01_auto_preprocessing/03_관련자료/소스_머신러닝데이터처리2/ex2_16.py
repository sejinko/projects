# 파이썬의 csv모듈을 이용한 CSV데이터처리방법

# CSV파일에 있는 필드 데이터가 큰따옴표(")로 둘러 싸인 경우에는
# CSV파일을 분석하기가 어렵다.

# 따라서, 이때에는 csv모듈을 이용하는데
# csv파일을 읽어올때 사용하는 메소드
# csv.reader(파일포인터, delimiter="," , quotechar='"')

# 여기서, delimiter는 구분문자를 지정하고, quotechar는 어떤 기호로 데이터를
# 감싸고 있는지를 지정한다.

# csv파일을 만들때 상용하는 메소드
# csv.writer(파일포인터, delimiter=",", quotechar='"')

import csv, codecs

with codecs.open("test.csv", "w", "euc_kr") as fp:
   writer = csv.writer(fp, delimiter=",", quotechar='"')
   writer.writerow(["상품코드", "상품이름", "가격"])
   writer.writerow(["1", "키보드", 20000])
   writer.writerow(["2", "마우스", 10000])
   writer.writerow(["3", "모니터", 100000])