from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from dashboard.apps import DashboardConfig
import logging


logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return render(request, 'dashboard/dashboard_bootstrap.html')

def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'dashboard/user_registration_bootstrap.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("dashboard:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'dashboard/user_registration_bootstrap.html', context)


def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'dashboard/user_login_bootstrap.html', context)
    else:
        return render(request, 'dashboard/user_login_bootstrap.html', context)


def logout_request(request):
    logout(request)
    return redirect('dashboard:index')

