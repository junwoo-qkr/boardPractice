from django.urls import path, include
from . import views

app_name = 'rptlvks_main'

urlpatterns = [
    path('', views.index, name='index')
]