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


while True:

    url = "https://finance.naver.com/sise/sise_market_sum.naver"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    data_list = soup.find_all('tr', {'onmouseout':"mouseOut(this)"})

    company = []
    company_urls = []

    for data in data_list[:10]:
        #print(data)
        name = data.find('a', {'class':'tltle'})
        #print(name)
        url_1 = 'https://finance.naver.com/'
        url_2 = name['href']
        cp_url = url_1 + url_2        #각 회사별 주식창 url 생성
        company.append(name.text)
        company_urls.append(cp_url)


    print('-'*40)
    print("[네이버 코스피 상위 10대 기업 목록 ]")
    print('-'*40)
    for i in range(10):
        print(f"[{i+1:2}] {company[i]}")

    user_num = int(input('주가를 검색할 기업의 번호를 입력하세요 (-1: 종료): '))

    #driver = webdriver.Chrome()

    if user_num == -1 :
        print('프로그램 종료합니다')
        print()
        break

    elif 1<= user_num <=10:
        driver = webdriver.Chrome()
        insert_url = company_urls[user_num - 1]
        driver.get(insert_url)

        # 회사별 주식 URL
        print(insert_url)

        # 뽑을 내용 : 종목명
        print(f"종목명: {company[user_num -1]}")

        # 뽑을 내용 : 종목코드
        value = driver.find_element(By.CLASS_NAME, 'code')
        print(f"종목코드: {value.text}")

        # 뽑을 내용 : 현재가, 전일가, 시가, 고가, 저가
        data = driver.find_elements(By. TAG_NAME, 'em')
        now = data[10].text
        yesterday = data[13].text
        high = data[14].text
        siga = data[17].text
        low = data[18].text

        print_dict = {'현재가':now, '전일가':yesterday, '시가':siga, '고가':high, '저가': low}

        for k, v in print_dict.items():
            stringlist = v.split('\n')
            value_str = ""
            for str in stringlist:
                value_str += str
            print(f"{k} : {value_str}")

        print()
        driver.close()
        driver.quit()

    else:
        print('종료를 원하시면 -1을, 혹은 1~10의 범위의 정수를 입력하세요')












# ------------------------------------------------------------------------------------------------------------------
# 해결 과정
# ------------------------------------------------------------------------------------------------------------------

'''
#현재가
value = driver.find_elements(By.CLASS_NAME, 'no_up')
value_now = value[0].text
stringlist = value_now.split('\n')
value_str = ""
for str in stringlist:
    value_str += str
#print(value_str)


#전일가
data = driver.find_elements(By. TAG_NAME, 'em')
i = 0

for d in data:
    print(i)
    print(d.text)
    print('-'*30)
    i += 1

now = data[10].text
yesterday = data[13].text
high = data[14].text
siga = data[17].text
low = data[18].text

print_list = [now, yesterday, high, siga, low]


for data in print_list:
    stringlist = data.split('\n')
    value_str = ""
    for str in stringlist:
        value_str += str
    print(value_str)
'''