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
