from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.

def index(request) :
	return HttpResponse("Hello, My Name is SCH Food ChatBot!")

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
