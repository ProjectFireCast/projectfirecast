from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('menu/', views.UserMenuView.as_view(), name='usermenu')
]
