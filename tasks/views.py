from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def signup(request):
        
        if request.method == 'GET':
            return render(request,'signup.html',{
                'form':UserCreationForm
        })
        else:
            if request.POST['paswword1'] == request.POST['paswword1']:
                user =  User.objects.create_user(username=request.POST('username'), password= request.POST['password1'])
                user.save()
                return HttpResponse('User created succesfully')
                #Register User
            return HttpResponse('Password do not match')
    