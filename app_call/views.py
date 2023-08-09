from django.shortcuts import render
from django.core.exceptions import FieldDoesNotExist
from app_call.models import TCALL
from django.contrib.auth.decorators import login_required

@login_required(login_url="app_login:login")
def home(request):
    return render(request, 'home/index.html', {"count": [1,2,3,4,5]})


def createCall(request):
    try:
        if request.method == "POST":
            info_to_insert = {
                "description": request.POST.get("description"),
                "isSolved": request.POST.get("isSolved")
            }
            tcall = TCALL()
            tcall.description = info_to_insert["description"]
            tcall.isSolved = info_to_insert["isSolved"]
            tcall.save()
    except FieldDoesNotExist as e:
        print("Deu erro")