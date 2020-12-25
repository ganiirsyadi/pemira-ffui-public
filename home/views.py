from datetime import datetime
from django.shortcuts import redirect, render
from vote.models import Vote, Vote2
import json
from vote.vote_helper import check_user_vote
# Create your views here.

def home_view(request):
    context = {}
    try:
        user = request.user
        if user.is_registered and not user.is_verified:
            context['info'] = 'UNVERIFIED'
        elif user.is_registered and user.is_active:
            if datetime.now() < datetime(2020,12,4,7,30,0):
                context['info'] = 'PROFILE'
            elif datetime(2020,12,4,7,30,0) < datetime.now() < datetime(2020,12,9,18,0,0):
                if not check_user_vote(request.user):
                    context['info'] = 'VOTE'
                else:
                    context['info'] = 'DONEVOTE'
            elif datetime(2020,12,9,18,0,0) < datetime.now() < datetime(2020,12,9,20,30,0):
                context['info'] = 'PROFILE'
            elif datetime(2020,12,9,20,30,0) < datetime.now() < datetime(2020,12,11,7,30,0):
                context['info'] = 'RESULT'
            elif datetime(2020,12,11,7,30,0) < datetime.now() < datetime(2020,12,15,18,0,0):
                if not check_user_vote(request.user):
                    context['info'] = 'VOTE'
                else:
                    context['info'] = 'DONEVOTE'
            elif datetime(2020,12,15,18,0,0) < datetime.now() < datetime(2020,12,15,20,0,0):
                context['info'] = 'PROFILE'
            elif datetime(2020,12,15,20,0,0) < datetime.now():
                context['info'] = 'RESULT'

            
    except Exception as e:
        print(e)
        if datetime.now() > datetime(2020,12,4,0,0,0):
            context['info'] = 'CLOSEREG'
        return render(request, 'home/index.html', context)
    return render(request, 'home/index.html', context)

def profile_calon_bem_view(request):
    return render(request, 'home/profil_calon_bem.html')

def profile_calon_bpm_view(request):
    return render(request, 'home/profil_calon_bpm.html')

def profile_detail_view(request, param):
    if param == 'bem1':
        return render(request, 'home/profile/bem1.html')
    elif param == 'bem2':
        return render(request, 'home/profile/bem2.html')
    elif param == 'bem3':
        return render(request, 'home/profile/bem3.html')
    elif param == 'bpm1':
        return render(request, 'home/profile/bpm1.html')
    elif param == 'bpm2':
        return render(request, 'home/profile/bpm2.html')
    elif param == 'bpm3':
        return render(request, 'home/profile/bpm3.html')
    else:
        return redirect('home:home_url')

def chart_view(request):
    if datetime(2020,12,9,20,30,0) < datetime.now() < datetime(2020,12,11,7,30,0):
        bem = {}
        bem['bem1'] = len(Vote.objects.filter(bem_vote='1'))
        bem['bem2'] = len(Vote.objects.filter(bem_vote='2'))
        bem['bem3'] = len(Vote.objects.filter(bem_vote='3'))
        bem_max = max([bem['bem1'],bem['bem2'],bem['bem3']])
        bem['max'] = bem_max
        bpm = {}
        bpm['bpm1'] = len(Vote.objects.filter(bpm_vote='1'))
        bpm['bpm2'] = len(Vote.objects.filter(bpm_vote='2'))
        bpm['bpm3'] = len(Vote.objects.filter(bpm_vote='3'))
        bpm_max = max([bpm['bpm1'],bpm['bpm2'],bpm['bpm3']])
        bpm['max'] = bpm_max
        bem['total'] = bem['bem1'] + bem['bem2'] + bem['bem3']
        bpm['total'] = bpm['bpm1'] + bpm['bpm2'] + bpm['bpm3']
        context = {'hasilBem': json.dumps(bem), 'hasilBpm': json.dumps(bpm)}
        return render(request, 'home/hasil.html', context)
    elif datetime(2020,12,15,20,0,0) < datetime.now():
        bem = {}
        bem['bem2'] = len(Vote2.objects.filter(bem_vote='2'))
        bem['bem3'] = len(Vote2.objects.filter(bem_vote='3'))
        bem_max = max([bem['bem2'],bem['bem3']])
        bem['max'] = bem_max
        bem['total'] = bem['bem2'] + bem['bem3']
        context = {'hasilBem': json.dumps(bem)}
        return render(request, 'home/hasil2.html', context)

    else:
        return redirect('home:home_url')
