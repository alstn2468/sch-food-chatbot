from django.http import JsonResponse
from app.my_module.button import *
import requests

# 결과를 출력하고 다시 입력을 받기 위한 함수
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
                'buttons' : basic_button
            }
        }
	)

# 학식 버튼을 눌렀을 때 세부 버튼을 받기 위한 함수
def food_sel_process() :

	return JsonResponse (
		{
			'message' :
			{
				'text' : '어느 곳의 메뉴가 궁금하신가요?'
			},
			'keyboard' :
			{
				'type' : 'buttons',
				'buttons' : food_sel_process_button
			}
		}
	)

def food_info_process() :

	return JsonResponse (
		{
			'message' :
			{
				'text' : '[확인할 수 있는 정보]\n· 메뉴\n· 이용 시간'
			},
			'keyboard' :
			{
				'type' : 'buttons',
				'buttons' : food_info_button
			}
		}
	)
