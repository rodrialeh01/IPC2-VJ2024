class Cancion:
    def __init__(self,id, nombre, pista, artista):
        self.id = id
        self.nombre = nombre
        self.pista = pista
        self.artista = artista

    def __str__(self):
        return f'ID: {self.id}\\n' \
            f'Nombre: {self.nombre}\\n' \
            f'Pista: {self.pista}\\n' \
            f'Artista: {self.artista}'