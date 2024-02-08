import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')
m = tel_checker.match('02-123-4567')

print(m.groups())
print('group(): ', m.group())
print('group(0): ', m.group(0))
print('group(1): ', m.group(1))
print('group(2,3): ', m.group(2,3))
print('start(): ', m.start())
print('end(): ', m.end())


print('='*50)

cell_phone = re.compile("^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$")

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))


print('='*50)

lookahead1 = re.search('.+(?=won)', '1000 won')
if(lookahead1 != None):
    print(lookahead1.group())
else:
    print('None')

lookahead2 = re.search('.+(?=am)', '2023-01-26 am 10:00:01')
print(lookahead2)

lookahead3 = re.search('\d{4}(?!-)', '010-1234-5678')
print(lookahead3)


print('='*50)
lookbehind1 = re.search('(?<=am).+', '2023-01-26 am 11:10:01')
print(lookbehind1)
lookbehind2 = re.search('(?<=:).+', 'USD:$51')
print(lookbehind2)
lookbehind3 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 apples.')
print(lookbehind3)


print('='*50)

