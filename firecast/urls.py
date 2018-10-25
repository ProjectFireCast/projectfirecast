from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.aboutview.as_view(), name='about'),
    path('menu/', views.UserMenuView.as_view(), name='usermenu'),
    path('podcast/upload/', views.create_podcast, name='upload'),
    path('podcast/listen/', views.podcast_listen, name='listen'),
    path('podcast/detail/<slug:slug>', views.podcast_detail, name='detail'),
    path('legal/privacy', views.PrivacyPolicyView.as_view(), name='privacy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)