#ESCRIBIR XML USANDO ELEMENT TREE
import xml.etree.ElementTree as ET
#CON MINIDOM
from xml.dom import minidom
from xml.dom.minidom import Document


#CREANDOLO A MANITA
def crearXMLaManita():
    contenido = ''
    contenido += '<?xml version="1.0" encoding="UTF-8"?>\n'
    contenido += '<numeros>\n'
    for i in range(20):
        contenido += '\t<numero>Numero '+str(i)+'</numero>\n'
    contenido += '</numeros>'

    with open('numeros.xml', 'w') as archivo:
        archivo.write(contenido)
        archivo.close()

#CREAR UN ARCHIVO XML CON MINIDOM
def crearXMLconMiniDOM():
    #CREAMOS UN DOCUMENTO
    doc = Document()

    #CREAMOS EL ELEMENTO RAIZ
    root = doc.createElement('usuarios')
    doc.appendChild(root)

    #CREAMOS LOS ELEMENTOS HIJOS
    usuario = doc.createElement('usuario')
    #AGREGAMOS ATRIBUTOS
    usuario.setAttribute('id', '1')
    usuario.setAttribute('password', '1234')
    root.appendChild(usuario)

    username = doc.createElement('username')
    usuario.appendChild(username)

    #AGREGAMOS TEXTO A LA ETIQUETA
    username_text = doc.createTextNode('usuario1')
    username.appendChild(username_text)

    nombre = doc.createElement('nombre')
    usuario.appendChild(nombre)

    nombre_text = doc.createTextNode('Usuario Uno')
    nombre.appendChild(nombre_text)

    cumpleanios = doc.createElement('cumpleanios')
    usuario.appendChild(cumpleanios)

    cumpleanios.setAttribute('dia', '1')
    cumpleanios.setAttribute('anio', '2024')

    cumplenios_text = doc.createTextNode('Enero')
    cumpleanios.appendChild(cumplenios_text)


    #CREAMOS EL ARCHIVO
    #AGREGAR UN FORMATO DE INDENTACION
    xml_str = doc.toprettyxml(indent='\t')

    #GUARDAMOS EL ARCHIVO
    with open('usuarios.xml', 'w') as archivo:
        archivo.write(xml_str)
        archivo.close()



#creamos el archivo XML utilizando ElementTree
def crearXMLconET():
    #Creamos el elemento raiz
    carrito_root = ET.Element('carrito_compras')
    for i in range(2):
        id_item = f'IT-{i}'
        nombre = 'Computadora'
        cantidad = i+5*8
        #CREAMOS LAS ETIQUETAS HIJAS CON SUBELEMENT
        #ET.SubElement(nombre_padre,nombre_etiqueta,atributos)
        item = ET.SubElement(carrito_root, 'item', id=id_item, password='1234')
        nombre_element = ET.SubElement(item, 'nombre')
        #AGREGAR TEXTO A LA ETIQUETA
        #variable_etiqueta.text = 'texto'   
        nombre_element.text = nombre
        cantidad_element = ET.SubElement(item, 'cantidad')
        cantidad_element.text = str(cantidad)

    #GENERAR EL ARCHIVO XML
    #tree = ET.ElementTree(nombre_raiz)
    tree = ET.ElementTree(carrito_root)
    #APLICAMOS UN FORMATO DE INDENTACION
    ET.indent(tree, space='\t', level=0)
    #GUARDAMOS Y ESCRIBIMOS EL ARCHIVO XML
    tree.write('carrito.xml', encoding='UTF-8', xml_declaration=True)

