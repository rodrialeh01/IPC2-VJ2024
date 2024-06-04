from animal import Animal


class Acuatico(Animal):
    def __init__(self,no_acuario,tempagua,id, nombre, especie, altura, peso):
        super().__init__(id,nombre, especie, altura, peso)
        self.no_acuario = no_acuario
        self.tempagua = tempagua

    def saludar(self):
        return "Hola, soy un animal acuatico!"

    def getNoAcuario(self):
        return self.no_acuario
    
    def setNoAcuario(self, no_acuario):
        self.no_acuario = no_acuario

    def getTempAgua(self):
        return self.tempagua
    
    def setTempAgua(self, tempagua):
        self.tempagua = tempagua