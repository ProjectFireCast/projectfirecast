#from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'firecast/home.html'

#def index(request):
#    return render(request, 'firecast/index.html', {})


