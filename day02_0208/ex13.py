from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
count = 0
def getLinks(pageUrl):
    global pages
    global count
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    #html = urlopen(f"https://en.wikipedia.org{pageUrl}")
    # 10번라인과 11번 라인은 쌤쌤
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                count += 1
                print(f'[{count}]: {newPage}'.format(count, newPage))
                pages.add(newPage)
                getLinks(newPage)

getLinks('')
# 예외 체크 안해서 중간에 에러남!
# 전체적인 흐름 정도만 해두자