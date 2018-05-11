from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pytz import timezone
import datetime
import json

Dev_Info = '순천향대학교 컴퓨터소프트웨어공학과 김민수'
Stop_Message = '[*]연속 동일 요청입니다. 나중에 다시 시도해주세요.'

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

def Re_Process(output) :

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

	json_str = (request.body).decode('utf-8')
	received_json = json.loads(json_str)
	content_name = received_json['content']
	type_name = received_json['type']
	user_name = received_json['user_key']

	# 오늘
	today = datetime.datetime.today()
	local_date1 = today.strftime('%Y년 %m월 %d일')
	local_weekday1 = today.weekday()

	# 내일
	tomorrow = datetime.datetime.today() + datetime.timedelta(days = 1)
	local_date2 = tomorrow.strftime('%Y년 %m월 %d일')
	local_weekday2 = tomorrow.weekday()

	if content_name == '학식' :
		if user0.check(user_key) :
			return Re_Process(Stop_Message)

		message = '선택한 버튼 : ' + content_name + '\n' + '오늘은 ' + today + '입니다.'

		return Re_Process(message)

	elif content_name == '내일의 학식' :
		if user1.check(user_key) :
			return Re_Process(Stop_Message)

		message = '선택한 버튼 : ' + content_name + '\n' + '내일은 ' + tomorrow + '입니다.'

		return Re_Process(message)

	elif content_name == '개발자 정보' :
		if user2.check(user_key) :
			return Re_Process(Stop_Message)

		message = '선택한 버튼 : ' + content_name + '\n' + '개발자는 ' + Dev_Info + '입니다.'

		return Re_Process(message)

	else :
		if user3.check(user_key) :
			return Re_Process(Stop_Message)

		Error_Message = '심각한 오류입니다. 개발자에게 알려주세요'

		if type_name == 'photo' :
			Error_Message = '사진 보내도 기능이 없네요. 버튼을 눌러주세요!'

		elif type_name == 'video' :
			Error_Message = '영상을 보내도 기능이 없네요. 버튼을 눌러주세요!'

		elif type_name == 'audio' :
			Error_Message = '녹음 파일을 보내도 기능이 없네요. 버튼을 눌러주세요!'

		return Re_Process(Error_Message)
