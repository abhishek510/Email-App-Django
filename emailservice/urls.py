from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('parse_input', views.parse_input, name='parse_input'),
    path('send_mail', views.send_mail, name='send_mail'),
]