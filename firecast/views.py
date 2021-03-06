
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


class PrivacyPolicyView(TemplateView):
    template_name = 'socialaccount/privacy_policy.html'

class aboutview(TemplateView):
    template_name = 'firecast/about.html'


@login_required(login_url="/accounts/login")
def create_podcast(request):
    if request.method == 'POST':
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listen')
    else:
        form = forms.PodcastForm()
    return render(request, 'firecast/upload_podcast.html', {'form': form})


def podcast_listen(request):
    podcasts = Podcast.objects.all().order_by('-date')
    return render(request, 'firecast/podcast_listen.html', {'podcasts': podcasts})


def podcast_detail(request, slug):
    # return HttpResponse(slug)
    podcast = Podcast.objects.get(slug=slug)
    return render(request, 'firecast/podcast_detail.html', {'podcast': podcast})
