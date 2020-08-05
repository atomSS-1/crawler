# html 예

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

# beautifulSoup을 import  한다
from bs4 import BeautifulSoup

#beautifulSoup 으로 html을 파싱해서 객체화 한다.
soup = BeautifulSoup(html_doc, 'html.parser')

# prettify() 함수는 html 을 줄바꿈 형태로 formatting 해서 보여준다

print(soup.prettify())

# 줄바꿈
print()
# html title 태그를 파싱한다.
print('html title 태그 : ', soup.title)

# 줄바꿈
print()
# html body 태그를 파싱한다.
print('html title body 태그 : ', soup.body)

# 줄바꿈
print()
# html body 태그의 첫번째 a 태그를 파싱한다.
print('html title a 태그 : ', soup.body.a)


# 줄바꿈
print()
# html body 태그의 첫번째 모든 a 태그를 파싱한다.

print(soup.find_all('a'))

# 줄바꿈
print()
# html body 태그의 첫번째 모든 a 태그의 모든 href url을 리스트 형태로 파싱한다.
i = 0 # i 초기화
for a_tag in soup.find_all('a'):
    i = i + 1
    print('url', i, '번째', a_tag['href'])
