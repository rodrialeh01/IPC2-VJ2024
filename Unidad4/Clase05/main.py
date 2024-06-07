#Libreria para ElementTree
import xml.etree.ElementTree as ET
from tkinter import filedialog, messagebox

#Importando clases
#libro
from clases.libro import Libro
#usuario
from clases.usuario import Usuario
#LISTA DOBLE
from lista_doble.lista_doble import ListaDoble
#IMPORTANDO LISTAS
#LISTA SIMPLE
from lista_simple.lista_simple import ListaSimple

#CREAMOS LISTA GLOBAL DE USUARIOS
lista_usuarios = ListaSimple()
lista_libros = ListaDoble()

def menu_principal():
    global lista_usuarios
    ruta = ''
    while True:
        print('--------- MENU PRINCIPAL ---------')
        print('- 1. Cargar y Leer Usuarios      -')
        print('- 2. Generar Reporte Usuarios    -')
        print('- 3. Cargar y Leer Libros        -')
        print('- 4. Generar Reporte Libros      -')
        print('- 5. Salir                       -')
        print('----------------------------------')
        opcion = int(input('Seleccione una opción: '))
        match opcion:
            case 1:
                ruta = 'C:\\Users\\rodri\\Documents\\REPOSITORIOS\\IPC2-VJ2024\\Unidad4\\entrada\\usuarios.xml'
                leer_xml_usuarios(ruta)
                '''if ruta == '':
                    messagebox.showerror('Error', 'No se ha seleccionado ningún archivo o hubo un error al cargar un archivo')
                else:
                    messagebox.showinfo('Éxito', 'Archivo cargado con éxito')'''
            case 2:
                lista_usuarios.graficar()
            case 3:
                ruta = 'C:\\Users\\rodri\\Documents\\REPOSITORIOS\\IPC2-VJ2024\\Unidad4\\entrada\\libros.xml'
                leer_xml_libros(ruta)
                '''if ruta == '':
                    messagebox.showerror('Error', 'No se ha seleccionado ningún archivo o hubo un error al cargar un archivo')
                else:
                    messagebox.showinfo('Éxito', 'Archivo cargado con éxito')'''
            case 4:
                lista_libros.graficar()
            case 5:
                print('Hasta luego')
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
        lista_usuarios.insertar(user)
    lista_usuarios.imprimirNombres()
    #imprimir el usuario IPC2-03
    print('------------------------')
    print(str(lista_usuarios.obtenerUsuario('IPC2-03')))

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
        lista_libros.insertar(libro)
    lista_libros.imprimirLibros()

if __name__ == '__main__':
    menu_principal()