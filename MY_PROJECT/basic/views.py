from django.shortcuts import render,HttpResponse
from django.template import loader

def home(request):
    templates=loader.get_template('index.html')
    return HttpResponse(templates.render())
def login(request):
    templates=loader.get_template('login.html')
    return HttpResponse(templates.render())
def info(request):
    templates=loader.get_template('info.html')
    return HttpResponse(templates.render())