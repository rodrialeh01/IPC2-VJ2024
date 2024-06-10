from clases.cancion import Cancion
from lista_doble_circular.lista_doble_circular import ListaDobleCircular

lista = ListaDobleCircular()
id = 0

def menu():
    opcion = 0
    while True:
        print('1. Agregar Canción')
        print('2. Mostrar Lista en consola')
        print('3. Mostrar Lista en gráfica')
        print('4. Salir')
        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                agregar()
            case 2:
                mostrar()
            case 3:
                graficar()
            case 4:
                break
            case _:
                print('Opción no válida')

def agregar():
    global id
    nombre = input('Ingrese el nombre de la canción: ')
    artista = input('Ingrese el nombre del artista: ')
    pista = input('Ingrese la ruta de la pista: ')
    cancion = Cancion(id, nombre, artista, pista)
    lista.agregar(cancion)
    id += 1

def mostrar():
    lista.mostrar()

def graficar():
    lista.graficar()

if __name__ == '__main__':
    menu()