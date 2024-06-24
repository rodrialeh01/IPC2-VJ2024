import json

import requests
#para mostrar mensajes en pantalla
from django.contrib import messages
#para el cache
from django.core.cache import cache
#para las cookies
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CantidadForm, FileForm, LoginForm, SearchForm

# Create your views here.
endpoint = 'http://localhost:5000/'

contexto = {
    'user':None,
    'contenido_archivo':None,
    'binario_xml':None
}

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signin(request):
    try:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                #obtenemos los datos del formulario
                iduser = form.cleaned_data['iduser']
                password = form.cleaned_data['password']

                #PETICION AL BACKEND
                #ENDPOINT- URL
                url = endpoint + 'usuarios/login'
                #DATA A ENVIAR
                data = {
                    'id': iduser,
                    'password': password
                }

                #convertimos los datos a json
                json_data = json.dumps(data)

                #HEADERS
                headers = {
                    'Content-Type': 'application/json'
                }

                #llamamos a la peticion backend
                response = requests.post(url, data=json_data, headers=headers)
                respuesta = response.json()
                if response.status_code == 200:
                    rol = int(respuesta['role'])
                    contexto['user'] = iduser
                    pagina_redireccion = None
                    #IR A ADMIN
                    if rol == 0:
                        #si yo quiero almacenar el usuario en cache
                        #cache.set('id_user', iduser, timeout=None)
                        #si yo quiero almacenar el usuario en cookies
                        pagina_redireccion = redirect('carga')
                        pagina_redireccion.set_cookie('id_user', iduser)
                        return pagina_redireccion
                    elif rol == 1:
                        #si yo quiero almacenar el usuario en cache
                        #cache.set('id_user', iduser, timeout=None)
                        #si yo quiero almacenar el usuario en cookies
                        pagina_redireccion = redirect('user')
                        pagina_redireccion.set_cookie('id_user', iduser)
                        return pagina_redireccion


    except:
        return render(request, 'login.html')

def admincarga(request):
    ctx = {
        'title':'Carga Masiva'
    }
    return render(request, 'cargaadmin.html', ctx)

def cargarXML(request):
    ctx = {
        'contenido_archivo':None
    }
    try:
        if request.method == 'POST':
            #obtenemos el formulario
            form = FileForm(request.POST, request.FILES)
            print(form.is_valid())
            if form.is_valid():
                #obtenemos el archivo
                archivo = request.FILES['file']
                #guardamos el binario
                xml = archivo.read()
                xml_decodificado = xml.decode('utf-8')
                #guardamos el contenido del archivo
                contexto['binario_xml'] = xml
                contexto['contenido_archivo'] = xml_decodificado
                ctx['contenido_archivo'] = xml_decodificado
                return render(request, 'cargaadmin.html', ctx)
    except:
        return render(request, 'cargaadmin.html')
    
def enviarLibros(request):
    try:
        if request.method == 'POST':
            xml = contexto['binario_xml']
            if xml is None:
                messages.error(request, 'No se ha cargado ningun archivo')
                return render(request, 'cargaadmin.html')
            
            #PETICION AL BACKEND
            url = endpoint + 'libros/carga'
            respuesta = requests.post(url, data=xml)
            mensaje = respuesta.json()
            messages.success(request, mensaje['message'])
            contexto['binario_xml'] = None
            contexto['contenido_archivo'] = None
            return render(request, 'cargaadmin.html', contexto)
    except:
        return render(request, 'cargaadmin.html')
    
def enviarUsuarios(request):
    try:
        if request.method == 'POST':
            xml = contexto['binario_xml']
            if xml is None:
                messages.error(request, 'No se ha cargado ningun archivo')
                return render(request, 'cargaadmin.html')
            
            #PETICION AL BACKEND
            url = endpoint + 'usuarios/carga'
            respuesta = requests.post(url, data=xml)
            mensaje = respuesta.json()
            messages.success(request, mensaje['message'])
            contexto['binario_xml'] = None
            contexto['contenido_archivo'] = None
            return render(request, 'cargaadmin.html', contexto)
    except:
        return render(request, 'cargaadmin.html')
    
def verLibros(request):
    ctx = {
        'libros':None,
        'title':'Libros'
    }
    url = endpoint + 'libros/verLibros'
    response = requests.get(url)
    data = response.json()
    ctx['libros'] = data['libros']
    return render(request, 'verLibrosAdmin.html', ctx)

def verEstadisticas(request):
    ctx = {
        'title':'Estadisticas'
    }
    return render(request, 'estadisticas.html', ctx)

def verPDF(request):
    ctx = {
        'title':'PDF'
    }
    return render(request, 'verpdf.html', ctx)

def logout(request):
    #si estan usando cache
    #cache.delete('id_user')
    response = redirect('login')
    response.delete_cookie('id_user')
    return response

def userview(request):
    ctx = {
        'libros':None,
        'title':'Libros'
    }
    url = endpoint + 'libros/verLibros'
    response = requests.get(url)
    data = response.json()
    ctx['libros'] = data['libros']
    return render(request, 'user.html', ctx)

def alquilarpage(request):
    return render(request, 'alquilar.html')

ctx_libro = {
    'id_libro':None
}

def buscarLibro(request):
    ctx = {
        'producto_encontrado':None
    }
    try:
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                idlibro = form.cleaned_data['idlibro']
                ctx_libro['id_libro'] = idlibro
                url = endpoint + 'libros/ver/'+idlibro
                response = requests.get(url)
                data = response.json()
                libro = data.get('libro')
                ctx['producto_encontrado'] = libro

                return render(request, 'alquilar.html', ctx)
    except:
        return render(request, 'alquilar.html')
    
def agregarCarrito(request):
    try:
        if request.method == 'POST':
            form = CantidadForm(request.POST)
            if form.is_valid():
                cantidad = form.cleaned_data['cantidad']
                idlibro = ctx_libro['id_libro']
                data = {
                    'idlibro':idlibro,
                    'cantidad':cantidad
                }
                url = endpoint + 'carro/agregar'
                headers = {'Content-type':'application/json'}
                response = requests.post(url, json=data, headers=headers)
                return render(request, 'alquilar.html')
    except:
        return render(request, 'alquilar.html')
    
def alquilar(request):
    try:
        if request.method == 'POST':
            id_user = request.COOKIES.get('id_user')
            url = endpoint + 'alquiler/agregar'
            data = {
                'id_user':id_user
            }
            headers = {'Content-type':'application/json'}
            response = requests.post(url, json=data, headers=headers)
            print(response.json())
            return render(request, 'alquilar.html')
    except:
        return render(request, 'alquilar.html')
    
def verCarrito(request):
    ctx = {
        'contenido_carrito':None
    }
    url = endpoint + 'carro/ver'
    response = requests.get(url)
    data = response.json()
    ctx['contenido_carrito'] = data['contenido']
    return render(request, 'verCarrito.html', ctx)