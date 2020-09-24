from django.shortcuts import render

# Create your views here.


def index(request):
    template_name = 'dashboard/index.html'
    return render(request, template_name=template_name)


def about_us(request):
    template_name = 'dashboard/about_us.html'
    return render(request, template_name=template_name)


def contact(request):
    template_name = 'dashboard/contact.html'
    return render(request, template_name=template_name)


def news(request):
    template_name = 'dashboard/news.html'
    return render(request, template_name=template_name)


def services(request):
    template_name = 'dashboard/services.html'
    return render(request, template_name=template_name)