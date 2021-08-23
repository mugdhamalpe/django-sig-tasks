from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'input.html')

def enternumber(request):
    number = int(request.GET["number"])
    if(number > 0):
        result = [n for n in range(1, number+1)]
        return render(request, 'number.html', { "resnumber": result , "link":"http://127.0.0.1:8000/number"})
    else:
        return "Invalid number entered! Please enter a positive number."