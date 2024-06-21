from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
'''from django.shortcuts import render
from django.http import Http404

def index(request, template_name):
    # Validate template name to prevent directory traversal attacks
    valid_templates = ['login.html', 'index.html']  # list of valid templates
    if template_name not in valid_templates:
        raise Http404("Template does not exist")

    return render(request, template_name)'''
