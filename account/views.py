from django.shortcuts import render

def user_login(request):
    render(request, "account/login.html")

def user_register(request):
    pass

def user_logout(request):
    pass