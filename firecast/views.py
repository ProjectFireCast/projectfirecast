from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
# from django.core.mail import EmailMessage


class HomePageView(TemplateView):
    template_name = 'firecast/home.html'




# email = EmailMessage('Subject', 'Body', to=['projectfirecast666@gmail.com'])
# email.send()
