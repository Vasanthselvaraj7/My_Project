import os
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.views.decorators.cache import never_cache
from django.template.loader import get_template, render_to_string
from weasyprint import HTML
from django.conf import settings
import time
from django.utils import timezone


# For Athlete
def athlete_signup(request):

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # check whether the username is exiting
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already Exists')
            return redirect('signin')

        # create new user instance
        user = User(
            first_name=firstname,
            last_name=lastname,
            username=username
        )
        # hash the password
        # if password == confirm_password:
        user.set_password(password)
        user.save()
        messages.success(request, "Signup successfully")
        return redirect('signin')

        # else:
        #     messages.error(request, 'password did not match')
        #     return redirect('signup')
    return render(request, "athlete/signup.html")


def athlete_signin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully login')
                return redirect('athlete')
            else:
                messages.error(request, 'password is incorrect')
                return redirect('signin')
        else:
            messages.error(request, "Username not exist")
            return redirect('signin')
    return render(request, 'athlete/signin.html')


@login_required
@never_cache
def athlete_dashboard(request):
    # Since the user is authenticated, we can safely retrieve the username
    firstname = request.user.first_name
    last_activity = request.user.last_login
    last_login_time = last_activity

    context = {
        "firstnames": firstname,
        "last_login_time": last_login_time
    }
    if request.method == 'POST':
        heart_rate = request.POST['heartrate']
        blood_pressure = request.POST['blood_pressure']
        temperature = request.POST['Temperature']
        if heart_rate and blood_pressure and temperature:
            info = HealthInputs(
                heartrate=heart_rate,
                blood_pressure=blood_pressure,
                Temperature=temperature
            )
            info.save()
            messages.success(request, 'Saved')
            template = get_template('Athlete/pdf.html')
            result = {
                'firstname': request.user.first_name,
                'heartrate': info.heartrate,
                'blood_pressure': info.blood_pressure,
                'Temperature': info.Temperature,
                'date_and_time': info.timestamp
            }
            html_string = template.render(result)
            html = HTML(string=html_string)
            css_path = os.path.join(settings.BASE_DIR, 'static/athletepage/css/pdf.css')
            pdf = html.write_pdf(stylesheets=[css_path])
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline;  filename="Athlete.pdf"'
            return response
    return render(request, 'Athlete/athlete.html', context)


def athlete_logout(request):
    logout(request)
    request.session.flush()
    return render(request, 'main/main.html')
