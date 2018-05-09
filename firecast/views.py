# from django.shortcuts import render
from django.views.generic import TemplateView
# from django.core.mail import EmailMessage


class HomePageView(TemplateView):
    template_name = 'firecast/home.html'

# def index(request):
#    return render(request, 'firecast/index.html', {})


# email = EmailMessage('Subject', 'Body', to=['projectfirecast666@gmail.com'])
# email.send()
