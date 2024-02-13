from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.naver.com')
print(driver.current_url)

sleep(2)
driver.close()
driver.quit()


#설치가 정상적으로 되었다면
#자동으로 네이버 웹페이지가 열리고 닫힌다.