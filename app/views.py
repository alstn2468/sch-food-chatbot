from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def keyboard(request) :
	return JsonResponse (
		{
		'type' : 'buttons',
		'buttons' : ['button1', 'button2', 'button3']
		}
	)

def message(request) :
	return JsonResponse (
		{
			'message' :
			{
				'text' : 'Input the sentence that you want.'
			},
			'keyboard' :
			{
				'type' : 'button',
				'buttons' : ['button1', 'button2', 'button3', 'button4', 'button5']
			}
		}
	)
