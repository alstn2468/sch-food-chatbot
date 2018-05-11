from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def keyboard(request) :

	return JsonResponse (
		{
		'type' : 'buttons',
		'buttons' : ['학식', '내일의 학식', '시간별 학식']
		}
	)

@csrf_exempt
def message(request) :

	json_str = (request.body).decode('utf-8')
	received_json = json.loads(json_str)
	content_name = received_json['content']

	if content_name == '학식' :
		return JsonResponse (
			{
				'message' :
				{
					'text' : '선택한 버튼 : ' + content_name
				},
				'keyboard' :
				{
					'type' : 'button',
					'buttons' : ['학식', '내일의 학식', '시간별 학식']
				}
			}
		)

	elif content_name == '내일의 학식' :
		return JsonResponse (
			{
				'message' :
				{
					'text' : '선택한 버튼 : ' + content_name
				},
				'keyboard' :
				{
					'type' : 'button',
					'buttons' : ['학식', '내일의 학식', '시간별 학식']
				}
			}
		)

	elif content_name == '시간별 학식' :
		return JsonResponse (
			{
				'message' :
				{
					'text' : '선택한 버튼 : ' + content_name
				},
				'keyboard' :
				{
					'type' : 'button',
					'buttons' : ['학식', '내일의 학식', '시간별 학식']
				}
			}
		)
