class Usuario:
    def __init__(self, id, password, nombre, edad, email, telefono):
        self.id = id
        self.password = password
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f'ID: {self.id}\\n' \
            f'Password: {self.password}\\n' \
            f'Nombre: {self.nombre}\\n' \
            f'Edad: {self.edad}\\n' \
            f'Email: {self.email}\\n' \
            f'Telefono: {self.telefono}'