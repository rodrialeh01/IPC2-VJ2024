from cola.cola import Cola
from pila.pila import Pila

pila = Pila()
cola = Cola()

def menu_principal():
    opcion = 0
    while True:
        print('-----------------MENU PRINCIPAL-----------------')
        print('1. Menu de Pila')
        print('2. Menu de Cola')
        print('3. Salir')
        opcion = int(input('Seleccione una opcion: '))
        if opcion == 1:
            menu_pila()
        elif opcion == 2:
            menu_cola()
        elif opcion == 3:
            break
        else:
            print('Opcion no valida')

def menu_pila():
    global pila
    opcion = 0
    while True:
        print('-----------------MENU DE PILA-----------------')
        print('1. Push (numero)')
        print('2. Pop')
        print('3. Peek')
        print('4. Mostrar Pila en consola')
        print('5. Graficar Pila')
        print('6. Regresar')
        opcion = int(input('Seleccione una opcion: '))
        if opcion == 1:
            numero = int(input('Ingrese un numero: '))
            pila.push(numero)
        elif opcion == 2:
            salio = pila.pop()
            print(f'Salio el numero {salio}')
        elif opcion == 3:
            print('El numero en la cima es:', pila.peek())
        elif opcion == 4:
            pila.mostrar()
        elif opcion == 5:
            pila.graficar()
        elif opcion == 6:
            break
        else:
            print('Opcion no valida')

def menu_cola():
    global cola
    opcion = 0
    while True:
        print('-----------------MENU DE COLA-----------------')
        print('1. Enqueue (numero)')
        print('2. Dequeue')
        print('3. Mostrar el primero en la cola')
        print('4. Mostrar Cola en consola')
        print('5. Graficar Cola')
        print('6. Regresar')
        opcion = int(input('Seleccione una opcion: '))
        if opcion == 1:
            numero = int(input('Ingrese un numero: '))
            cola.enqueue(numero)
        elif opcion == 2:
            salio = cola.dequeue()
            print(f'Salio el numero {salio}')
        elif opcion == 3:
            print('El primero en la cola es:', cola.verPrimero())
        elif opcion == 4:
            cola.mostrar()
        elif opcion == 5:
            cola.graficar()
        elif opcion == 6:
            break
        else:
            print('Opcion no valida')


if __name__ == "__main__":
    menu_principal()