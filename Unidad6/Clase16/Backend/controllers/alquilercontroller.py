import os
from xml.etree import ElementTree as ET

from controllers.carritocontroller import carrito
from controllers.librocontroller import getlibro
from controllers.usercontroller import getUsuario
from flask import Blueprint, jsonify, request
from models.alquiler import Alquiler
from models.carro import Carro

BlueprintAlquiler = Blueprint('alquiler', __name__)

@BlueprintAlquiler.route('/alquiler/agregar', methods=['POST'])
def agregarAlquiler():
    try:
        alquileres = precargarAlquiler()
        #OBTENEMOS EL JSON
        id_user = request.json['id_user']
        id_alquiler = len(alquileres)+1
        nuevo = Alquiler(id_alquiler,id_user, carrito)
        alquileres.append(nuevo)
        if os.path.exists('database/alquileres.xml'):
            tree = ET.parse('database/alquileres.xml')
            root = tree.getroot()
            nuevo_alquiler = ET.Element('alquiler', numero=str(id_alquiler))
            usuario = getUsuario(id_user)
            user = ET.SubElement(nuevo_alquiler, 'usuario', id=id_user)
            user.text = usuario.nombre
            libros = ET.SubElement(nuevo_alquiler, 'libros')
            for car in carrito:
                libro = getlibro(car.idlibro)
                libroxml = ET.SubElement(libros, 'libro', id=libro.id)
                titulo = ET.SubElement(libroxml, 'titulo')
                titulo.text = libro.titulo
                cantidad = ET.SubElement(libroxml, 'cantidad')
                cantidad.text = str(car.cantidad)
            root.append(nuevo_alquiler)
            ET.indent(root, space='\t', level=0)
            tree.write('database/alquileres.xml', encoding='utf-8', xml_declaration=True)
        else:
            alquileresxml = ET.Element('alquileres')
            nuevo_alquiler = ET.SubElement(alquileresxml,'alquiler', numero=str(id_alquiler))
            usuario = getUsuario(id_user)
            user = ET.SubElement(nuevo_alquiler, 'usuario', id=id_user)
            user.text = usuario.nombre
            libros = ET.SubElement(nuevo_alquiler, 'libros')
            for car in carrito:
                libro = getlibro(car.idlibro)
                libroxml = ET.SubElement(libros, 'libro', id=libro.id)
                titulo = ET.SubElement(libroxml, 'titulo')
                titulo.text = libro.titulo
                cantidad = ET.SubElement(libroxml, 'cantidad')
                cantidad.text = str(car.cantidad)
            tree = ET.ElementTree(alquileresxml)
            ET.indent(tree, space='\t', level=0)
            tree.write('database/alquileres.xml', encoding='utf-8', xml_declaration=True)
            print('ya no')
        carrito.clear()
        return jsonify({
            'message': 'Libro agregado al alquiler',
            'status': 200
        }), 200
    except:
        return jsonify({
            'message': 'Error al agregar al alquiler',
            'status': 404
        }), 404

@BlueprintAlquiler.route('/alquiler/ver', methods=['GET'])
def verAlquiler():
    try:
        xml_salida = ''
        with open('database/alquileres.xml', 'r', encoding='utf-8') as file:
            xml_salida = file.read()
            file.close()
        return (xml_salida)
    except:
        return jsonify({
            'message': 'Error al ver el alquiler',
            'status': 404
        }), 404

def precargarAlquiler():
    alquileres = []
    if os.path.exists('database/alquileres.xml'):
        tree = ET.parse('database/alquileres.xml')
        root = tree.getroot()
        for alquiler in root:
            id = alquiler.attrib['numero']
            id_user = ''
            libros = []
            for elemento in alquiler:
                if elemento.tag == 'usuario':
                    id_user = elemento.attrib['id']
                if elemento.tag == 'libros':
                    for libro in elemento:
                        libros.append(Carro(libro.attrib['id'],libro.text))
            nuevo = Alquiler(id, id_user, libros)
            alquileres.append(nuevo)
    return alquileres