class Libro:
    def __init__(self, id, titulo, autor, precio, imagen):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.imagen = imagen
    
    def __str__(self):
        return f'ID: {self.id}\\n' \
            f'Título: {self.titulo}\\n' \
            f'Autor: {self.autor}\\n' \
            f'Precio: {self.precio}\\n' \
            f'Imagen: {self.imagen}'