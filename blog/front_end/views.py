# -*- coding: UTF-8 -*-

from django.shortcuts import render
from articulos.models import *

# Create your views here.
def index_view(request):
    ctx = {}
    p = Publicacion.objects.get(pk=9)
    ctx['pagina'] = p
    ctx['seccion'] = 'inicio'
    ctx['category'] = 'home'
    return render(request, 'dbc-theme/index.html', ctx)

def portfolio_view(request):
    ctx = {}
    p = Publicacion.objects.order_by('-fecha').filter(tipo=3)
    print(p)
    ctx['contenido'] = p
    ctx['category'] = 'projects'

    return render(request, 'dbc-theme/projects.html', ctx)


def blog_view(request):
    ctx = {}
    p = Publicacion.objects.order_by('-fecha').filter(tipo=2)
    ctx['contenido'] = p
    ctx['category'] = 'blog'

    return render(request, 'dbc-theme/blog.html', ctx)

def article_view(request, slug):
    ctx = {}
    p = Publicacion.objects.get(slug=slug)
    op = Publicacion.objects.order_by('?')[:10]
    ctx['contenido'] = p
    ctx['op'] = op
    return render(request, 'dbc-theme/article.html', ctx)

def hire_me_view(request):
    return render(request, 'dbc-theme/about.html')

def send_mail_view(request):
    from django.conf import settings
    from django.core.mail import send_mail
    post = request.POST
    name = post['name']
    email = post['email']
    mail = email + '''
    ''' + post['mail']

    send_mail(''+ name +' want to hire you', mail, email,
        [settings.EMAIL_HOST_USER], fail_silently=False)
    return render(request, 'frontEnd/hire-me-do.html')
