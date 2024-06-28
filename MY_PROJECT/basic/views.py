from django.shortcuts import render,HttpResponse
from django.template import loader
'''
def home(request):
    templates=loader.get_template('index.html')
    return HttpResponse(templates.render())
def login(request):
    templates=loader.get_template('login.html')
    return HttpResponse(templates.render())
def info(request):
    templates=loader.get_template('info.html')
    return HttpResponse(templates.render())


def index(request):
    if(request.method=='POST'):
        if(request.POST.get('name')):
            table='bio'
            table.name=request.POST.get('name')
            table.mail=request.POST.get('mail')
            table.phno=request.POST.get('phno')
            table.msg=request.POST.get('msg')
            table.Save()
            
        return render(request,'info.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import userdb

def index(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            # Assuming 'bio' is a model. Replace 'bio' with your actual model class.
            table = userdb()  # Initialize the model instance
            table.name = request.POST.get('name')
            table.mail = request.POST.get('mail')
            table.phno = request.POST.get('phno')
            table.msg = request.POST.get('msg')
            table.save()  # Use save() instead of Save()

    return render(request, 'info.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import userdb

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        phno = request.POST.get('phno')
        msg = request.POST.get('msg')

        if name and mail and phno and msg:
            table = userdb()
            table.name = name
            table.mail = mail
            table.phno = phno
            table.msg = msg
            table.save()
        else:
            return HttpResponse("All fields are required.", status=400)

    return render(request, 'info.html')'''

from django.shortcuts import render
from django.http import HttpResponse
from .models import userdb

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        phno = request.POST.get('phno')
        '''msg = request.POST.get('msg')'''

        # Print statements for debugging
        print(f"name: {name}")
        print(f"mail: {mail}")
        '''print(f"phno: {phno}")
        print(f"msg: {msg}")'''

        if name and mail:
            table = userdb()
            table.name = name
            table.mail = mail
            table.phno = phno
            #table.msg = msg
            table.save()
        else:
            return HttpResponse("All fields are required.", status=400)

    return render(request, 'info.html')

