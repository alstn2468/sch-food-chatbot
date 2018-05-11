from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pytz import timezone
import datetime
import json

dev_info = '순천향대학교 컴퓨터소프트웨어공학과 김민수'
stop_message = '[*]연속 동일 요청입니다. 나중에 다시 시도해주세요.'

class user_chk() :

    def __init__(self) :
        self.pre_key = "" #이전 user_key값
        self.now_key = "" #현재 user_key값

    def check(self, key) :
        self.now_key = key # now_key값에 현재 user_key값 대입

        if self.pre_key == self.now_key : # 비교 하여 같으면 1을 반환
            passcode = 1

        else :
            self.pre_key = self.now_key # 다를 경우 pre_key값에 now_key값을 덮어쓰고 0 반환
            passcode = 0

        return passcode

user0 = user_chk()
user1 = user_chk()
user2 = user_chk()
user3 = user_chk()
user4 = user_chk()

def re_process(output) :

    return JsonResponse (
			{
            'message':
			{
                'text': output
            },
            'keyboard':
			{
                'type': 'buttons',
                'buttons' : ['학식', '내일의 학식', '개발자 정보']
            }
        }
	)

def keyboard(request) :

	return JsonResponse (
		{
		'type' : 'buttons',
		'buttons' : ['학식', '내일의 학식', '개발자 정보']
		}
	)

@csrf_exempt
def message(request) :

	json_str = ((request.body).decode('utf-8'))
	received_json = json.loads(json_str)
	content_name = received_json['content']
	type_name = received_json['type']
	user_key = received_json_data['user_key']

	# 오늘
	today = datetime.datetime.today()
	today_info = today.strftime('%Y년 %m월 %d일')

	# 내일
	tomorrow = datetime.datetime.today() + datetime.timedelta(days = 1)
	tomorrow_info = tomorrow.strftime('%Y년 %m월 %d일')

	if content_name == '학식' :
		if user0.check(user_key) :
			return re_process(stop_message)

		message = '선택한 버튼 : ' + content_name + '\n' + '오늘은 ' + today_info + '입니다.'

		return re_process(message)

	elif content_name == '내일의 학식' :
		if user1.check(user_key) :
			return re_process(stop_message)

		message = '선택한 버튼 : ' + content_name + '\n' + '내일은 ' + tomorrow_info + '입니다.'

		return re_process(message)

	elif content_name == '개발자 정보' :
		if user2.check(user_key) :
			return re_process(stop_message)

		message = '선택한 버튼 : ' + content_name + '\n' + '개발자는 ' + dev_info + '입니다.'

		return re_process(message)

	else :
		if user3.check(user_key) :
			return re_process(stop_message)

		error_message = '심각한 오류입니다. 개발자에게 알려주세요'

		if type_name == 'photo' :
			error_message = '사진 보내도 기능이 없네요. 버튼을 눌러주세요!'

		elif type_name == 'video' :
			error_message = '영상을 보내도 기능이 없네요. 버튼을 눌러주세요!'

		elif type_name == 'audio' :
			error_message = '녹음 파일을 보내도 기능이 없네요. 버튼을 눌러주세요!'

		return re_process(error_message)
