class Libro: 
    titulo = ''
    autor = ''
    def __init__(self):
        self.libreria =''
    def agregar(self, titulo, autor):
        n = int(input("Cuantos libros deseas agregar: "))
        for i in range(n):
            self.titulo = input("Introduce el título: ")
            self.autor = input("Introduce el autor: ")
            f = open("primero.txt", "a")
            f.write(self.titulo + " - ")
            f.write(self.autor)
            f.write("\n")
            f.close()
    def imprimir(self):
        for k in range(len(self.libreria)):
            for j in range(len(self.libreria[k])):
                print(self.libreria[k][j]," ",end="")
            print()
    def buscar(self):
        f = open ("primero.txt", "r")
        word = input("Que Libro deseas? ")
        s = " "
        count = 1
        existe = False
        while (s):
            s = f.readline()
            L = s.split()
            if word in L:
                print("Se Encuentra en ", count, ":", s)
                count += 1
                existe = True  
            """else:
                print("No Existe")"""
        if existe == False:
            print ("No existe")
        f.close()
        