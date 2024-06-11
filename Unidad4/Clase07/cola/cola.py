import os

from cola.nodo import Nodo


class Cola:
    def __init__(self):
        self.primero = None
        self.tamanio = 0
    
    #METODOS DE COLA
    #1. METODO PARA INSERTAR UN ELEMENTO A LA COLA (ENQUEUE)
    def enqueue(self, dato):
        nuevo = Nodo(dato)
        if self.primero == None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual != None:
                if actual.siguiente == None:
                    actual.siguiente = nuevo
                    break
                actual = actual.siguiente
        self.tamanio += 1

    #2. METODO PARA ELIMINAR UN ELEMENTO DE LA COLA (DEQUEUE)
    def dequeue(self):
        if self.primero == None:
            print('Cola vacia')
            return None
        else:
            nodo_a_eliminar = self.primero
            self.primero = self.primero.siguiente
            self.tamanio -= 1
            return nodo_a_eliminar.dato
        
    #3. METODO PARA MOSTRAR EL PRIMERO DE LA COLA
    def verPrimero(self):
        if self.primero == None:
            print('Cola vacia')
            return None
        return self.primero.dato
    
    #4. OBTENER EL TAMAÑO DE LA COLA
    def __len__(self):
        return self.tamanio
    
    #5. METODO PARA MOSTRAR LA COLA EN CONSOLA
    def mostrar(self):
        if self.primero == None:
            print('Cola vacia')
            return
        actual = self.primero
        while actual != None:
            print(actual.dato)
            actual = actual.siguiente

    #6. METODO PARA SABER SI LA COLA ESTA VACIA
    def isEmpty(self):
        return self.primero == None
    
    #7. METODO PARA GRAFICAR LA COLA
    def graficar(self):
        codigodot = ''
        archivo = open('reportedot/cola.dot', 'w')
        codigodot += '''digraph G {
    rankdir="RL";
    label="Cola";
    node[shape=box];\n'''

        contador = 0
        actual = self.primero
        conexiones = ''
        nodos = ''
        while actual != None:
            nodos += 'Nodo'+str(contador)+'[style="filled", label="'+str(actual.dato)+'", fillcolor="green"];\n'
            if actual.siguiente != None:
                conexiones += 'Nodo'+str(contador+1) + ' -> Nodo'+str(contador)+';\n'
            contador += 1
            actual = actual.siguiente
        
        codigodot += nodos +"\n"+ conexiones + '\n}'

        #ESCRIBIMOS EN EL ARCHIVO
        archivo.write(codigodot)
        archivo.close()

        #GENERAMOS LA IMAGEN
        ruta_dot = 'reportedot/cola.dot'
        ruta_salida = 'reportes/cola.svg'
        comando = 'dot -Tsvg '+ruta_dot+' -o '+ruta_salida
        os.system(comando)
        #ABRIMOS LA IMAGEN
        #CONVIERTE LA RUTA RELATIVA EN ABSOLUTA
        ruta_salida2 = os.path.abspath(ruta_salida)
        os.startfile(ruta_salida2)