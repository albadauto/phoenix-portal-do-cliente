from django.urls import path
from . import views

app_name = 'app_call'

urlpatterns = [
    path('', views.home, name='call_home')
]
