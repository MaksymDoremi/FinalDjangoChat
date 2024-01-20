from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

'''
registration renders templates/registration.html
logout 
'''
urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')

]
