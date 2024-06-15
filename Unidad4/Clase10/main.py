# MANEJO DE EXPRESIONES REGULARES

#1. IMPORTAR EL MÓDULO RE
import re

#2. COINCIDENCIA SIMPLE

#Patron
#LITERAL
patron = r'python'

cadena = 'los alumnos de ipc2 estan aprendiendo el lenguaje de programacion python'

#Buscamos la coincidencia
coincidencia = re.search(patron, cadena)

if coincidencia:
    print('Se encontró la coincidencia')
    print(coincidencia.group())
else:
    print('No se encontró la coincidencia')

#USANDO METACARECTERES
patron = r'[0-9]'

cadena = 'los alumnos de ipc2 estan aprendiendo el lenguaje de programacion python'

#Buscamos la coincidencia
coincidencia = re.search(patron, cadena)

if coincidencia:
    print('Se encontró la coincidencia')
    print(coincidencia.group())
else:
    print('No se encontró la coincidencia')

#USANDO RANGO DE LETRAS
patron = r'[a-zñ]' #a|b|c|d|e|f|g|h|i|j|k|l|m|n|ñ|o|p|q|r|s|t|u|v|w|x|y|z
cadena = 'ñ'

#Buscamos la coincidencia
coincidencia = re.search(patron, cadena)
if coincidencia:
    print('Se encontró la coincidencia')
    print(coincidencia.group())
else:
    print('No se encontró la coincidencia')

#CON METACARACTERES ITERADORES
patron = r'a+'
cadena = 'aaaaaaaaaaaaaaaaaaaaaaayud'
coincidencia = re.search(patron, cadena)
if coincidencia:
    print('Se encontró la coincidencia')
    print(coincidencia.group())
else:
    print('No se encontró la coincidencia')

#PONGAMOLO MAS COMPLEJO - RECONOCIENDO DECIMALES Y ENTEROS
patron = r'[0-9]+(\.[0-9]+)?'
cadena = '50248465184.10 25'
coincidencia = re.search(patron, cadena)
if coincidencia:
    print('Se encontró la coincidencia')
    print(coincidencia.group())
else:
    print('No se encontró la coincidencia')

#3. COINCIDENCIA MULTIPLE O MEJOR DICHO ENCONTRAR TODAS LAS COINCIDENCIAS
patron = r'[0-9]+(\.[0-9]+)?'

cadena = '25 a 356 a 1.25 a 25.6 a 25.6'
coincidencias = re.findall(patron, cadena)
print(coincidencias)

patron = r'\bP\w+'
cadena = 'Python es un lenguaje de programación y PyPI es un repositorio.'

# Encontrar todas las coincidencias
coincidencias = re.findall(patron, cadena)
print('Todas las coincidencias:', coincidencias)

#4. CORREO ELECTRONICO
patron = r'(\w+)@(\w+\.\w+)'

cadena = 'mi correo es usuario@gmail.com'

coincidencia = re.search(patron, cadena)

if coincidencia:
    print('Se encontró la coincidencia')
    print(coincidencia.group(1))
    print(coincidencia.group(2))

#PATRON DE UNA IP
patron = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

cadena = '255.255.255.255'

if re.fullmatch(patron, cadena):
    print('La cadena es una IP')
else:
    print('La cadena no es una IP')