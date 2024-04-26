from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    posts =[{
        'author':'biren bond',
        'title':'my first post',
        'content':'this is my first post',
        'date_posted':'August 10, 2016'
    },{
        'author':'James kumar',
        'title':'my second post',
        'content':'this is my Second post',
        'date_posted':'July 15, 2016'
    },]
    context={'posts': posts,'title':'Blog'}
    return render(request, template_name='blog/home.html',context=context)
    # return render(request, template_name='home.html',context=context)

def about(request):
    context={'title':'About'}
    return render(request, template_name='blog/about.html',context=context)
    # return render(request, template_name='about.html',context=context)
