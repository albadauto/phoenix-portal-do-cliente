from django.urls import path
from . import views

app_name = "app_payment"

urlpatterns = [
    path('', views.home_payment, name="home_payment")
]