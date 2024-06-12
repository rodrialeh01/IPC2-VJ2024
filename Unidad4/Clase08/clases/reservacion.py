class Reservacion:
    def __init__(self, id, descripcion, libro, usuario, dia, hora):
        self.id = id
        self.descripcion = descripcion
        self.libro = libro
        self.usuario = usuario
        self.dia = dia
        self.hora = hora

    def __str__(self):
        return f'ID: {self.id}\n' \
            f'Descripción: {self.descripcion}\n' \
            f'Libro: {self.libro}\n' \
            f'Usuario: {self.usuario}\n' \
            f'Día: {str(self.dia)}\n' \
            f'Hora: {str(self.hora)}:00'