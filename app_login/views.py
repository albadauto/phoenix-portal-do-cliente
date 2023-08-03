from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.core import exceptions
from app_login.models import TUSER


def login_user(request):
    try:
        if request.method == 'POST':
                dict = {"name": request.POST.get("username"), "password": request.POST.get("password")}
                result = TUSER.objects.get(name=dict["name"], password=dict["password"])
                if result is not None:  
                    return render(request, 'home/index.html')
        else:
            return render(request, 'login/home.html')

    except TUSER.DoesNotExist:
        messages.error(request, "Usuário não existente. Favor contatar o administrador", )
        return render(request, 'login/home.html')

    

def test_register_admin(request):
    try:
        if request.method == 'GET':
            user = TUSER()
            user.name = "root"
            user.password = "root" 
            user.save()
            return HttpResponse("Inserido com sucesso")
    except exceptions.FieldError as err:
        print(err)
    