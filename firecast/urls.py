from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views

#app_name = 'podcasts'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('menu/', views.UserMenuView.as_view(), name='usermenu'),
    path('podcast/upload/', views.create_podcast, name='upload'),
    path('podcasts/list/', views.podcast_list, name='list'),
    path('upload/', views.create_podcast, name='upload'),
    path('podcast/detail/<slug:slug>', views.podcast_detail, name='detail'),
    #url(r'podcasts/(?P<slug>[-\w]+)$', views.podcast_detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)