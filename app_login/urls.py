from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
    path('', views.login_user, name='login'),
    path('registerAdmin/', views.test_register_admin, name='registerAdmin'),
    path('logout/', views.logout_user, name='logout')


]
