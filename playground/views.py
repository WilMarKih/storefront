from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x ,y = 1, 2
    return x

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name':'Wilson'})