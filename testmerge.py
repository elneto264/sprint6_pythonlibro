class Libro: 
    titulo = ''
    autor = ''
    def __init__(self):
        self.libreria = []
    def agregar(self, titulo, autor):
        n = int(input("Cuantos libros deseas agregar: "))
        for i in range(n):
            self.titulo = input("Introduce el título: ")
            self.autor = input("Introduce el autor: ")
            estanteria = [self.titulo,self.autor]
            self.libreria.append(estanteria)
            f = open("text.txt", "a")
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
        se = open("text.txt", "r")
        word =  input("¿Qué libro deseas? ")
        print(se.index(word))