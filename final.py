import time
class Libro: 
    titulo = ''
    autor = ''
    def __init__(self):
        self.libreria =''
    def agregar(self):
        n = int(input("Cuantos libros deseas agregar: "))
        for i in range(n):#buscar
            self.titulo = input("Introduce el título: ")
            f = open ("primero.txt", "r")
            s = " "
            existe = False
            while (s):
                s = f.readline()
                L = s.split()
                if self.titulo in L:
                    existe = True
                    print("Existe")
            f.close()
            if existe == False:
                self.autor = input("Introduce el autor: ")
                f = open("primero.txt", "a")
                f.write(self.titulo + " - ")
                f.write(self.autor)
                f.write("\n")
                f.close() #fin buscar
    def imprimir(self):
        for k in range(len(self.libreria)):
            for j in range(len(self.libreria[k])):
                print(self.libreria[k][j]," ",end="")
            print()
    def buscar(self):
        f = open ("primero.txt", "r")
        word = input("   ¿Qué libro deseas consultar? ")
        s = " "
        count = 1
        existe = False
        while (s):
            s = f.readline()
            L = s.split()
            if word in L:
                print("    Se Encuentra en ", count, ":", s)
                count += 1
                existe = True
                time.sleep(1)
        if existe == False:
            print ("No existe")
            time.sleep(1)
        f.close()    
    def eli2(self):
        f = open("primero.txt","r")
        lineas = f.readlines()
        f.close()
        f = open("primero.txt","w")
        eli = input("¿Qué libro deseas eliminar? ")
        existe = False
        for linea in lineas:
            if linea!= eli+"\n":
                f.write(linea)
            else: #if linea == eli+"\n"
                existe = True
                print("Se eliminó")
        if existe == False:
            print("No existe")
        f.close()
         
