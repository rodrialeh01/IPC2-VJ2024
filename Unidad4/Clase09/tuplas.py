# MANEJO DE TUPLAS

#1. CREAR UNA TUPLA

#TUPLA VACIA
tupla_vacia = ()
print(tupla_vacia)

#TUPLA CON 1 ELEMENTO
tupla_un_elemento = (1,)
print(tupla_un_elemento)

#TUPLA CON VARIOS ELEMENTOS
tupla = (1, 2, 3, 4, 5)
print(tupla)

#TUPLA SIN PARENTESIS
tupla_sin_parentesis = 1, 2, 3, 4, 5
print(tupla_sin_parentesis)

#2. ACCEDER A LOS ELEMENTOS DE UNA TUPLA

#ACCEDER POR INDIVIDUAL

primero = tupla[0]
print(primero)

ultimo = tupla[-1]
print(ultimo)

#3. ITERAR SOBRE UNA TUPLA

print('---- ITERANDO SOBRE UNA TUPLA ----')
for numero in tupla:
    print(numero)


#4. CORTAR UNA TUPLA

#OBTENER UNA SUBTUPLA

subtupla = tupla[:3]
print(subtupla)

subtupla = tupla[1:3]
print(subtupla)

subtupla = tupla[3:]
print(subtupla)

#5. CONCATENAR TUPLAS
print('---- CONCATENAR TUPLAS ----')
tupla1 = ('hola', 'mundo')
tupla2 = ('introduccion', 'a', 'la', 'programacion', 'y', 'computacion', '2')
tupla3 = tupla1 + tupla2
print(tupla3)

#6. REPETIR UNA TUPLA

print('---- REPETIR UNA TUPLA ----')
tupla_prueba = (1,2)
tupla_resultado = tupla_prueba * 5
print(tupla_resultado)

#7. DESEMPAQUETAR TUPLAS
print('---- DESEMPAQUETAR TUPLAS ----')

#DESEMPAQUETANDO TODOS LOS ELEMENTOS
tupla = ('hola', 'mundo')
hola, mundo = tupla
print(hola)

#DESEMPAQUETANDO SOLO ALGUNOS ELEMENTOS
tupla = ('hola', 'mundo', 'como', 'estas')
hola, *resto = tupla

print(resto)

#8. COUNT
print('---- COUNT ----')
tupla = ('hola', 'hola', 'hola', 'adios', 'adios')
conteo = tupla.count('adios')
print(conteo)

#9. INDEX
print('---- INDEX ----')
tupla = ('hola', 'mundo', 'como', 'estas')
indice = tupla.index('hola')
print(indice)

#PRUEBA DE SI SE PUEDE MODIFICAR UNA TUPLA
tupla = ('ipc1', 'ipc2')
tupla[0] = 'IPC1'
print(tupla)