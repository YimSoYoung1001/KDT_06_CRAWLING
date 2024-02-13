from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.coffeebeankorea.com/store/store.asp")

driver.execute_script('storePop2(1)')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify()) #HTML소스를 보기 좋게 출력


store_names = soup.select('div.store_txt > p.name > span')
store_name_list = []
for name in store_names:
    store_name_list.append(name.get_text())

print('매장 개수: ', len(store_name_list))
print(store_name_list)

store_addresses = soup.select('p.addr > span')
store_address_list = []
for addr in store_addresses:
    print(addr.get_text())
    store_address_list.append(addr.get_text())
driver.quit()
