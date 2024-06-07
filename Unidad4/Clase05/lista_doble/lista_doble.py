import os

from lista_doble.nodo import Nodo


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio
    
    def insertar(self, dato):
        #CREAMOS NUESTRO NODO
        nuevo = Nodo(dato)
        #VERIFICAMOS SI LA LISTA ESTÁ VACÍA
        if self.cabeza == None and self.ultimo == None:
            self.cabeza = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo
        self.tamanio += 1

    def imprimirlista_desdeinicio(self):
        actual = self.cabeza
        while actual != None:
            print(actual.dato)
            actual = actual.siguiente

    def imprimirlista_alreves(self):
        actual = self.ultimo
        while actual != None:
            print(actual.dato)
            actual = actual.anterior

    def imprimirLibros(self):
        actual = self.cabeza
        while actual != None:
            print('---------------------------')
            print(str(actual.dato))
            actual = actual.siguiente

    def eliminar(self, id):
        actual = self.cabeza
        while actual != None:
            if actual.dato.id == id:
                if actual.anterior == None:
                    self.cabeza = actual.siguiente
                    if self.cabeza != None:
                        self.cabeza.anterior = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente != None:
                        actual.siguiente.anterior = actual.anterior
                self.tamanio -= 1
                break
            actual = actual.siguiente
    
    def obtenerLibro(self, id):
        actual = self.cabeza
        while actual != None:
            if actual.dato.id == id:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def graficar(self):
        codigo_dot = ''
        archivo = open('reportedot/lista_doble.dot', 'w')
        codigo_dot +='''digraph G {
  rankdir=LR;
  node [shape = record, height = .1]\n'''
        actual = self.cabeza
        contador_nodos = 0
        #PRIMERO CREAMOS LOS NODOS
        while actual != None:
            codigo_dot += 'node'+str(contador_nodos)+' [label = \"{<f1>| '+str(actual.dato)+'|<f2>}\"];\n'
            contador_nodos += 1
            actual = actual.siguiente

        #HACEMOS LAS RELACIONES
        actual = self.cabeza
        contador_nodos = 0
        while actual.siguiente != None:
            #RELACIONES DE IZQUIERDA A DERECHA
            codigo_dot += 'node'+str(contador_nodos)+':f2 -> node'+str(contador_nodos+1)+':f1;\n'
            #RELACIONES DE DERECHA A IZQUIERDA
            codigo_dot += 'node'+str(contador_nodos+1)+':f1 -> node'+str(contador_nodos)+':f2;\n'
            contador_nodos += 1
            actual = actual.siguiente

        codigo_dot += '}'

        archivo.write(codigo_dot)
        archivo.close()

        #GENERAMOS LA IMAGEN
        ruta_dot = 'reportedot/lista_doble.dot'
        ruta_imagen = 'reportes/lista_doble.png'
        comando = 'dot -Tpng '+ruta_dot+' -o '+ruta_imagen
        os.system(comando)

        #ABRIR LA IMAGEN
        #convierte la ruta a una ruta válida para windows
        ruta_reporte = os.path.abspath(ruta_imagen)
        os.startfile(ruta_reporte)