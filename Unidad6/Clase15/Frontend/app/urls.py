from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('carga/', views.admincarga, name='carga'),
    path('cargaxml/', views.cargarXML, name='cargaxml'),
    path('xmllibros/', views.enviarLibros, name='xmllibros'),
    path('xmlusuarios/', views.enviarUsuarios, name='xmlusuarios'),
    path('libros/', views.verLibros, name='libros'),
    path('estadisticas/', views.verEstadisticas, name='estadisticas'),
    path('pdf/', views.verPDF, name='pdf'),
    path('user/', views.userview, name='user'),
    path('signin/', views.signin, name='signin'),
]