"""
URL configuration for phoenixportaldocliente project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('home/', include('app_home.urls', namespace='app_home')),
    path('', include('app_login.urls', namespace='app_login')),
    path('call/', include('app_call.urls', namespace='app_call')),
    path('payment/', include('app_payment.urls', namespace='app_payment')),
    path('admin/', admin.site.urls)
]
