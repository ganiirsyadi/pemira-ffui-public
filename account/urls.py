from account.views import account_view
from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path('', views.account_view, name='account_url'),
    path('login/', views.login_view, name='login_url'),
    path('verification/', views.verification_view, name="verification_url"),
    path('register/', views.register_view, name="register_url"),
    path('logout/', views.logout_view, name="logout_url")
]
