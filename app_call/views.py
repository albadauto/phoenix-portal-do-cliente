from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import FieldDoesNotExist, ObjectDoesNotExist
from app_call.models import TCALL
from django.contrib.auth.decorators import login_required


@login_required(login_url="app_login:login")
def home(request):
    try:
        call = TCALL.objects.all().filter(login_id=request.session['user_id'])
        if call is not None:
            return render(request, 'home/index.html', {"call": call})
    except ObjectDoesNotExist as e:
        print(e)


@login_required(login_url="app_login:login")
def create_call(request):
    try:
        if request.method == "POST":
            call_inserted = TCALL.objects.all().filter(login_id=request.session['user_id'], is_solved=0)
            if len(call_inserted) >= 3:
                messages.error(request, "Você já tem 3 chamados para serem respondidos")
                return redirect("app_call:call_home")
            tcall = TCALL()
            tcall.description = request.POST.get("description")
            tcall.title = request.POST.get("title")
            tcall.login_id = request.session.get("user_id")
            tcall.save()
            messages.success(request, "Novo chamado aberto com sucesso!")
            return redirect("app_call:call_home")
    except FieldDoesNotExist as e:
        print("Deu erro")
