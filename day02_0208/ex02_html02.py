from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

namelist = soup.find_all('span', {'class': 'green'})
for name in namelist:
    print(name.string)

princelist = soup.find_all(string = 'the prince')  #특정 단어를 검색함 (the prince)
print(princelist)
print('the prince count: ', len(princelist))  #특정단어가 총 7개 나왔음