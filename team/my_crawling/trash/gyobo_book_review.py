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
'''
#교보문고에서 도서검색에서 AI 한거
url = "https://search.kyobobook.co.kr/search?keyword=ai&gbCode=TOT&target=total"

html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')


data_list = soup.find_all('a', {'class':'prod_info'})

#1페이지의 20개의 도서의 url 목록을 리스트에 저장함
url_list = []
for data in data_list[0:20]:
    #print(data['href'])
    #print('-'*50)
    url_list.append(data['href'])
#print(len(url_list))


'''
#먼저 1번 책부터 접근하다고 가정해보자
i = 0
book_url = url_list[i]
print(f"{i+1:3}위 책 : {book_url}")

html = requests.get(book_url)
book_soup = BeautifulSoup(html.text, 'html.parser')

#info_data = book_soup.find('div', {'class':'info_text'})
info_data = book_soup.select("div.info_text")

print(info_data)

print(info_data)
for data in info_data:
    print(data.text)