import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

rating_page = urlopen("https://www.linkedin.com/jobs/search/?currentJobId=3823143379&keywords=%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D&origin=BLENDED_SEARCH_RESULT_NAVIGATION_SEE_ALL&originToLandingJobPostings=3828283938%2C3828936066%2C3499782547")
print(rating_page)

soup = BeautifulSoup(rating_page, "html.parser")
print(soup.prettify())