import datetime
import xml.etree.ElementTree as ET
from tkinter import filedialog

from clases.libro import Libro
from clases.reservacion import Reservacion
from clases.usuario import Usuario
from lista_circular.lista_circular import ListaCircular
from lista_doble.lista_doble import ListaDoble
from matriz_dispersa.matrizDispersa import MatrizDispersa

lista_libros = ListaCircular()
lista_usuarios = ListaDoble()
matriz_reservaciones = MatrizDispersa()

def menu_principal():
    global lista_libros
    global lista_usuarios
    global matriz_reservaciones
    opcion = 0
    while True:
        print('Menú principal')
        print('1. Cargar Usuarios')
        print('2. Cargar Libros')
        print('3. Cargar Reservaciones')
        print('4. Reporte de Usuarios')
        print('5. Reporte de Libros')
        print('6. Reporte de Reservaciones')
        print('7. Obtener el numero del dia de hoy')
        print('8. Obtener todas las reservaciones de un dia especifico')
        print('9. Salir')
        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                #CAMBIAR A LA FUNCION CARGAR_XML
                ruta = cargar_xml()
                leer_xml_usuarios(ruta)
            case 2:
                #CAMBIAR A LA FUNCION CARGAR_XML
                ruta = cargar_xml()
                leer_xml_libros(ruta)
            case 3:
                #CAMBIAR A LA FUNCION CARGAR_XML
                ruta = cargar_xml()
                leer_xml_reservaciones(ruta)
            case 4:
                lista_usuarios.graficar()
            case 5:
                lista_libros.graficar()
            case 6:
                matriz_reservaciones.graficar()
            case 7:
                obtener_dia_hoy()
            case 8:
                obtener_reservaciones_dia()
            case 9:
                break
            case _:
                print('Opción no válida')


def cargar_xml():
    ruta_tinter = filedialog.askopenfilename(title='Cargar Archivo XML', filetypes= (('Text files', '*.xml*'), ('All files', '*.*')))
    return ruta_tinter

def leer_xml_usuarios(ruta):
    global lista_usuarios
    tree = ET.parse(ruta)
    root = tree.getroot()
    for usuario in root:
        #Para obtener los atributos de una etiqueta
        id = usuario.attrib['id']
        password = usuario.attrib['password']
        nombre = ''
        edad = ''
        email = ''
        telefono = ''
        #para recorrer las etiquetas dentro de usuario
        for subusuario in usuario:
            match subusuario.tag:
                case 'nombre':
                    nombre = subusuario.text
                case 'edad':
                    edad = subusuario.text
                case 'email':
                    email = subusuario.text
                case 'telefono':
                    telefono = subusuario.text
        #CREAMOS UN OBJETO USUARIO
        user = Usuario(id, password, nombre, edad, email, telefono)
        #INSERTAMOS EL USUARIO EN LA LISTA
        lista_usuarios.agregar(user)

def leer_xml_libros(ruta):
    global lista_libros
    tree = ET.parse(ruta)
    root = tree.getroot()
    for libro in root:
        #Para obtener los atributos de una etiqueta
        id = libro.attrib['id']
        titulo = ''
        autor = ''
        precio = ''
        imagen = ''
        #para recorrer las etiquetas dentro de usuario
        for sublibro in libro:
            match sublibro.tag:
                case 'titulo':
                    titulo = sublibro.text
                case 'autor':
                    autor = sublibro.text
                case 'precio':
                    precio = sublibro.text
                case 'imagen':
                    imagen = sublibro.text
        #CREAMOS UN OBJETO LIBRO
        libro = Libro(id, titulo, autor, precio, imagen)
        lista_libros.agregar(libro)

def leer_xml_reservaciones(ruta):
    global matriz_reservaciones
    if lista_libros.tamano == 0 or lista_usuarios.tamano == 0:
        print('Primero debe cargar los libros y los usuarios')
        return
    tree = ET.parse(ruta)
    root = tree.getroot()

    for reservacion in root:
        id_reservacion = reservacion.attrib['id']
        descripcion = ''
        libro = ''
        usuario = ''
        dia = 0
        hora = 0
        for subreservacion in reservacion:
            match subreservacion.tag:
                case 'descripcion':
                    descripcion = subreservacion.text
                case 'libro':
                    libro = subreservacion.text
                case 'usuario':
                    usuario = subreservacion.text
                case 'dia':
                    dia = int(subreservacion.text)
                    hora = int(subreservacion.attrib['hora'])
        
        #OBTENEMOS EL NOMBRE DEL LIBRO Y DEL USUARIO
        nombre_libro = lista_libros.buscar(libro).titulo
        nombre_usuario = lista_usuarios.buscar(usuario).nombre
        #CREAMOS UN OBJETO RESERVACIÓN
        reservacion = Reservacion(id_reservacion, descripcion, nombre_libro, nombre_usuario, dia, hora)
        #INSERTAMOS LA RESERVACIÓN EN LA MATRIZ
        # X = FILAS = HORAS, Y = COLUMNAS = DIAS
        matriz_reservaciones.insertar(hora, dia, reservacion)

def obtener_dia_hoy():
    hoy = datetime.datetime.today()
    dia_hoy = hoy.weekday()+1
    print(f'Hoy es el dia {str(dia_hoy)} de la semana')

def obtener_reservaciones_dia():
    dia = int(input('Ingrese el dia que desea consultar[1-7]: '))
    if dia < 1 or dia > 7:
        print('Dia no válido')
        return
    matriz_reservaciones.recorridoColumnas(dia)


if __name__ == '__main__':
    menu_principal()