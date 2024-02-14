import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#알라딘에서 인공지능 분야 베스트셀러
url = "https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=BestSeller&CID=212364"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

data_list = soup.find_all('a', {'class':'bo'})

url_list = []
for data in data_list:
    #print(data['href'])
    url_list.append(data['href'])
#print(len(url_list))                           #베스트 50위권의 책들의 url을 뽑음






#먼저 1위인 책을 뽑아본다고 가정하자

'''
# 이방식으로 창으로 들어가서 후기에 접근하려고 했으나 실패,,,ㅜ
driver = webdriver.Chrome()
driver.get(insert_url)
print(insert_url)
print('- 위 url 접속 완료 -')


data = driver.find_elements(By.ID,'divPaper15001903')
print(len(data))
for d in data:
    print(d.text)
    print('-'*50)
    
    
driver.close()
driver.quit()
'''

book_url = url_list[0]
html = requests.get(book_url)
soup = BeautifulSoup(html.text, 'html.parser')

#data_list = soup.find_all('div', {'id':"paperShort_15001903"})
#data_list = soup.select('div#divPaper15001903')
#data_list = soup.select('ul > li > div#paperShort_15001903 > div#divPaper15001903')

data_list = soup.find('div', {'class':'hundred_list'})

print(data_list)
#paperShort_15001903
#paperShort_15001903

#paperShort_15001903
#divPaper15001903
