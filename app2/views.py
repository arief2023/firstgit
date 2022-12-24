from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Third(request):
    return HttpResponse('<h1>Third String</h1>')

def Fourth(request):
    return HttpResponse('<marquee><h2>Fourth string</h2></marquee>')