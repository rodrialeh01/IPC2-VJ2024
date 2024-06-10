import os

from lista_doble_circular.nodo import Nodo


class ListaDobleCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio
    
    def agregar(self, dato):
        nuevo = Nodo(dato)
        # Si esta vacia la lista
        if self.primero == None and self.ultimo == None:
            self.primero = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
        # Si la lista tiene mínimo 1 elemento
        else:
            # 1. El siguiente del ultimo nodo es el nuevo nodo
            self.ultimo.siguiente = nuevo
            # 2. El anterior del nuevo nodo es el ultimo nodo
            nuevo.anterior = self.ultimo
            # 3. El ultimo nodo es el nuevo nodo
            self.ultimo = nuevo
            # 4. El siguiente del ultimo nodo es el primer nodo
            self.ultimo.siguiente = self.primero
            # 5. El anterior del primer nodo es el ultimo nodo
            self.primero.anterior = self.ultimo
        self.tamanio += 1

    # MOSTRAR LISTA
    def mostrar(self):
        contador = 0
        actual = self.primero
        while contador < self.tamanio:
            print(actual.dato)
            actual = actual.siguiente
            contador += 1

    def mostrar_ciclo(self):
        actual = self.primero
        while actual != None:
            print(actual.dato)
            actual = actual.siguiente
    
    def reversa(self):
        contador = 0
        actual = self.ultimo
        while contador < self.tamanio:
            print(actual.dato)
            actual = actual.anterior
            contador += 1

    # OBTENER EL DATO DE UN NODO
    def obtenerDato (self, dato):
        actual = self.primero
        contador = 0
        while contador < self.tamanio:
            if actual.dato == dato:
                return actual.dato
            actual = actual.siguiente
            contador += 1
        return None
    
    # OBTENER UN OBJETO NODO
    def obtenerNodo(self, id):
        contador = 0
        actual = self.primero
        while contador < self.tamanio:
            if actual.dato.id == id:
                return actual
            actual = actual.siguiente
            contador += 1
        return

    # GRAFICAR LA LISTA
    def graficar(self):
        codigodot = ''
        archivo = open('reportedot/lista_doble_circular.dot', 'w')
        codigodot+= '''digraph G {
  rankdir=LR;
  node [shape = record, height = .1]\n'''
        #PRIMERO CREAMOS LOS NODOS
        actual = self.primero
        contador = 0
        while contador < self.tamanio:
            codigodot+='node'+str(contador)+' [label = "{<f1>|'+str(actual.dato)+'|<f2>}"];\n'
            actual = actual.siguiente
            contador += 1

        #AHORA CREAMOS LOS APUNTADORES
        contador = 0
        actual = self.primero
        while contador < self.tamanio-1:
            codigodot += 'node'+str(contador)+':f2  -> node'+str(contador+1)+':f1[dir=both];\n'
            contador += 1
            actual = actual.siguiente
        
        #CREAMOS LOS APUNTADORES DE LOS EXTREMOS
        codigodot += 'node0:f1 -> node'+str(self.tamanio-1)+':f2 [dir=both constraint=false];\n'

        codigodot += '}'

        #ESCRIBIR EL ARCHIVO .DOT
        archivo.write(codigodot)
        archivo.close()

        #GENERAMOS LA IMAGEN
        ruta_dot = 'reportedot/lista_doble_circular.dot'
        ruta_png = 'reportes/lista_doble_circular.png'
        comando = 'dot -Tpng '+ruta_dot+' -o '+ruta_png
        os.system(comando)

        #ABRIMOS LA IMAGEN
        #convierte la ruta relativa a absoluta
        ruta_salida = os.path.abspath(ruta_png)
        os.startfile(ruta_salida)
