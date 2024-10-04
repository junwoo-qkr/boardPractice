from django.urls import path
from . import views

app_name = 'rptlvks_write'

urlpatterns = [
    path('', views.write, name='write'),
]