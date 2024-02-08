from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, 'html.parser')

# 자손: descendants
desc = soup.find('table', {'id': 'giftList'}).descendants
list_desc = list(desc)
print('descendants 개수 : ', len(list_desc))

for tag in list_desc:
    print(tag)

print('='*50)
# next_siblings 속성
for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)

