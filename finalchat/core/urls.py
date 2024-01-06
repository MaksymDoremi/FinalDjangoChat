from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('login/', views.signin, name='login'),
    path('registration/', views.registration, name='registration')

]
