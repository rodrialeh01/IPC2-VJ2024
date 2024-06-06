#Libreria para ElementTree
import xml.etree.ElementTree as ET
from tkinter import filedialog, messagebox
#Libreria para minidom
from xml.dom import minidom


def menu_principal():
    ruta = ''
    while True:
        print('--------- MENU PRINCIPAL ---------')
        print('- 1. Cargar XML                  -')
        print('- 2. Leer XML con miniDOM        -')
        print('- 3. Leer XML con ElementTree    -')
        print('- 4. Escribir XML con miniDOM    -')
        print('- 5. Escribir XML con ElementTree-')
        print('- 6. Salir                       -')
        print('----------------------------------')
        opcion = int(input('Seleccione una opción: '))
        match opcion:
            case 1:
                ruta = cargar_xml()
                if ruta == '':
                    messagebox.showerror('Error', 'No se ha seleccionado ningún archivo o hubo un error al cargar un archivo')
                else:
                    messagebox.showinfo('Éxito', 'Archivo cargado con éxito')
            case 2:
                leer_xml_minidom(ruta)
            case 3:
                leer_xml_elementtree(ruta)
            case 4:
                escribir_xml_minidom()
            case 5:
                escribir_xml_elementtree()
            case 6:
                print('Hasta luego')
            case _:
                print('Opción no válida')

def cargar_xml():
    ruta_tinter = filedialog.askopenfilename(title='Cargar Archivo XML', filetypes= (('Text files', '*.xml*'), ('All files', '*.*')))
    return ruta_tinter

def leer_xml_minidom(ruta):
    #PARSEA EL XML
    doc = minidom.parse(ruta)
    #OBTIENE EL ELEMENTO RAIZ
    root = doc.documentElement
    #Imprime el nombre de la etiqueta raiz
    print(root.nodeName)

    if root.nodeName == 'libros':
        #Obtener los nodos de la raiz
        libros = root.getElementsByTagName('libro')

        #Recorrer los nodos de la raiz
        for libro in libros:
            #PARA OBTENER ATRIBUTO
            id = libro.getAttribute('id')
            #PARA OBTENER EL TEXTO DE UNA ETIQUETA
            titulo = libro.getElementsByTagName('titulo')[0].firstChild.data
            autor = libro.getElementsByTagName('autor')[0].firstChild.data
            precio = libro.getElementsByTagName('precio')[0].firstChild.data
            imagen = libro.getElementsByTagName('imagen')[0].firstChild.data
            print(f'ID: {id}\n'
                f'Título: {titulo}\n'
                f'Autor: {autor}\n'
                f'Precio: {precio}\n'
                f'Imagen: {imagen}\n')
    
    elif root.nodeName == 'reservaciones':
        #OBTIENE LAS RESERVACIONES
        reservaciones = root.getElementsByTagName('reservacion')
        for reservacion in reservaciones:
            id = reservacion.getAttribute('id')
            descripcion = reservacion.getElementsByTagName('descripcion')[0].firstChild.data
            libro = reservacion.getElementsByTagName('libro')[0].firstChild.data
            usuario = reservacion.getElementsByTagName('usuario')[0].firstChild.data
            #contenido de la etiqueta
            dia = reservacion.getElementsByTagName('dia')[0].firstChild.data
            #atributo
            hora = reservacion.getElementsByTagName('dia')[0].getAttribute('hora')
            print(f'ID: {id}\n'
                f'Descripcion: {descripcion}\n'
                f'Libro: {libro}\n'
                f'Usuario: {usuario}\n'
                f'Dia: {dia}\n'
                f'Hora: {hora}\n')

def leer_xml_elementtree(ruta):
    #PARSEAR EL XML
    tree = ET.parse(ruta)
    #OBTENER EL ELEMENTO RAIZ
    root = tree.getroot()
    #imprime el nombre de la etiqueta raiz
    print(root.tag)
    if root.tag == 'libros':
        #imprime cuantas etiquetas tiene la raiz
        print(len(root))

        #recorremos las etiquetas de la raiz
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
            print(f'ID: {id}\n'
                f'Password: {password}\n'
                f'Nombre: {nombre}\n'
                f'Edad: {edad}\n'
                f'Email: {email}\n'
                f'Telefono: {telefono}\n')
            print('----------------------------------')
    elif root.tag == 'reservaciones':
        for reservacion in root:
            id = reservacion.attrib['id']
            descripcion = ''
            libro = ''
            usuario = ''
            dia = ''
            hora = ''
            for subreservacion in reservacion:
                match subreservacion.tag:
                    case 'descripcion':
                        descripcion = subreservacion.text
                    case 'libro':
                        libro = subreservacion.text
                    case 'usuario':
                        usuario = subreservacion.text
                    case 'dia':
                        dia = subreservacion.text
                        hora = subreservacion.attrib['hora']
            print(f'ID: {id}\n'
                f'Descripcion: {descripcion}\n'
                f'Libro: {libro}\n'
                f'Usuario: {usuario}\n'
                f'Dia: {dia}\n'
                f'Hora: {hora}\n')
            print('----------------------------------')

def escribir_xml_minidom():
    pass

def escribir_xml_elementtree():
    pass

if __name__ == '__main__':
    menu_principal()