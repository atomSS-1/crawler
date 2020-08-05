# urllib.request 를 import 한다
import urllib.request

# url로 요청해 html 파일을 받아온다
fp = urllib.request.urlopen("http://www.python.org")


# beautifulSoup을 import  한다
from bs4 import BeautifulSoup

#beautifulSoup 으로 html을 파싱해서 객체화 한다.
soup = BeautifulSoup(fp, 'html.parser')

print(soup.prettify())
