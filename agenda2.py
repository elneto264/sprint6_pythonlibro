#Agregar contacto
#Remover contacto
#actualizar contacto
#ver contacto
#ver todos los contactos

agenda_telefonica = dict()

print(" ----- Agenda telefónica ----- ")
print(" Bienvenido Mike0n a tu agenda telefonica")

def imprimir_operacion(nombre_operacion): 
    print()
    print("-------------------Agenda Telefonica------------------")
    print(nombre_operacion)
    print("------------------------------------------------------")
    print() 

def agregar_contacto():
    print()
    nombre = input("Nombre del contacto para añadir: ")
    numero = input("Numero del contacto para añadir: ")
    agenda_telefonica[nombre] = numero
    nombre_operacion = ("Contacto Agregado")
    imprimir_operacion(nombre_operacion)
    

def remover_contacto():
    print()
    nombre = input("Nombre del contacto que quiere borrar: ")
    nombre_operacion = None
    
    
    try:
        del agenda_telefonica[nombre]
    except KeyError:
        imprimir_operacion("Ese contacto no existe")
    else:
        imprimir_operacion("Contacto Borrado")

def actualizar_contacto():
    print()
    print("----- actualizar_contacto----------")
    print()
    nombre = input("Nombre del contacto que quiere actualizar: ")
    numero = input("nuevo numero de contacto: ")
    agenda_telefonica[nombre] = numero
    print()
    print("------- Numero actualizado -------------")
    print("-------------------------------")
    print()

def ver_contacto():
    print()
    print("----- ver contacto ----------")
    print()
    nombre = input("Nombre del contacto")
    print()
    nombre_operacion = None
    try:
        nombre_operacion = nombre + " - " + agenda_telefonica[nombre]
        imprimir_operacion(nombre_operacion)
    except KeyError:
        nombre_operacion = ("Ese nombre no existe")
        
        
def ver_todos_contacto():
    print()
    print("----- Lista de contactos----------")
    print()
    nombre_operacion = None
    
    if len(agenda_telefonica) == 0:
        nombre_operacion = ("No dispones de contactos en la agenda")
    else: 
        for contacto in agenda_telefonica:
            if nombre_operacion == None:
                nombre_operacion = "{} > >>>>>>> > {}".format(contacto,agenda_telefonica[contacto])
            else:
                nombre_operacion += "\n{} > >>>>>> > {}".format(contacto,agenda_telefonica[contacto])
                
    
    imprimir_operacion(nombre_operacion)
            
    print()
    print("-------------------------------")
    print()

while True:
    print("Estas son las operaciones que puedes realizar")
    print("1 - Agregar Contacto")
    print("2 - Remover Contacto")
    print("3 - Actualizar Contacto")
    print("4 - Ver Contacto")
    print("5 - Ver todos los contactos")
    print("6 - Salir")
    
    try:
        operacion = int(input(": "))
    except ValueError:
        print("-----------------------------------------")
        print("Selecciona una operacion valida del 1 al 6")
        print("-----------------------------------------")
    else: 
        if operacion == 1:
            agregar_contacto()
        elif operacion == 2:
            remover_contacto()
        elif operacion == 3:
            actualizar_contacto()
        elif operacion == 4:
            ver_contacto()
        elif operacion == 5:
            ver_todos_contacto()
        elif operacion == 6:
            break
        else:
            print("Operacion desconocida")

print()
print("Gracias por usar nuestra Lista de Contactos")
print("Vuelve Pronto! nos gusta trabajar contigo")