from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('', views.home_view, name='home_url'),
    path('profile-bem/', views.profile_calon_bem_view, name='profil_calon_bem_url'),
    path('profile-bpm/', views.profile_calon_bpm_view, name='profil_calon_bpm_url'),
    path('hasil/', views.chart_view, name='hasil_url'),
    path('profile/<str:param>/', views.profile_detail_view, name='profil_detail_url')
]
