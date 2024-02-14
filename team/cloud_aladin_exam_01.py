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

file = "aladin_exam_01"

df = pd.read_csv(file)
df1 = df.transpose()
print(df1)
print(df1.columns)