from django.shortcuts import redirect, render
from .vote_helper import send_otp, check_user_vote
import threading
from random import randint
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from .models import Vote2

# Create your views here.

@login_required(login_url='account:login_url')
def vote_view(request):
    if datetime(2020,12,11,7,30,0) < datetime.now() < datetime(2020,12,15,18,0,0) and request.user.is_verified:
        context = {}
        if request.method == "POST" and not check_user_vote(request.user):
            c = request.POST['bem-choice']
            if c not in ["2","3"]:
                return render(request, 'vote/vote.html')
            else:
                new_vote = Vote2.objects.create(
                    user=request.user,
                    bem_vote = c
                )
                new_vote.save()
                return render(request, 'vote/thanks.html')
        else:
            return redirect('home:home_url')
    else:
        return redirect('home:home_url')

@login_required(login_url='account:login_url')
def otp_view(request):
    return render(request, 'vote/vote.html')
    # if datetime(2020,12,11,7,30,0) < datetime.now() < datetime(2020,12,15,18,0,0) and request.user.is_verified:
    #     context= {}
    #     if check_user_vote(request.user):
    #         return redirect('home:home_url')
    #     if request.method == 'POST':
    #         otp_input = request.POST["otp"]
    #         date_str = request.session["OTP"].split('#')[1]
    #         date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    #         if str(otp_input) == request.session["OTP"].split('#')[0] and date > datetime.now():
    #             request.session["OTP"] = str(str(otp_input) + '#' + str(datetime.now()))
    #             return render(request, 'vote/vote.html')
    #         elif str(otp_input) == request.session["OTP"].split('#')[0] and date < datetime.now():
    #             context['error'] = "Kode OTP sudah kadaluwarsa."
    #             return render(request, 'vote/otp.html', context)
    #         elif str(otp_input) != request.session["OTP"].split('#')[0]:
    #             context['error'] = "Kode OTP yang Anda masukkan salah."
    #             return render(request, 'vote/otp.html', context)
    #     otp = randint(100000, 999999)
    #     try:
    #         date_str = request.session["OTP"].split('#')[1]
    #         date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    #         if date < datetime.now():
    #             t = threading.Thread(target=send_otp, args=(otp, request.user.email,))
    #             t.start()
    #             request.session["OTP"] = str(str(otp) + '#' + str(datetime.now() + timedelta(minutes=15)))
    #         print(request.session["OTP"])
    #         return render(request, 'vote/otp.html', context)
    #     except KeyError as e:
    #         t = threading.Thread(target=send_otp, args=(otp, request.user.email,))
    #         t.start()
    #         request.session["OTP"] = str(str(otp) + '#' + str(datetime.now() + timedelta(minutes=15)))
    #         print(request.session["OTP"])
    #         return render(request, 'vote/otp.html', context)
    #     except Exception as e:
    #         print(e)
    #         context['error'] = "Gagal mengirimkan email untuk kode OTP."
    #         return render(request, 'vote/otp.html', context)
    # else:
    #     return redirect('home:home_url')


