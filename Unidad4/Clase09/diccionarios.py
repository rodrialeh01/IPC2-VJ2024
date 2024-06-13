# MANEJO DE DICCIONARIOS

#1. CREACIÓN DE UN DICCIONARIO
#DICCIONARIO VACIO
diccionario_nuevo = {}

#DICCIONARIO CON DATOS INICIALES
mi_diccionario = {
    'nombre': 'Rodri',
    'username': 'rodrialeh',
    'edad': 23,
    'pais': 'Guatemala'
}

#2. ACCESO A LOS ELEMENTOS DE UN DICCIONARIO - VALORES
print('------ ACCESO A LOS ELEMENTOS DE UN DICCIONARIO ------')
nombre = mi_diccionario['edad']
print(nombre)

#3. MODIFICAR LOS VALORES
mi_diccionario['nombre'] = 'Rodrigo'
print(mi_diccionario)

#4. AÑADIR UN NUEVO CLAVE-VALOR
print('---- AÑADIENDO ELEMENTOS AL DICCIONARIO ----')
mi_diccionario['apellido'] = 'Hernández'
mi_diccionario['carrera'] = 'Ing. Ciencias y Sistemas'


clave = 'cursos'
valor = [
    {
        'curso': 'IPC1'
    },
    {
        'curso': 'IPC2'
    }
]
mi_diccionario[clave] = valor
print(mi_diccionario)

#5. ELIMINAR UN CLAVE-VALOR
print('---- ELIMINANDO ELEMENTOS DEL DICCIONARIO ----')
del mi_diccionario['cursos']
print(mi_diccionario)

#6. ITERAR SOBRE UN DICCIONARIO
print('---- ITERANDO SOBRE UN DICCIONARIO ----')
for clave in mi_diccionario:
    print(clave + ' : ' + str(mi_diccionario[clave]))

#7. ITERAR SOBRE LOS VALORES
print('---- ITERANDO SOBRE LOS VALORES DE UN DICCIONARIO ----')
for valor in mi_diccionario.values():
    print(valor)

print('---- ITERANDO SOBRE LOS VALORES DE UN DICCIONARIO ----')
for clave, valor in mi_diccionario.items():
    print(clave, str(valor))

#8. COMPROBAR SI EXISTE UNA CLAVE
if 'cursos' in mi_diccionario:
    print('La clave cursos existe')
else:
    print('La clave cursos no existe')

#9. GET
#OBTENER EL VALOR DE NOMBRE
print('---- OBTENER EL VALOR DE UNA CLAVE ----')
nombre = mi_diccionario.get('nombre')
print(nombre)
#para excepciones
cursos = mi_diccionario.get('cursos', 'No existe esa clave')
print(cursos)

#10. KEYS
claves = mi_diccionario.keys()
print(claves)

#11. VALUES
valores = mi_diccionario.values()
print(valores)

#12. ITEMS
items = mi_diccionario.items()
print(items)

#13. LIMPIAR EL DICCIONARIO
mi_diccionario.clear()
print(mi_diccionario)