from django.core.mail import send_mail
from django.conf import settings
# from .models import Vote
from .models import Vote2

def send_otp(otp, recipient):
    recipient_list = []
    recipient_list.append(recipient)
    send_mail('Kode OTP Pemira FF UI', 
        f'Berikut adalah kode OTP Anda: {otp}\nKode ini hanya dapat digunakan sekali dan akan hangus setelah 15 menit',
        from_email='Pemira FF UI 2020 <donotreply@pemiraffui.com>',
        recipient_list=recipient_list,
    )

def check_user_vote(user):
    try:
        return Vote2.objects.get(user=user)
    except:
        return False