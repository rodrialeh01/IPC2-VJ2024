from animal import Animal


#HERENCIA -> class nombre_clase_hijo(nombre_clase_padre):
class Granja(Animal):
    def __init__(self, no_granja,id, nombre, especie, altura, peso):
        super().__init__(id,nombre, especie, altura, peso)
        self.no_granja = no_granja

    def saludar(self):
        return "Hola, soy un animal de granja!"

    def getNoGranja(self):
        return self.no_granja
    
    def setNoGranja(self, no_granja):
        self.no_granja = no_granja