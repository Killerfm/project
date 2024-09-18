from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, 'users/register.html')


def logging(request):
    return render(request, 'users/login.html')
