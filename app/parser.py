# parser.py
import requests
import os, json, re
from bs4 import BeautifulSoup

# Location of parser.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# HTTP GET Request
request =  requests.get('https://homepage.sch.ac.kr/sch/05/05010000.jsp')

# GET HTML Source
html = request.text

# Use BeautifulSoup, From HTML Source to Python Object
# First Parameter is HTML Source, Second Parameter is the parser to be used
soup = BeautifulSoup(html, 'html.parser')

# HTML element using CSS Selector
schedules = soup.find_all('a', {'class' : 'schedule'})

for schedule in schedules:
    # 날짜 가져오기 성공
    print(schedule.text)
    # 세부 내용 가져오기 성공
    print(schedule.get('title'))


# GET HTTP Header
header = request.headers

# GET HTTP Status ( 200 : normal )
status = request.status_code

# Check HTTP ( TRUE / FALSE )
is_HTTP_OK = request.ok
