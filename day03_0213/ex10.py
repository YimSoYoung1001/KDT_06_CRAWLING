import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://google.com')

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Python')
search_box.submit()

time.sleep(3)
search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
print(len(search_results), '\n')  #검색버튼누름

for result in search_results:
    title_element = result.find_element(By.CSS_SELECTOR, 'h3')
    title = title_element.text.strip()
    print(f"{title}")

driver.quit()