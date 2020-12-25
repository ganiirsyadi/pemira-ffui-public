from django.urls import path

from . import views

app_name = "vote"

urlpatterns = [
    path('', views.otp_view, name='otp_url'),
    path('submit/', views.vote_view, name='vote_url')
]
