import os

from pila.nodo import Nodo


class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    #METODOS DE PILA
    #1. METODO DE INSERTAR UN ELEMENTO A LA PILA (PUSH)
    def push(self, dato):
        #1. CREAMOS UN NODO
        nuevo = Nodo(dato)
        #2. Nuevo nodo va a tener apuntando a la cima
        nuevo.abajo = self.cima
        #3. ACTUALIZAMOS LA CIMA
        self.cima = nuevo
        #4. ACTUALIZAMOS EL TAMAÑO DE LA PILA
        self.tamanio += 1

    #2. METODO DE ELIMINAR UN ELEMENTO DE LA PILA (POP)
    def pop(self):
        if self.cima == None:
            print('Pila vacia')
            return None
        nodo_a_eliminar = self.cima
        self.cima = self.cima.abajo
        self.tamanio -= 1
        return nodo_a_eliminar.dato
    
    #3. METODO PARA MOSTRAR EL ELEMENTO QUE ESTA EN LA CIMA DE LA PILA (PEEK)
    def peek(self):
        if self.cima == None:
            print('Pila vacia')
            return None
        return self.cima.dato
    
    #4. METODO PARA VER SI ESTA VACIA LA PILA
    def isEmpty(self):
        return self.cima == None
    
    #5. METODO PARA MOSTRAR EL TAMAÑO DE LA PILA
    def __len__(self):
        return self.tamanio
    
    #6. METODO PARA MOSTRAR LA PILA EN CONSOLA
    def mostrar(self):
        if self.isEmpty():
            print('Pila vacia')
            return
        actual = self.cima
        while actual != None:
            print(actual.dato)
            actual = actual.abajo

    #7. METODO PARA GRAFICAR LA PILA
    def graficar(self):
        codigodot = ''
        archivo = open('reportedot/pila.dot', 'w')
        codigodot += '''digraph G {
    rankdir=LR;
    node[shape=Mrecord];\n'''
        nodos = 'Nodo[xlabel = Pila label = "'
        #GRAFICAMOS LOS NODOS
        actual = self.cima
        while actual != None:
            if actual.abajo != None:
                nodos+= str(actual.dato) + '|'
            else:
                nodos+= str(actual.dato)
            actual = actual.abajo
        nodos+= '"];\n'
        codigodot+= nodos+"}"

        #GENERAMOS EL DOT
        archivo.write(codigodot)
        archivo.close()

        #GENERAMOS LA IMAGEN
        ruta_dot = 'reportedot/pila.dot'
        ruta_salida = 'reportes/pila.svg'
        comando = 'dot -Tsvg '+ruta_dot+' -o '+ruta_salida
        os.system(comando)
        #ABRIMOS LA IMAGEN
        #convierte la ruta relativa en absoluta
        ruta_salida2 = os.path.abspath(ruta_salida)
        #COMANDO PARA ABRIR LA IMAGEN
        os.startfile(ruta_salida2)

    #METODO PARA RETORNAR MI PILA COMO UN STRING
    def retornarpila(self):
        cadena = ''
        actual = self.cima
        while actual != None:
            cadena += str(actual.dato) + ', '
            actual = actual.abajo
        return cadena