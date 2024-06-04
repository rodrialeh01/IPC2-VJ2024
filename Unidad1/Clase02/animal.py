#CREAMOS NUESTRA CLASE
class Animal:
    #CONSTRUCTOR
    def __init__(self,id, nombre, especie, altura, peso):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.altura = altura
        self.peso = peso

    #METODOS Y ENCAPSULAMIENTO

    def saludar(self):
        return "Hola, soy un animal!"

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getEspecie(self):
        return self.especie
    
    def setEspecie(self, especie):
        self.especie = especie

    def getAltura(self):
        return self.altura
    
    def setAltura(self, altura):
        self.altura = altura

    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso = peso

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id