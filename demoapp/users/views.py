from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationUserForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"{username} has Successfully registered. Please Login")
            return redirect('login')
    else:
        form=RegistrationUserForm()
    return render(request,template_name='users/register.html',context={'form':form})

@login_required('')
def profile(request):
    return render(request,template_name='users/profile.html')