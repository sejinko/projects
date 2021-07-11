from selenium import webdriver

user = "여러분의 아이디"
myPass = "여러분의 비밀번호"

driver = webdriver.PhantomJS('F:/OneDrive\2020/auto_preprocessing/02_드라이브/phantomjs-2.1.1-windows/bin/phantomjs.exe')
#크롬을 이용할 경우
# driver = webdriver.Chrome('크롬드라이버 경로')
driver.implicitly_wait(3)

url_login = "https://nid.naver.com/nidlogin.login"

driver.get(url_login)
print("로그인 페이지에 접속하였습니다")

#아이디를 입력하는 input 요소를 찾아오기
inputID = driver.find_element_id("id")

#입력박스에 있는 텍스트를 모두 지워준다.
inputID.clear()

#아이디 입력박스에 아이디 입력하기
inputID.send_keys(user)

#비밀번호를 입력하는 input 요소를 찾아오기
inputPW = driver.find_element_id("pw")
inputPW.clear()

#비밀번호 입력박스에 비빌번호를 입력하기
inputPW.send_keys(myPass)


#로그인 버튼을 찾기
loginBtn =driver.find_element_by_css_selector("input.btn_global[type=submit]")

#아이디와 비밀번호를 전송한다.
loginBtn.submit()
print("로그인에 성공하였습니다.")
