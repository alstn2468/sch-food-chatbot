from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.my_module.repdic import *
from app.my_module.scheduleparser import *
from app.my_module.stringformat import *
from app.my_module.process import *
from app.my_module.button import *
from pytz import timezone
import requests, datetime, json

# 데이터 목록
# menu/SnowFlowerOne.json     향설1 생활관
# menu/SnowFlowerTwo.json     향설2 생활관
# menu/SnowFlowerThree.json   향설3 생활관
# menu/StudentUnion.json      학생 회관
# menu/FacultyRestaurant.json 교직원 식당

def keyboard(request) :

	return JsonResponse (
		{
			'type' : 'buttons',
			'buttons' : basic_button
		}
	)

@csrf_exempt
def answer(request) :

	json_str = (request.body).decode('utf-8')
	received_json = json.loads(json_str)
	content_name = received_json['content']
	type_name = received_json['type']
	user_key = received_json['user_key']
	
	# 오늘
	today = datetime.datetime.now()
	today_info = today.strftime('%Y년 %m월 %d일')
	today_weekday = today.weekday()

	if content_name == '학식' :

		return food_info_process()

	elif content_name == '메뉴' :

		return food_sel_process()

	elif content_name == '이용 시간' :

		send_message = select_else_button.format(content_name) + using_time

		return re_process(send_message)

	elif content_name == '향설1 생활관' :

		try :
			with open('app/menu/SnowFlowerOne.json', 'rb') as f :
				datas = json.load(f)

			if today_weekday == 0 :
				meal = str(datas.get('월'))
				meal = char_replace(meal)

			elif today_weekday == 1 :
				meal = str(datas.get('화'))
				meal = char_replace(meal)

			elif today_weekday == 2 :
				meal = str(datas.get('수'))
				meal = char_replace(meal)

			elif today_weekday == 3 :
				meal = str(datas.get('목'))
				meal = char_replace(meal)

			elif today_weekday == 4 :
				meal = str(datas.get('금'))
				meal = char_replace(meal)

			elif today_weekday == 5 :
				meal = str(datas.get('토'))
				meal = char_replace(meal)

			else :
				meal = sun_except.format(content_name)

		except Exception as e:
			meal = str(e) + json_open_error

		send_message = select_button.format(content_name, today_info) + meal

		return re_process(send_message)

	elif content_name == '향설2 생활관' :

		try :
			with open('app/menu/SnowFlowerTwo.json', 'rb') as f :
				datas = json.load(f)

			if today_weekday >= 0 or today_weekday <= 4  :
				meal = str(datas.get('향2'))
				meal = char_replace(meal)

			else :
				meal = weekend_except.format(content_name)

		except Exception as e:
			meal = str(e) + json_open_error

		send_message = select_button.format(content_name, today_info) + meal

		return re_process(send_message)

	elif content_name == '향설3 생활관' :

		try :
			with open('app/menu/SnowFlowerThree.json', 'rb') as f :
				datas = json.load(f)

			if today_weekday == 0 :
				meal = str(datas.get('월'))
				meal = char_replace(meal)

			elif today_weekday == 1 :
				meal = str(datas.get('화'))
				meal = char_replace(meal)

			elif today_weekday == 2 :
				meal = str(datas.get('수'))
				meal = char_replace(meal)

			elif today_weekday == 3 :
				meal = str(datas.get('목'))
				meal = char_replace(meal)

			elif today_weekday == 4 :
				meal = str(datas.get('금'))
				meal = char_replace(meal)

			else :
				meal = str(datas.get('주말'))
				meal = char_replace(meal)

		except Exception as e:
			meal = str(e) + json_open_error

		send_message = select_button.format(content_name, today_info) + meal

		return re_process(send_message)

	elif content_name == '학생회관' :

		try :
			with open('app/menu/StudentUnion.json', 'rb') as f :
				datas = json.load(f)

			if today_weekday == 0 :
				meal = str(datas.get('월'))
				meal = char_replace(meal)

			elif today_weekday == 1 :
				meal = str(datas.get('화'))
				meal = char_replace(meal)

			elif today_weekday == 2 :
				meal = str(datas.get('수'))
				meal = char_replace(meal)

			elif today_weekday == 3 :
				meal = str(datas.get('목'))
				meal = char_replace(meal)

			elif today_weekday == 4 :
				meal = str(datas.get('금'))
				meal = char_replace(meal)

			else :
				meal = weekend_except.format(content_name)

		except Exception as e:
			meal = str(e) + json_open_error

		send_message = select_button.format(content_name, today_info) + meal

		return re_process(send_message)

	elif content_name == '교직원 식당' :

		try :
			with open('app/menu/FacultyRestaurant.json', 'rb') as f :
				datas = json.load(f)

			if today_weekday == 0 :
				meal = str(datas.get('월'))
				meal = char_replace(meal)

			elif today_weekday == 1 :
				meal = str(datas.get('화'))
				meal = char_replace(meal)

			elif today_weekday == 2 :
				meal = str(datas.get('수'))
				meal = char_replace(meal)

			elif today_weekday == 3 :
				meal = str(datas.get('목'))
				meal = char_replace(meal)

			elif today_weekday == 4 :
				meal = str(datas.get('금'))
				meal = char_replace(meal)

			else :
				meal = weekend_except.format(content_name)

		except Exception as e:
			meal = str(e) + json_open_error

		send_message = select_button.format(content_name, today_info) + meal

		return re_process(send_message)

	elif content_name == '처음으로' :

		return re_process(content_name)

	elif content_name == '교내 Wi-Fi' :

		send_message = select_else_button.format(content_name) + wifi_info

		return re_process(send_message)

	elif content_name == '종강' :

		# 종강 일
		try :
			finish = datetime.datetime(2018, 6, 22)
			finish_info = finish.strftime('%Y년 %m월 %d일')
			date_dif = finish - today

			send_message = select_else_button.format(content_name) + end_day.format(today_info, finish_info, date_dif.days)

		except Exception as e :
			send_message = str(e)

		return re_process(send_message)

	elif content_name == '학사 일정' :

		result_message = parser()

		today_info = today.strftime('%Y년 %m월')

		send_message =  select_else_button.format(content_name) + '[*] ' + today_info + result_message

		return re_process(send_message)

	elif content_name == '개발자 정보' :

		send_message = select_else_button.format(content_name) + dev_info

		return re_process(send_message)

	else :

		error_message = fatal_error

		return re_process(error_message)
