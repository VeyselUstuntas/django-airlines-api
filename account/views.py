from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def user_login(request):
    if request.user.is_authenticated:
        return redirect("airline_list")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username, password=password)

        if user is not None:
            login(request,user)
            nextUrl = request.GET.get("next",None)
            if nextUrl is None:
                return redirect("airline_list")
            else:
                return redirect(nextUrl)

        else:
            return render(request, "account/login.html",{"error":"username or password is wrong"})
    else:
        return render(request, "account/login.html")

def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]    
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html",{"error":"username kullanılmış","user_name":username, "email":email})
            if User.objects.filter(email=email).exists():
                return render(request, "account/register.html",{"error":"email kullanılmış","user_name":username, "email":email})
            else:
                user = User.objects.create(is_superuser = True, is_staff = True , is_active = True, username = username, email = email, password = password)
                user.set_password(password)
                user.save()
                return redirect("user_login")
        else:
            return render(request, "account/register.html",{"error":"Şifreler Eşleşmiyor","user_name":username, "email":email})
        
    else:
        return render(request, "account/register.html")

@login_required()
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("user_login")
