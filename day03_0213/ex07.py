from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com')

print(driver.current_url) 
print(driver.title) 
print(driver.page_source) #페이지의 전체 소스를 가져옴

driver.implicitly_wait(time_to_wait=5)
driver.close()
driver.quit()
