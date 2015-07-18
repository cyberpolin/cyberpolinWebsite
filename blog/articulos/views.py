from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from rest_framework import viewsets, generics
from articulos.serializers import *
from articulos.models import *
from articulos.forms import *
from articulos.models import Publicacion
import json


from django.shortcuts import render
from django.http import HttpResponseRedirect

# Vistas regulares

def index_view(request):
    return render_to_response('frontEnd/index.html', context_instance=RequestContext(request))

# MEDIA
def media_func():

    media = Media.objects.order_by('date')
    ctx = {}
    ctx['media'] = media

    return media

def add_media_view(request):
    ctx ={}
    form = Media_Form(request.POST, request.FILES)

    if form:
        if form.is_valid():
            # SOLO PARA HACERLO A MANO
            #handle_uploaded_file(request.FILES['file'])

            form.save()
            return HttpResponseRedirect('/admin/articulos/')
        else:
            ctx['error'] = 'Los datos del formulario son invalidos, intentelo de nuevo por favor'
            ctx['form'] = form
            return render(request, 'index.html', ctx)
    else:
        # No enviaron nada
        return




#
@login_required(login_url='/admin/login/')
def articulos_view(request):
    ctx = {}
    p = Publicacion.objects.order_by('fecha')
    activas = p.filter(status=True)
    borradas = p.filter(status=False).count()
    ctx['publicaciones'] = activas
    ctx['pubBorradas'] = borradas


    return render(request, 'listas.html', ctx)

def list_portfolio_view(request):
    """

    :param request:
    :return:
    """
    ctx = {}
    p = Portfolio.objects.order_by('date').filter(status = True)
    ctx['portfolio'] = p
    ctx['pubBorradas'] = Portfolio.objects.filter(status =False).count()

    return render(request, 'portfolio.html', ctx)

def add_portfolio_view(request):
    ctx = {}
    ctx['form'] = NewPortfolio_form(request.POST, request.FILES)

    if request.method == 'POST':
        print(request.FILES)
        if ctx['form'].is_valid():
            '''
            p = Portfolio()
            p.title = ctx['form'].cleaned_data['title']
            p.description = ctx['form'].cleaned_data['description']
            p.url = ctx['form'].cleaned_data['description']
            p.save()
            '''
            ctx['form'].save()
            return HttpResponseRedirect('../portfolio/')
        else:
            ctx['error'] = 'Los datos del formulario son invalidos, intentelo de nuevo por favor'
            return render(request, 'index.html', ctx)
        return render(request, 'index.html', ctx)

    else:

        ctx['form'] = NewPortfolio_form()
        return render(request, 'index.html', ctx)

def portfolio_deleted_view(request):
    ctx ={}
    p = Portfolio.objects.order_by('date').filter(status=False)
    ctx['portfolio'] = p

    return render(request, 'portfolio.html', ctx)

def portfolio_delete_view(request, pk):
    ctx = {}
    p =  Portfolio.objects.get(pk=pk)
    p.status=False
    p.save()

    from django.http import HttpResponse
    return HttpResponse(json.dumps({"status": True}), content_type='application/json')

def porfolio_udelete_view(request, pk):
    ctx = {}
    p = Portfolio.objects.get(pk=pk)
    p.status=True
    p.save()

    from django.http import HttpResponse
    return HttpResponse(json.dumps({"status": True}), content_type='application/json')

#       PORTOFOLIO      #
#       ARTICLE         #

def articulos_borrados_view(request):
    ctx ={}
    p = Publicacion.objects.order_by('fecha').filter(status=False)
    ctx['publicaciones'] = p

    return render(request, 'listas.html', ctx)

def add_article_view(request):
    ctx = {}
    form = NewPost_form(request.POST)

    #Trae los datos de la funcion media_func
    ctx['media'] = media_func()

    if request.method == 'POST':

        if form.is_valid():

            titulo = form.cleaned_data['titulo']
            texto = form.cleaned_data['texto']

            p = Publicacion()
            p.titulo = titulo
            p.texto = texto

            p.save()
            return HttpResponseRedirect('./articulos/')
        else:
            # print(form.cleaned_data['texto'])

            ctx['error'] = 'Los datos del formulario son invalidos, intentelo de nuevo por favor'
            ctx['form'] = form
            return render(request, 'index.html', ctx)
    else:

        formulario = NewPost_form()
        ctx['form'] = formulario
        return render(request, 'index.html', ctx)

def borrar_view(request, articulo_id):
    ctx = {}
    p =  Publicacion.objects.get(pk=articulo_id)
    p.status=False
    p.save()

    from django.http import HttpResponse
    return HttpResponse(json.dumps({"status": True}), content_type='application/json')

def des_borrar_view(request, articulo_id):
    ctx = {}
    p = Publicacion.objects.get(pk=articulo_id)
    p.status=True
    p.save()

    from django.http import HttpResponse
    return HttpResponse(json.dumps({"status": True}), content_type='application/json')


def editar_view(request, articulo_id):
    ctx={}
    p =  Publicacion.objects.get(pk=articulo_id)
    ctx['media'] = media_func()


    if request.method == 'POST':
        form = NewPost_form(request.POST)

        if form.is_valid():

            titulo = form.cleaned_data['titulo']
            texto = form.cleaned_data['texto']

            p = Publicacion.objects.get(pk=articulo_id)
            p.titulo = titulo
            p.texto = texto

            p.save()
            return HttpResponseRedirect(request.path)
        else:

            print(form.errors)
            ctx['error'] = 'Los datos del formulario son invalidos, intentelo de nuevo por favor'
            ctx['form'] = form
            return render(request, 'index.html', ctx)

    else:

        form = NewPost_form(instance=p)
        ctx['form'] = form

        return render(request, 'index.html', ctx)

def login_view(request):

    ctx = {}
    ctx['next'] = request.GET['next']

    user = None
    print (request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        ctx['error'] = username + password
        user = authenticate(username=username, password=password)
        return print('aaa0')

    if user is not None:
        if user.is_active:
            login(request, user)
            return print('logeado')
        else:
            print('mandaste pero no logeaste')
            ctx['error'] = 'El usuario o contraseña, no coincide'
            return render(request, 'login.html', ctx)
    else:
        print('nada')
        return render(request, 'login.html', ctx)

def logout_view(request):
    return logout(request)

# RESTFUL API

class PostView(generics.ListCreateAPIView):
	queryset = Publicacion.objects.all()
	model = Publicacion
	serializer_class = Post
