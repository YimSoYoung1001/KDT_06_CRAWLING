import requests
import csv
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


'''
크롤링한 내용
- 알라딘 도서 검색창에서 '빅데이터' 검색 => 검색 조건 ('제목', 분야 = '컴퓨터/모바일')
'''

# --------------------------------------------------------------------------------------------------------------------
# 26~50위
# --------------------------------------------------------------------------------------------------------------------


insert_url2 = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&KeyTitle=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&KeyRecentPublish=0&CategorySearch=351%2C0%400&OutStock=0&ViewType=Detail&SortOrder=2&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&KeyLastWord=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&SearchFieldEnable=1&KeyWord=&chkKeyTitle=on&chkKeyAuthor=&chkKeyPublisher=&chkKeyISBN=&chkKeyTag=&chkKeyTOC=&chkKeySubject=&ViewRowCount=25&SuggestKeyWord=&page=2"

html = requests.get(insert_url2)
soup = BeautifulSoup(html.text, 'html.parser')
data_list = soup.find_all('a', {'class':'bo3'})


num = 25
rank = []
book_name = []


for i in range(len(data_list)):
    html_data = data_list[i]
    text_data = html_data.find('b').text
    rank_num = num + i + 1
    print(f"{rank_num}번 책 제목 : {text_data}")
    rank.append(rank_num)
    book_name.append(text_data)

#print(rank)
#print(book_name)

DF_list = []
DF_list.append(rank)
DF_list.append(book_name)

dataframe = pd.DataFrame(DF_list)
dataframe.to_csv('aladin_exam_02')

