# 학사 일정 파싱 모듈

from pytz import timezone
from bs4 import BeautifulSoup
import requests, os, re
import json

def parser() :

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

	schedule_day = []
	schedule_list = []

	for schedule in schedules:
		# 날짜 가져오기
		schedule_day.append(schedule.text)
		# 세부 내용 가져오기
		schedule_list.append(schedule.get('title'))

	idx = 0

	result_message = '의 학사일정\n'

	for schedule in schedule_day :
		schedule_message = '\n[' + str(schedule) + '일 일정]\n' + '· ' + schedule_list[idx]
		result_message = str(result_message) + schedule_message
		idx += 1

	# GET HTTP Header
	header = request.headers

	# GET HTTP Status ( 200 : normal )
	status = request.status_code

	# Check HTTP ( TRUE / FALSE )
	is_HTTP_OK = request.ok

	return result_message
