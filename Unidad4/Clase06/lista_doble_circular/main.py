from lista_doble_circular import ListaDobleCircular

lista = ListaDobleCircular()

lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
lista.agregar(7)
lista.agregar(8)
lista.agregar(9)
lista.agregar(10)

lista.reversa()
print('--------------------')
lista.mostrar()
print('--------------------')
print(lista.obtenerDato(3))

lista.graficar()