from acuaticos import Acuatico
from granja import Granja

# LISTA GENERAL DE ANIMALES
animales = []
id_animales = 0

# MENU PRINCIPAL
def menuPrincipal():
    opcion = 0
    while True:
        print("----------------- Menu Principal -----------------")
        print("- 1. Crear animales de granja                    -")
        print("- 2. Crear animales acuaticos                    -")
        print("- 3. Ver todos los animales                      -")
        print("- 4. Editar atributos de un animal               -")
        print("- 5. Eliminar un animal                          -")
        print("- 6. Salir                                       -")
        print("--------------------------------------------------")
        opcion = input("Ingrese una opcion: ")
        try:
            opcion = int(opcion)
            match opcion:
                case 1:
                    crearAnimalGranja()
                case 2:
                    crearAnimalAcuatico()
                case 3:
                    verAnimales()
                case 4:
                    editarAnimal()
                case 5:
                    eliminarAnimal()
                case 6:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opcion no valida.")
        except:
            print("Opcion no valida, unicamente se aceptan enteros")


def crearAnimalGranja():
    global id_animales
    global animales
    print('----------------- CREAR ANIMAL DE GRANJA -----------------')
    id = id_animales
    no_granja = input('Ingrese el numero de la granja: ')
    nombre = input('Ingrese el nombre del animal: ')
    especie = input('Ingrese la especie del animal: ')
    altura = input('Ingrese la altura del animal: ')
    peso = input('Ingrese el peso del animal: ')
    nuevo = Granja(no_granja,id,nombre,especie,altura,peso)
    animales.append(nuevo)
    id_animales += 1

def crearAnimalAcuatico():
    global id_animales
    global animales
    print('----------------- CREAR ANIMAL ACUATICO -----------------')
    id = id_animales
    no_acuario = input('Ingrese el numero del acuario: ')
    tempagua = input('Ingrese la temperatura del agua: ')
    nombre = input('Ingrese el nombre del animal: ')
    especie = input('Ingrese la especie del animal: ')
    altura = input('Ingrese la altura del animal: ')
    peso = input('Ingrese el peso del animal: ')
    nuevo = Acuatico(no_acuario,tempagua,id,nombre,especie,altura,peso)
    animales.append(nuevo)
    id_animales += 1

def verAnimales():
    '''
    {
        atributo: loquecontiene,
        ...
    }
    '''
    global animales
    print('----------------- ANIMALES -----------------')
    if len(animales) == 0:
        print('No hay animales registrados.')

    for animal in animales:
        json_string = '''
{
    id: '''+str(animal.getId())+''',
    nombre: '''+animal.getNombre()+''',
    especie: '''+animal.getEspecie()+''',
    altura: '''+str(animal.getAltura())+''',
    peso: '''+str(animal.getPeso())+''',
    mensaje: '''+str(animal.saludar())+'''
}
'''
        print(json_string)
    
def editarAnimal():
    global animales
    id = input('Ingrese el id del animal a editar: ')
    #unicamente editaremos el nombre
    nombre = input('Ingrese el nuevo nombre del animal: ')
    for animal in animales:
        if animal.getId() == int(id):
            animal.setNombre(nombre)
            print('Nombre actualizado correctamente.')
            break

    print('Animal no encontrado.')

def eliminarAnimal():
    global animales
    id = input('Ingrese el id del animal a eliminar: ')
    for animal in animales:
        if animal.getId() == int(id):
            animales.remove(animal)
            print('Animal eliminado correctamente.')
            break

    print('Animal no encontrado.')

#MAIN
if __name__ == "__main__":
    menuPrincipal()

#PASS
'''
public static void mimetodo(){

}

def mimetodo():
    pass
'''