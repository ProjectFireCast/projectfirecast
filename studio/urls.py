from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    path('record/', views.record, name='record'),
    path('mix/', views.mix, name='mix'),
]
