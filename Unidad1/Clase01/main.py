# Hola, soy un comentario simple

'''
Hola
soy 
un
comentario
de
multiples
lineas
:D
'''


# Declaracion de variables

ipc = "Introducción a la programación y computación"
DOS = 2
PI = 3.1416
esVerdadero = True

# Asignacion de variables

ipc = "Introducción a la programación y computación 2"
DOS = "Dos"

#print

#print con salto de linea
print("hola")
#print sin salto de linea
print("mundo", end="")
print("!")

#Input
nombre = input("Ingresa tu nombre: ")
print("Has ingresado tu nombre que es: " +  nombre)

#CONDICION IF
edad = 18
if (edad > 18):
    print("Eres mayor de edad")
elif (edad == 18):
    print("Tienes 18 años")
else:
    print("Eres menor de edad")

#CONDICION MATCH-CASE
dia = "Luness"

match dia:
    case "Lunes":
        print("Hoy es Lunes")
    case "Martes":
        print("Hoy es Martes")
    case "Miercoles":
        print("Hoy es Miercoles")
    case "Jueves":
        print("Hoy es Jueves")
    case "Viernes":
        print("Hoy es Viernes")
    case "Sabado":
        print("Hoy es Sabado")
    case "Domingo":
        print("Hoy es Domingo")
    case _:
        print("No es un dia de la semana")

#CICLO WHILE
contador = 0
while contador <=9:
    print(contador)
    contador += 1

print('-------------------')
#CICLO FOR
for contador in range(1,10):
    print(contador)

#FUNCIONES
def imprimirCurso():
    print("Estamos en IPC2")

def imprimirNombre(nombre):
    print("Tu nombre es: " + nombre)

def sumaDeDosNumeros(a,b):
    return a+b

#LLAMAR FUNCIONES
imprimirCurso()
imprimirNombre("Rodri")
print(sumaDeDosNumeros(5,6))