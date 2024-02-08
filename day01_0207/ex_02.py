from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page1.html')
#url오픈해서 해당 웹사이트에 적속함

bs = BeautifulSoup(html.read(), 'html.parser')
#바이트 형태로 read한다.
#bequtifulsoup이 우리가 읽을 수 있는 형태로 자동으로 바꿔줌

print(bs)   #전체 html 코드를 가지고 있음
print(bs.h1) #전체인 bs에서 h1부분만 가져옴
print(bs.h1.string) #태그 내부의 문자열만 가져옴

print(bs.title)
print('title:', bs.title.string)