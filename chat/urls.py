from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='message'),
    path('<str:room_name>/', views.room, name='room'),


    path('register', views.user, name='register'),
    path('login', views.loginuser, name='login'),
    path('sendmessage', views.sendmessage, name="sendmessage"),
]