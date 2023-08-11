from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_call.models import TCALL


@login_required(login_url="app_login:login")
def main(request):
    try:
        calls = TCALL.objects.all().filter(login_id=request.session["user_id"])
        return render(request, 'main/index.html', {"calls": calls})
    except TCALL.DoesNotExist:
        print("Não existe")
