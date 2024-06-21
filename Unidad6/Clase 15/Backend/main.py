from controllers.estructuras import libros, users
from controllers.librocontroller import BlueprintLibro, precargaLibros
from controllers.usercontroller import BlueprintUser, precargarUsuarios
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

#PARA PRECARGAR LA DATA
libros = precargaLibros()
users = precargarUsuarios()

#IMPRIMIMOS LA LONGITUD DE LAS LISTAS
print('Hay '+str(len(libros)) + ' libros')
print('Hay '+str(len(users)) + ' usuarios')

#REGISTRAMOS LOS BLUEPRINTS
app.register_blueprint(BlueprintLibro)
app.register_blueprint(BlueprintUser)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)