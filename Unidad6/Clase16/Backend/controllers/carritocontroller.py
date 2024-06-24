from controllers.librocontroller import getlibro
from flask import Blueprint, jsonify, request
from models.carro import Carro

BlueprintCarro = Blueprint('carro', __name__)
carrito = []
@BlueprintCarro.route('/carro/agregar', methods=['POST'])
def agregarcarro():
    try:
        #OBTENEMOS EL JSON
        json_entrada = request.json
        print(json_entrada)
        if json_entrada == '':
            return jsonify({
                'message': 'Error al agregar al carro: EL JSON está vacio',
                'status': 404
            }), 404
        #LEER EL JSON
        idlibro = json_entrada['idlibro']
        cantidad = json_entrada['cantidad']
        nuevo = Carro(idlibro, cantidad)
        carrito.append(nuevo)
        return jsonify({
            'message': 'Libro agregado al carro',
            'status': 200
        }), 200
    except:
        return jsonify({
            'message': 'Error al agregar al carro',
            'status': 404
        }), 404
    
@BlueprintCarro.route('/carro/ver', methods=['GET'])
def vercarro():
    try:
        contenido = '<carrito>\n'
        for car in carrito:
            libro = getlibro(car.idlibro)
            contenido += '\t<libro id="'+str(libro.id)+'">\n'
            contenido += '\t\t<titulo>'+libro.titulo+'</titulo>\n'
            contenido += '\t\t<cantidad>'+str(car.cantidad)+'</cantidad>\n'
            contenido += '\t</libro>\n'
        contenido += '</carrito>'
        return jsonify({
            'message': 'Carro',
            'status': 200,
            'contenido': contenido
        }), 200
    except:
        return jsonify({
            'message': 'Error al ver el carro',
            'status': 404
        }), 404