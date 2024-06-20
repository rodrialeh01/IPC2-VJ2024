import os
from xml.etree import ElementTree as ET

from controllers.estructuras import libros
from flask import Blueprint, jsonify, request
from models.libro import Libro

BlueprintLibro = Blueprint('libro', __name__)

@BlueprintLibro.route('/libros/carga', methods=['POST'])
def cargaLibros():
    try:
        #OBTENEMOS EL XML
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'message': 'Error al cargar los libros: EL XML está vacio',
                'status': 404
            }), 404
        #QUITARLE LOS SALTOS DE LINEA INNECESARIOS
        xml_entrada = xml_entrada.replace('\n', '')
        #LEER EL XML
        root = ET.fromstring(xml_entrada)
        for libro in root:
            id = libro.attrib['id']
            titulo = ''
            autor = ''
            precio = ''
            imagen = ''
            for elemento in libro:
                if elemento.tag == 'titulo':
                    titulo = elemento.text
                if elemento.tag == 'autor':
                    autor = elemento.text
                if elemento.tag == 'precio':
                    precio = elemento.text
                if elemento.tag == 'imagen':
                    imagen = elemento.text
            nuevo = Libro(id, titulo, autor, precio, imagen)
            libros.append(nuevo)
            #AGREGAMOS EL LIBRO AL XML QUE YA EXISTE
            if os.path.exists('database/libros.xml'):
                tree2 = ET.parse('database/libros.xml')
                root2 = tree2.getroot()
                nuevo_libro = ET.Element('libro', id=nuevo.id)
                titulo = ET.SubElement(nuevo_libro, 'titulo')
                titulo.text = nuevo.titulo
                autor = ET.SubElement(nuevo_libro, 'autor')
                autor.text = nuevo.autor
                precio = ET.SubElement(nuevo_libro, 'precio')
                precio.text = nuevo.precio
                imagen = ET.SubElement(nuevo_libro, 'imagen')
                imagen.text = nuevo.imagen
                root2.append(nuevo_libro)
                ET.indent(root2, space='\t', level=0)
                tree2.write('database/libros.xml', encoding='utf-8', xml_declaration=True)

        #SI EN DADO CASO NO EXISTE EL XML, LO CREAMOS
        if not os.path.exists('database/libros.xml'):
            with open('database/libros.xml', 'w', encoding='utf-8') as file:
                file.write(xml_entrada)
                file.close()
        
        return jsonify({
            'message': 'Libros cargados correctamente',
            'status': 200
        }), 200
    except:
        return jsonify({
            'message': 'Error al cargar los libros',
            'status': 404
        }), 404


#METODO DE PRECARGAR LIBROS
def precargaLibros():
    books = []
    if os.path.exists('database/libros.xml'):
        tree = ET.parse('database/libros.xml')
        root = tree.getroot()
        for libro in root:
            id = libro.attrib['id']
            titulo = ''
            autor = ''
            precio = ''
            imagen = ''
            for elemento in libro:
                if elemento.tag == 'titulo':
                    titulo = elemento.text
                if elemento.tag == 'autor':
                    autor = elemento.text
                if elemento.tag == 'precio':
                    precio = elemento.text
                if elemento.tag == 'imagen':
                    imagen = elemento.text
            nuevo = Libro(id, titulo, autor, precio, imagen)
            books.append(nuevo)
    return books