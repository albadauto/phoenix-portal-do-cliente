from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="app_login:login")
def home_payment(request):
    return render(request, 'main_payment/index.html')

