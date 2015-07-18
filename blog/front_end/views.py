# -*- coding: UTF-8 -*-

from django.shortcuts import render
from articulos.models import *

# Create your views here.
def index_view(request):
    ctx = {}
    p = Publicacion.objects.get(pk=9)
    ctx['pagina'] = p
    ctx['seccion'] = 'inicio'
    return render(request, 'frontEnd/index.html', ctx)

def portfolio_view(request):
    ctx = {}
    p= Portfolio.objects.filter(status=True)
    ctx['portfolio'] = p
    return render(request, 'frontEnd/portfolio.html', ctx)

def blog_view(request):
    ctx = {}
    p = Publicacion.objects.order_by('-fecha').filter(tipo=2)
    tips = Publicacion.objects.filter(tipo=4)
    ctx['contenido'] = p
    ctx['tips'] = tips

    return render(request, 'frontEnd/list.html', ctx)

def article_view(request, slug):
    ctx = {}
    p = Publicacion.objects.get(slug=slug)
    op = Publicacion.objects.order_by('?')[:10]
#    print(op)
    ctx['contenido'] = p
    ctx['op'] = op
    return render(request, 'frontEnd/article.html', ctx)

def hire_me_view(request):
    return render(request, 'frontEnd/hire-me.html')

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
