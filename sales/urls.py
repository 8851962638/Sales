# sales/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload_referral_fee/', views.upload_referral_fee, name='upload_referral_fee'),
    path('upload_cost/', views.upload_cost, name='upload_cost'),
    path('user_data/', views.user_data, name='user_data'),
]
