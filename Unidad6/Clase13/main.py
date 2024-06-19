from clases.usuario import Usuario
from estructuras.estructuras import lista_usuarios
from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS

#CREAMOS LA API DE FLASK
app = Flask(__name__)
#añadimos CORS
#cors = CORS(app, origins=True, allow_headers=['Content-Type', 'Authorization'], supports_credentials=True)
cors = CORS(app)

#CREAMOS UN ENDPOINT DE BIENVENIDA
@app.route('/')
def index():
    return '<h1>Bienvenido a mi api de la clase 13 IPC2</h1><br\\> <p>Usando Backend con Python y Flask</p>'

#ENDPOINT PARA CREAR UN USUARIO = CREATE
@app.route('/usuario/crear', methods=['POST'])
def crear_usuario():
    if request.method == 'POST':
        try:
            nombre = request.json['nombre']
            username = request.json['username']
            password = request.json['password']
            nuevo = Usuario(nombre, username, password)
            lista_usuarios.append(nuevo)
            return jsonify({
                'message':'Usuario creado con éxito',
                'status': 200
            }),200
        except KeyError as e:
            return jsonify({
                'message':f'Falta el atributo: {e}',
                'status': 400
            }),400
        except Exception as e:
            return jsonify({
                'message': f'Error al procesar la solicitud en el servidor: {str(e)}',
                'status': 400
            }),400
        
#ENPOINT PARA VER TODOS LOS USUARIOS = READ
@app.route('/usuario/ver', methods=['GET'])
def verUsuarios():
    if request.method == 'GET':
        diccionario_respuesta = {
            'message':'Lista de usuarios',
            'usuarios':[],
            'status':200
        }
        for user in lista_usuarios:
            diccionario_respuesta['usuarios'].append({
                'nombre': user.nombre,
                'username': user.username,
                'password': user.password
            })
        return jsonify(diccionario_respuesta), 200
    
#ENDPOINT PARA ACTUALIZAR UN USUARIO = UPDATE
@app.route('/usuario/actualizar/<string:username>', methods=['PUT'])
def actualizarUsuario(username):
    if request.method == 'PUT':
        try:
            nombre = request.json['nombre']
            password = request.json['password']
            for user in lista_usuarios:
                if user.username == username:
                    user.nombre = nombre
                    user.password = password
                    return jsonify({
                        'message': 'Usuario actualizado correctamente',
                        'status': 200
                    })
            return jsonify({
                'message': 'El usuario que agregó, no se encuentra en el sistema',
                'status': 400
            })
        except KeyError as e:
            return jsonify({
                'message':f'Falta el atributo: {e}',
                'status': 400
            }),400
        except Exception as e:
            return jsonify({
                'message': f'Error al procesar la solicitud en el servidor: {str(e)}',
                'status': 400
            }),400
        
#ACTUALIZAR CAMBIOS MINIMOS = PATCH
@app.route('/usuario/actualizar/password/<string:username>', methods=['PATCH'])
def actualizarContrasenia(username):
    if request.method == 'PATCH':
        try:
            password = request.json['password']
            for user in lista_usuarios:
                if user.username == username:
                    user.password = password
                    return jsonify({
                        'message': 'Contraseña actualizada correctamente',
                        'status': 200
                    })
            return jsonify({
                'message': 'El usuario que agregó, no se encuentra en el sistema',
                'status': 400
            })

        except KeyError as e:
            return jsonify({
                'message':f'Falta el atributo: {e}',
                'status': 400
            }),400
        except Exception as e:
            return jsonify({
                'message': f'Error al procesar la solicitud en el servidor: {str(e)}',
                'status': 400
            }),400
        
#ENDPOINT PARA ELIMINAR UN USUARIO = DELETE
@app.route('/usuario/eliminar/<string:username>', methods=['DELETE'])
def eliminarUsuario(username):
    if request.method == 'DELETE':
        try:
            for user in lista_usuarios:
                if user.username == username:
                    lista_usuarios.remove(user)
                    return jsonify({
                        'message':'Usuario eliminado correctamente',
                        'status':200
                    })
            return jsonify({
                'message':'El usuario que intenta eliminar no existe',
                'status':400
            })
        except Exception as e:
            return jsonify({
                'message': f'Error al procesar la solicitud en el servidor: {str(e)}',
                'status': 400
            }),400

@app.route('/auth/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.json['username']
            password = request.json['password']
            if username == 'AdminIPC2' and password == 'IPC2VJ2024':
                return jsonify({
                    'message': 'Usuario logueado correctamente',
                    'role': 1,
                    'status': 200
                })
            for user in lista_usuarios:
                if user.username == username and user.password == password:
                    return jsonify({
                        'message': 'Usuario logueado correctamente',
                        'role': 2,
                        'status': 200
                    })
            return jsonify({
                'message': 'Usuario o contraseña incorrectos',
                'status': 400
            })
        except KeyError as e:
            return jsonify({
                'message':f'Falta el atributo: {e}',
                'status': 400
            }),400
        except Exception as e:
            return jsonify({
                'message': f'Error al procesar la solicitud en el servidor: {str(e)}',
                'status': 400
            }),400

#MANEJO GENERICO DE ERRORES 404 PARA CUANDO LA RUTA NO EXISTE
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'message':'La ruta solicitada no existe',
        'status':404
    }),404

#MANEJO GENERICO DE ERRORES 405 PARA CUANDO EL METODO NO ESTA PERMITIDO
@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        'message':'El método solicitado no está permitido',
        'status':405
    }),405

if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)