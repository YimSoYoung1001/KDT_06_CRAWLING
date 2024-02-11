# ========================================================================================================
# 크롤링 2일차 과제 - 임소영
# ========================================================================================================
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd


# ========================================================================================================
# 51페이지 까지의 각 가게들의 정보 뽑아낸 후 dataframe 생성하여 csv 파일로 저장하기
# ========================================================================================================
'''
분해
(1) 각 페이지 접근하기 (url에서 페이지번호의 숫자만 변경)
(2) 그 페이지에서 정보 수집하기
    수집이 되면 print하기 
(3) 수집된 정보를 csv 파일에 넣기
'''

data_list = []

def cafe():
    global data_list

    count = 1
    for i in range(1, 52):
        html = urlopen(f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store=")
        bs = BeautifulSoup(html, 'html.parser')

        data_all = bs.find('tbody').find_all('tr')

        for data in data_all:
            datas = data.find_all('td')
            area = datas[0].text  # 지역
            store = datas[1].text  # 매장명
            adr = datas[3].text  # 주소
            number = datas[5].text  # 전번
            print(f"[{count:3}]: 매장이름: {store}, 지역: {area}, 주소: {adr}, 전화번호:{number}")
            count += 1

            list = [area, store, adr, number]
            data_list.append(list)


def activate():
    cafe()
    df_data = pd.DataFrame(data_list)  # 데이터 프레임 생성 완료
    df_data.columns = ['매장이름', '지역', '주소', '전화번호']
    #print(df_data)
    print(f"전체 매장 수: {df_data.shape[0]}")
    df_data.to_csv('hollys_branches.csv')
    print(f"hollys_branches.csv 파일 저장 완료")

#activate()



# ========================================================================================================
# 저장된 csv 파일을 읽어서 사용자가 입력한 도시 정보를 검색하고 결과를 출력 (무한반복, quit 입력시 종료)
# ========================================================================================================
'''
분해
(1) csv 파일 읽기
(2) 사용자가 검색할 도시 정보 입력
- quit 입력하면 종료됨
- 입력된 정보가 있는지 확인
- 입력된 정보가 있다면 csv파일에서 찾기
- print
'''


def search_data(word):
    file = pd.read_csv('hollys_branches.csv', usecols=[1, 2, 3, 4])
    # 입력된 도시 이름을 2개의 단어로 분리하기
    word1 = word.split()[0]
    word2 = word.split()[1]

    # 각 단어별로 정규식 객체 생성
    p1 = re.compile(f"{word1}.*")
    p2 = re.compile(f".*{word2}.*")

    # 먼저 word1과 일치하는 정보만 뽑아냄
    list_one = []
    list_one_phone = []
    for n in range(file.shape[0]):
        addr = file.iloc[n]['주소']
        m1 = p1.match(addr)
        if m1 != None:
            list_one.append(addr)
            list_one_phone.append(file.iloc[n]['전화번호'])

    # word1에서 뽑아낸 정보 중 word2와 일치하는 정보만 뽑아내어 print
    if len(list_one) == 0 :
        print('입력한 도시는 검색할 매장이 없습니다.')
    else:
        list_two = []
        list_two_phone = []
        for n in range(len(list_one)):
            m2 = p2.match(list_one[n])
            if m2 != None:
                list_two.append(list_one[n])
                list_two_phone.append(list_one_phone[n])

        print('-'*20)
        print(f"검색된 매장 수: {len(list_two)}")
        print('-'*20)
        for i in range(len(list_two)):
            print(f"[{i+1:3}]: [{list_two[i]}, {list_two_phone[i]}]")
        print('-'*55)


def caffeine():
    start = True

    while start:
        print('-' * 55)
        user_word = input('검색할 매장의 도시 입력하세요: ')
        print('-'*20)
        if user_word == 'quit':
            print('종료합니다')
            print('-' * 55)
            start = False
        else:
            search_data(user_word)

caffeine()







# ========================================================================================================
# ETC (해결과정)
# ========================================================================================================

"""
# 1행에서 데이터를 구하는 법을 알았으니 이제 전체 열에서 찾아보자

count = 1
data_all = bs.find('tbody').find_all('tr')

for data in data_all:
    datas = data.find_all('td')
    area_data = datas[0]  # 지역
    store_data = datas[1]  # 매장명
    adr_data = datas[3]  # 주소
    number_data = datas[5]  # 전번

    print(count)
    print(area_data.text)
    print(store_data.text)
    print(adr_data.text)
    print(number_data.text)

    count += 1
"""



"""
# 일단 1페이지에서 정보를 찾는다고 가정하자
i = 1
html = urlopen(f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store=")
bs = BeautifulSoup(html, 'html.parser')

# 웹사이트 1페이지의 1행 부터 찾아본다고 가정하자
data = bs.find('tbody').find('tr')
datas = data.find_all('td')
print(len(datas))
for d in datas:
    print(d)
    print()

area_data = datas[0]    #지역
store_data = datas[1]   #매장명
adr_data = datas[3]     #주소
number_data = datas[5]  #전번

print(area_data.text)
print(store_data.text)
print(adr_data.text)
print(number_data.text)

# 1페이지의 정보를 얻었으니 다른 페이지에도 똑같이 적용하자
"""