from django.shortcuts import render
from .models import NewsModel

def brand(request):
    
    brand = NewsModel.objects.all()
    context = {
        'brand' : brand
    }
    return render(request, 'index.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, "index.html")


def single_page(request):
    return render(request, "pages/single_page.html")


def contact(request):
    return render(request, "contact.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Login yoki parol noto‘g‘ri")

    return render(request, "pages/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")

from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")



