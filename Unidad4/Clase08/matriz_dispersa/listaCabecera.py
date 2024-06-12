class ListaCabecera:
    def __init__(self, tipo):
        self.tipo = tipo
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio
    
    def insertarNodoCabecera(self, nuevo):
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            #----------INSERCION EN ORDEN ASCENDENTE----------
            #-- VERTIFICAMOS SI EL NUEVO NODO ES MENOR QUE EL PRIMER
            if nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            #-- VERIFICAMOS SI EL NUEVO NODO ES MAYOR QUE EL ULTIMO NODO
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            #-- SINO, RECORREMOS LA LISTA PARA BUSCAR DONDE ACOMODAR EL NUEVO NODDO CABECERA QUE SE UBICA ENTRE EL PRIMERO Y EL ULTIMO
            else:
                actual = self.primero
                while actual != None:
                    if nuevo.id < actual.id:
                        nuevo.siguiente = actual
                        nuevo.anterior = actual.anterior
                        actual.anterior.siguiente = nuevo
                        actual.anterior = nuevo
                        break
                    elif nuevo.id > actual.id:
                        actual = actual.siguiente
                    else:
                        break
        self.tamanio += 1


    def obtenerCabecera(self, id):
        actual = self.primero
        while actual != None:
            if actual.id == id:
                return actual
            actual = actual.siguiente
        return None
    
    def mostrarCabeceras(self):
        actual = self.primero
        while actual != None:
            print(actual.id)
            actual = actual.siguiente