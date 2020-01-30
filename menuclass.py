from testmerge import Libro
from limpiar import Limpieza
print("*********************************************") 
print("*                                           *")
print("*  ¡Bienvenidos a la Biblioteca Open Mind!  *")
print("*                                           *")
print("*********************************************")
l1 = Libro()
la = Limpieza()
class Menu:
    def menu(): 
        print ("Selecciona una opción")
        print ("\t1 - Consultar listado")
        print ("\t2 - Agregar libro al listado")
        print ("\t3 - Salir")
    while True:
        menu()
    
        opcionMenu = input("inserta un numero valor >> ")
    
        if opcionMenu=="1":
            print ("")
            input("Has pulsado la opción 1...\npulsa una tecla para continuar")
            la.clean()
            f = open("text.txt", "r")
            print(f.read())
            print("****************************************")
           

        elif opcionMenu=="2":
            print ("")
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")
            l1.agregar(l1.titulo,l1.autor)

        elif opcionMenu=="3":
            f.close()
            break
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")