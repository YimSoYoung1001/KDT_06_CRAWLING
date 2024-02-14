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


book_url = "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=333998986"
#book_url = 'https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=326285388'
# html = requests.get(book_url)
html = urlopen(book_url)
book_soup = BeautifulSoup(html, 'html.parser')


info_data = book_soup.find("meta", {'property' : 'og:description'})
info_data2 = info_data.find('meta', {'property':'og:description'})

# print(info_data)

print(info_data2)

list1 = []

for i in info_data:
    list1.append(i)

print(list1[3])


print(len(list1))
for i in range(len(list1)):
    print(f"인덱스 번호 => {i}번")
    print(list1[i])