class Libro: 
    titulo = ''
    autor = ''
    def agregar(self, titulo, autor):
        n = int(input("Cuantos libros deseas agregar: "))
        for i in range(n):
            self.titulo = input("Introduce el título: ")
            self.autor = input("Introduce el autor: ")
            f = open("text.txt", "a")
            f.write(self.titulo + " - ")
            f.write(self.autor)
            f.write("\n")
            f.close()