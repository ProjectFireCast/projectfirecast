from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .import forms
from .forms import PodcastForm
from .models import Podcast
from django.shortcuts import redirect
# from django.core.mail import EmailMessage


class HomePageView(TemplateView):
    template_name = 'firecast/home.html'


class UserMenuView(TemplateView):
    template_name = 'firecast/usermenu.html'


# class CreatePodcastView(TemplateView):
#     template_name = 'firecast/create_podcast.html'


# login_required(login_url="/accounts/login")
# def create_podcast(request):
#     form = forms.PodcastForm()
#     return render(request, 'firecast/create_podcast.html', {'form': form})

# def home(request):
#     podcasts = Podcast.objects.all()
#     return render(request, 'firecast/', {'podcasts': podcasts})

def create_podcast(request):
    if request.method == 'POST':
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('usermenu')
    else:
        form = forms.PodcastForm()
    return render(request, 'firecast/upload_podcast.html', {'form': form})
