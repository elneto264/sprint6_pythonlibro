from final import Libro
from limpiar import Limpieza

class Menu:
    def menu(self):
        la = Limpieza()
        la.clean()
        print("\033[0;33;40m    *********************************************") 
        print("\033[0;33;40m    *                                           *")
        print("\033[0;33;40m    *  ¡Bienvenidos a la Biblioteca Open Mind!  *")
        print("\033[0;33;40m    *                                           *")
        print("\033[0;33;40m    *********************************************")
        print ("\033[0;31;40m\t1 - Consultar listado")
        print ("\033[0;33;40m\t2 - Agregar libro al listado ")
        print ("\033[0;32;40m\t3 - Consultar libro ")
        print ("\033[0;36;40m\t4 - Eliminar libro ")
        print ("\033[0;34;40m\t5 - Salir")
        print ("\033[0;35;40m   Selecciona una opción")
        l1 = Libro()
        
    def todo(self):
        l1 = Libro()
        la = Limpieza()
        while True:
            self.menu()
            opcionMenu = input("\033[0;37;40m   Inserta un número: >> ")
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
                l1.buscar()
                f.close()
            elif opcionMenu=="4":
                f = open("primero.txt", "r")
                l1.eli2()
                f.close()
            elif opcionMenu=="5":
                f = open("primero.txt", "r")
                f.close()
                break
            else:
                print ("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
lmenu = Menu()
lmenu.todo()
