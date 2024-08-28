from django.shortcuts import render

def helloWord(request):
    return render(request,'signup.html')