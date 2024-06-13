# MANEJO DE FICHEROS

#1. MÉTODO DE LECTURA DE FICHEROS
print('------ LECTURA DE ARCHIVOS ------')
with open('entrada.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print(contenido)

#2. MÉTODO DE ESCRITURA DE FICHEROS
print('------ ESCRITURA DE ARCHIVOS ------')
with open('escritura.py', 'w') as archivo:
    contenido = 'print("Hola Mundo!!!!!!!!!")\nprint("si funciona :D")'
    archivo.write(contenido)
    print('Archivo creado con éxito')

#3. MÉTODO PARA AÑADIR TEXTO A UN FICHERO
print('------ AÑADIR TEXTO A UN ARCHIVO ------')
with open('entrada.txt', 'a') as archivo:
    contenido = '\nAcabo de agregar mas texto a mi archivo desde python'
    archivo.write(contenido)
    print('Texto añadido con éxito')

#4. MÉTODO PARA UN ARCHIVO EN MODO LECTURA Y ESCRITURA
print('------ LECTURA Y ESCRITURA DE ARCHIVOS ------')
with open('entrada.txt', 'r+', encoding='utf8') as archivo:
    contenido = archivo.read()
    print('Antes de que añada texto: '+ contenido)
    extra = '\nAcabo de concatenar texto con mi contenido actual'
    salida = contenido + extra
    print('Mi salida ahora va a ser: '+ salida)
    archivo.write(salida)
    print('Texto añadido con éxito')

#LEER EN UN PUNTO ESPECIFICO DEL ARCHIVO 
print('------ LECTURA EN UN PUNTO ESPECIFICO DEL ARCHIVO ------')
with open('entrada.txt', 'a+', encoding='utf-8') as archivo:
    #ubicamos donde quiero escribir
    archivo.write('prueba ')
    archivo.seek(5)
    contenido = archivo.read()
    print(contenido)
    print('Texto añadido con éxito')

#ESCRIBIR EN UN PUNTO ESPECIFICO
print('------ ESCRITURA EN UN PUNTO ESPECIFICO DEL ARCHIVO ------')
with open('entrada.txt', 'r+', encoding='utf-8') as archivo:
    archivo.seek(5)
    archivo.write('prueba ')
    print('Texto añadido con éxito')

# LEER UN ARCHIVO LINEA POR LINEA
with open('entrada.txt', 'r', encoding='utf-8') as archivo:
    contador = 0
    for linea in archivo:
        contador += 1
    print('El archivo tiene '+str(contador)+' lineas')