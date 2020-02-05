class Libro: 
    titulo = ''
    autor = ''
    def __init__(self):
        self.libreria =''
    def agregar(self):
        fichero = open("primero.txt","r")
        self.titulo = input("Introduce el título: ")
        self.autor = input("Introduce el autor: ")
        s = fichero.readline()
        L = s.split()
        if self.titulo in L:
            print("Libro Existe")
        else:
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
    def eli2(self):
        # abrimos el archivo solo de lectura
        f = open("primero.txt","r")
        # Creamos una lista con cada una de sus lineas
        lineas = f.readlines()
        # cerramos el archivo
        f.close()
        # abrimos el archivo pero vacio
        f = open("primero.txt","w")
        # recorremos todas las lineas
        eli = input("¿Qué libro deseas eliminar? ")
        for linea in lineas:
            # miramos si el contenido de la linea es diferente a la linea a eliminar
            # añadimos al final \n que es el salto de linea
            if linea!= eli+"\n":
            # Si no es la linea que queremos eliminar, guardamos la linea en el archivo
                f.write(linea)
                print("va")
        # cerramos el archivo
        f.close()
         
