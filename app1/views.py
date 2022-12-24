from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<b>This is first string</b>')
def Second(request):
    return HttpResponse('<i>This is second string</i>')