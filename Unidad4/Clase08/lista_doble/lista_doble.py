import os

from lista_doble.nodo import Nodo


class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo
        self.tamano += 1

    def mostrar(self):
        actual = self.primero
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente
        
    def buscar(self, id):
        actual = self.primero
        while actual is not None:
            if actual.dato.id == id:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def eliminar(self, dato):
        actual = self.primero
        while actual is not None:
            if actual.dato == dato:
                if actual.anterior is None:
                    self.primero = actual.siguiente
                else:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente is None:
                    self.ultimo = actual.anterior
                else:
                    actual.siguiente.anterior = actual.anterior
                return True
            actual = actual.siguiente
        self.tamano -= 1
        return False
    
    def eliminar_primero(self):
        if self.primero is not None:
            self.primero = self.primero.siguiente
            if self.primero is not None:
                self.primero.anterior = None
            else:
                self.ultimo = None
            return True
        return False
    
    def eliminar_ultimo(self):
        if self.ultimo is not None:
            self.ultimo = self.ultimo.anterior
            if self.ultimo is not None:
                self.ultimo.siguiente = None
            else:
                self.primero = None
            return True
        return False
    
    def graficar(self):
        contenido = ''
        archivo = open('reportedot/lista_doble.dot', 'w')
        actual = self.primero
        contenido += '''digraph G {
  rankdir=LR;
  node [shape = record, height = .1]\n'''
        contador_nodos = 0
        #PRIMERO CREAMOS LOS NODOS
        while actual != None:
            contenido +='node'+str(contador_nodos)+' [label = \"{<f1>| '+str(actual.dato)+'|<f2>}\"];\n'
            contador_nodos += 1
            actual = actual.siguiente

        #HACEMOS LAS RELACIONES
        actual = self.primero
        contador_nodos = 0
        while actual.siguiente != None:
            #DE IZQUIERDA A DERECHA
            contenido += 'node'+str(contador_nodos)+':f2 -> node'+str(contador_nodos+1)+':f1;\n'
            #DE DERECHA A IZQUIERDA
            contenido += 'node'+str(contador_nodos+1)+':f1 -> node'+str(contador_nodos)+':f2;\n'
            contador_nodos += 1
            actual = actual.siguiente
        contenido += '}'

        archivo.write(contenido)
        archivo.close()

        #Generamos la imagen
        ruta_dot = 'reportedot/lista_doble.dot'
        ruta_reporte = 'reportes/lista_doble.png'
        comando = 'dot -Tpng '+ruta_dot+' -o '+ruta_reporte
        os.system(comando)
        #Abrimos la imagen
        #convierte la ruta relativa a absoluta
        ruta_reporte2 = os.path.abspath(ruta_reporte)
        os.startfile(ruta_reporte2)