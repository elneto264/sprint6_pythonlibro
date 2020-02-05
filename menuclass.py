from testmerge import Libro
from limpiar import Limpieza
#validacion de libro, consultar la informacion especifica de un libro, eliminar un libro en especifico, 


class Menu:
    def menu(self):
        print("*********************************************") 
        print("*                                           *")
        print("*  ¡Bienvenidos a la Biblioteca Open Mind!  *")
        print("*                                           *")
        print("*********************************************")
        la = Limpieza()
        print ("Selecciona una opción")
        la.clean()
        print ("\t1 - Consultar listado")
        print ("\t2 - Agregar libro al listado ")
        print ("\t3 - Validar el libro ")
        print ("\t4 - Consultar libro ")
        print ("\t5 - Eliminar libro ")
        print ("\t6 - Salir")
        l1 = Libro()
        
    def todo(self):
        l1 = Libro()
        la = Limpieza()
        while True:
            self.menu()
        
            opcionMenu = input("Inserta un número: >> ")
        
            if opcionMenu=="1":
                print ("")
                la.clean()
                f = open("primero.txt", "r")
                print(f.read())
                print("****************************************")
                input("Has pulsado la opción 1...\npulsa una tecla para continuar")
                la.clean()
            

            elif opcionMenu=="2":
                print ("")
                input("Has pulsado la opción 2...\npulsa una tecla para continuar")
                l1.agregar()
                l1.imprimir()
                la.clean()

            elif opcionMenu=="3":
                f = open("primero.txt", "r")
                f.close()
                break
            elif opcionMenu=="4":
                f = open("primero.txt", "r")
                l1.buscar()
                f.close()
            elif opcionMenu=="5":
                f = open("primero.txt", "r")
                l1.eli2()
                f.close()
            elif opcionMenu=="6":
                f = open("primero.txt", "r")
                f.close()
                break
            else:
                print ("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
lmenu = Menu()
lmenu.todo()
