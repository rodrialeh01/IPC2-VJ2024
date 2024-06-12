import os

from lista_circular.nodo import Nodo


class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0

    def agregar(self, dato):
        nuevo = Nodo(dato)
        # Si la lista está vacía
        if self.primero is None and self.ultimo is None:
            self.primero = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
        # Si la lista tiene al menos un elemento
        else:
            # El siguiente del último nodo es el nuevo nodo
            self.ultimo.siguiente = nuevo
            # El ultimo nodo es el nuevo nodo
            self.ultimo = nuevo
            # El siguiente del último nodo es el primero
            self.ultimo.siguiente = self.primero
        self.tamano += 1

    def mostrar(self):
        if self.primero is None:
            print("La lista está vacía")
        else:
            actual = self.primero
            contador = 0
            while contador < self.tamano:
                print(actual.dato)
                actual = actual.siguiente
                contador += 1

    def buscar(self, id):
        if self.primero is None:
            return None
        else:
            actual = self.primero
            contador = 0
            while contador < self.tamano:
                if actual.dato.id == id:
                    return actual.dato
                actual = actual.siguiente
                contador += 1
            return None

    def graficar(self):
        contenido = ''
        archivo = open('reportedot/lista_circular.dot', 'w')
        actual = self.primero
        contenido += '''digraph G {
  rankdir=LR;
  node [shape = record, height = .1]\n'''
        contador_nodos = 0
        #PRIMERO CREAMOS LOS NODOS
        while contador_nodos < self.tamano:
            contenido +='node'+str(contador_nodos)+' [label = \"{'+str(actual.dato)+'|<f1>}\"];\n'
            actual = actual.siguiente
            contador_nodos += 1

        #AHORA CREAMOS LAS RELACIONES
        actual = self.primero
        contador_nodos = 0
        while contador_nodos < self.tamano-1:
            contenido += 'node'+str(contador_nodos)+' -> node'+str(contador_nodos+1)+';\n'
            contador_nodos += 1
            actual = actual.siguiente
        
        #AGREGAMOS LA RELACIÓN DEL NOODO FINAL CON EL PRIMERO Y SE PONE CURVADO
        contenido += 'node'+str(contador_nodos)+' -> node0 [constraint=false];\n'

        contenido += '}'

        #Lo escribimos en el archivo
        archivo.write(contenido)
        archivo.close()

        #Generamos la imagen
        ruta_dot = 'reportedot/lista_circular.dot'
        ruta_reporte = 'reportes/lista_circular.png'
        comando = 'dot -Tpng '+ruta_dot+' -o '+ruta_reporte
        os.system(comando)
        #Abrimos la imagen
        #convierte la ruta relativa a absoluta
        ruta_reporte2 = os.path.abspath(ruta_reporte)
        os.startfile(ruta_reporte2)
