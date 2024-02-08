import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def scraping_use_find(html):
    soup = BeautifulSoup(html.read(), 'html.parser')

    data_list = soup.find('ul', {'id':{'seven-day-forecast-list'}})
    data = data_list.find_all('li', {'class':{'forecast-tombstone'}})
    length = len(data)

    print(f"총 tomestone-container 검색 개수 : {length}")

    # 일단 해당 스택만 덩어리로 가져옴
    for i in range(length):
        data_period = data[i].find_all('p', {'class':'period-name'})
        data_weather = data[i].find_all('p', {'class': 'short-desc'})
        if i == 0 :
            data_temp = '없음'
        else:
            if i % 2 == 1 :
                data_temp = data[i].find_all('p', {'class':'temp temp-low'})
            else :
                data_temp = data[i].find_all('p', {'class':'temp temp-high'})
        data_img = data[i].find_all('img', {'class':'forecast-icon'})

        #print(data_period, data_weather, data_temp, sep = '\n')
        #print()
        #print(data_img)
        #print('='*50)

        # 여기서 글자만 뽑아온다
        print('-'*50)
        print(f"[Period]: {data_period[0].text}")
        print(f"[Short desc]: {data_weather[0].text}")
        if data_temp == '없음':
            print(f"[Temperature]: 없음")
        else:
            print(f"[Temperature]: {data_temp[0].text}")
        print(f"[Image desc]: {data_img[0]['alt']}")

        #print(data_img[0].text)


html_example = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
print('National Weather Service Scraping')
print('[find 함수 사용]')
scraping_use_find(html_example)