from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def home(request):
    context={'posts': Post.objects.all()}
    return render(request, template_name='blog/home.html',context=context)

def about(request):
    context={'title':'About'}
    return render(request, template_name='blog/about.html',context=context)
