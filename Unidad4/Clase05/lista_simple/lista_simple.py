import os

from lista_simple.nodo import Nodo


class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    #len(milista)
    def __len__(self):
        return self.tamanio
    
    #INSERTAR -> INSERTAR AL FINAL DE LA LISTA
    def insertar(self, dato):
        #CREAMOS UN NODO
        nuevo = Nodo(dato)
        #VERIFICAMOS SI LA LISTA ESTÁ VACÍA
        if self.cabeza == None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual != None:
                if actual.siguiente == None:
                    actual.siguiente = nuevo
                    break
                actual = actual.siguiente
        self.tamanio += 1

    def imprimirlista(self):
        actual = self.cabeza
        while actual != None:
            print(actual.dato)
            actual = actual.siguiente

    def imprimirNombres(self):
        actual = self.cabeza
        while actual != None:
            print('------------------------')
            print('Nombre: ', actual.dato.nombre)
            actual = actual.siguiente

    def obtenerUsuario(self, id):
        actual = self.cabeza
        while actual != None:
            if actual.dato.id == id:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def eliminar(self, id):
        actual = self.cabeza
        anterior = None
        while actual != None:
            if actual.dato.id == id:
                if anterior == None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamanio -= 1
                break
            anterior = actual
            actual = actual.siguiente

    def graficar(self):
        codigodot = ''
        archivo = open('reportedot/lista_simple.dot', 'w')
        codigodot += '''digraph G {
  rankdir=LR;
  node [shape = record, height = .1]'''
        contador_nodos = 0
        #PRIMERO CREAMOS LOS NODOS
        actual = self.cabeza
        while actual != None:
            codigodot += 'node'+str(contador_nodos)+' [label = \"{'+ str(actual.dato)+'|<f1>}\"];\n'
            contador_nodos += 1
            actual = actual.siguiente

        #AHORA CREAMOS LAS RELACIONES
        actual = self.cabeza
        contador_nodos = 0
        while actual.siguiente != None:
            codigodot += 'node'+str(contador_nodos)+'-> node'+str(contador_nodos+1)+';\n'
            contador_nodos += 1
            actual = actual.siguiente

        codigodot += '}'

        #Lo escribimos en el archivo dot
        archivo.write(codigodot)
        archivo.close()

        #Generamos la imagen
        ruta_dot = 'reportedot/lista_simple.dot'
        ruta_reporte = 'reportes/lista_simple.png'
        comando = 'dot -Tpng '+ruta_dot+' -o '+ruta_reporte
        os.system(comando)
        #Abrir la imagen
        #CONVERTIR DE RUTA RELATIVA A RUTA ABSOLUTA
        ruta_abrir_reporte = os.path.abspath(ruta_reporte)
        os.startfile(ruta_abrir_reporte)
        print('Reporte generado con éxito')

    def autenticacion(self, id, password):
        actual = self.cabeza
        while actual != None:
            if actual.dato.id == id and actual.dato.password == password:
                return True
            actual = actual.siguiente
        return False