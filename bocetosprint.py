#creamos la clase con los atributos que queremos
class libros:
	titulo= ''
	autor= ''

	def consulta(self,titulo,autor):
		print(self.titulo)
		print(self.autor)


f = open("prueba.txt", "r")
print(f.read())
print("****************************************")

l1= libros()
n=int(input("Cuantos Libros Deseas Agregar"))
for i in range(n):# el ciclo for ejecuta el rango de veces de n, permite agregar mas de un libro

	l1.titulo=input("Introduce el título: ")
	l1.autor=input("Introduce el autor: ")
	f = open("prueba.txt", "a")
	f.write(l1.titulo+" - ")
	f.write(l1.autor)
	f.write("\n")
	f.close()

f = open("prueba.txt", "r")
print(f.read())
f.close()