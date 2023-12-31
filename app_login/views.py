from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, FieldError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    try:
        if request.method == 'POST':
            dict = {"name": request.POST.get("username"), "password": request.POST.get("password")}
            user = authenticate(username=dict["name"], password=dict["password"])
            if user:
                login(request, user)
                request.session["user_id"] = User.objects.get(username=dict["name"]).pk
                return redirect("app_home:main")
            else:
                messages.error(request, "Erro: Login ou senha inválido(s) Favor, contatar a JR Smarts Softwares (contato@jrsoftwares.com.br)")
                return render(request, 'login/home.html')
        else:
            return render(request, 'login/home.html')

    except User.DoesNotExist:
        return render(request, 'login/home.html')
    except ObjectDoesNotExist as obj:
        print(f"Erro: Por favor contatar um administrador. Mensagem original: {obj}")


def test_register_admin(request):
    try:
        if request.method == 'GET':
            User.objects.create_user(username="root", email="root@root", password="root")
            return HttpResponse("Inserido com sucesso")
    except FieldError as err:
        print(err)


def logout_user(request):
    logout(request=request)
    return redirect("app_login:login")
