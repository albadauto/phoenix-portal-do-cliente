from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="app_login:login")
def main(request):
    return render(request, 'main/index.html')