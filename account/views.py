from datetime import date, datetime
from django.contrib.auth import login, logout
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Voter
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    context = {}
    if datetime.now() > datetime(2020,12,4,0,0,0):
        context['info'] = 'CLOSEREG'
    if request.method == 'POST':
        try:
            email = request.POST['email']
            npm = request.POST['npm']
            print(email)
            print(npm)
            user = Voter.object.get(email=email, npm=npm)
            if user.is_registered:
                login(request, user)
                return redirect('home:home_url')
            else:
                context['error'] = 'Akun yang Anda masukkan belum terdaftar'
        except Exception as e:
            print(e)
            context['error'] = 'Email atau NPM yang Anda masukkan salah'
        return render(request, 'account/login.html', context)
    return render(request, 'account/login.html', context)


def register_view(request):
    if datetime.now() < datetime(2020,12,4,0,0,0):
        if request.method == 'POST':
            context = {}
            try:
                email = request.POST['email']
                npm = request.POST['npm']
                print(email)
                print(npm)
                user = Voter.object.get(email=email, npm=npm)
                if user.is_registered:
                    context['error'] = 'Akun Anda sudah terdaftar, silahkan masuk.'
                else:
                    context['user'] = user
                    return render(request, 'account/summary.html', context)
            except Exception as e:
                print(e)
                context['error'] = 'Email atau NPM Anda tidak terdaftar sebagai pemilih.'
                print(context['error'])
            print(context['error'])
            return render(request, 'account/registrasi.html', context)
        return render(request, 'account/registrasi.html')
    else:
        return redirect('home:home_url')


def verification_view(request):
    if datetime.now() < datetime(2020,12,4,0,0,0):
        if request.method == 'POST':
            context = {}
            try:
                email = request.POST['email']
                npm = request.POST['npm']
                user = Voter.object.get(email=email, npm=npm)
                print(request.FILES)
                if request.FILES:
                    user.bukti_foto = request.FILES['file']
                    user.is_registered = True
                    user.is_active = True
                    user.save()
                    login(request, user)
                    return redirect('home:home_url')
                else:
                    context['email'] = email
                    context['npm'] = npm
                    return render(request, 'account/verification.html', context)
            except:
                return redirect(request, 'account:register_url')
        else:
            return redirect('home:home_url')
    else:
        return redirect('home:home_url')


@login_required(login_url='account:login_url')
def account_view(request):
    return render(request, 'account/account.html')

def logout_view(request):
    logout(request)
    return redirect('home:home_url')