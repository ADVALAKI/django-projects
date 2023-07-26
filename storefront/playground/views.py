from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# actions

def say_hello(request):
    return render(request, 'hello.html')

def calc(request):
    x = 10
    y = 20
    return render(request, 'calc.html')




