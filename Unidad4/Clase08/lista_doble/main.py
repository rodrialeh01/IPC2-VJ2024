from lista_doble import ListaDoble

lista = ListaDoble()

lista.agregar(1)    
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)

lista.mostrar()
lista.graficar()

print('-')
lista.eliminar(3)
lista.mostrar()

print('-')
lista.eliminar(1)
lista.mostrar()

print('-')
lista.eliminar(5)
lista.mostrar()