#creamos la clase con los atributos que queremos
class libros:
	titulo= ''
	autor= ''

	def consulta(self,titulo,autor): #aqui definimos lo que hara nuestro metodo
		print(self.titulo)
		print(self.autor)
#con el siguiente bloque de codigo alojamos en las variables lo que el usuario escribe 
f = open("text.txt", "r")
print(f.read())#esta linea lee el fichero
print("****************************************")

l1= libros()
n=int(input("Cuantos Libros Deseas Agregar"))#se pregunta cuantos elementos agregar
for i in range(n):# el ciclo for ejecuta el rango de veces de n, permite agregar mas de un libro
	#Con el siguiente bloque de codigo escribimos usando las variables anteriores al txt
	l1.titulo=input("Introduce el título: ")
	l1.autor=input("Introduce el autor: ")
	f = open("text.txt", "a")
	f.write(l1.titulo+" - ")#esta línea escribe el título
	f.write(l1.autor)#esta línea escribe el autor 
	f.write("\n")#el \n crea un salto de línea para la siguiente entrada
	f.close()
#abre y lee el fichero después de haber grabado el último libro
f = open("text.txt", "r")
print(f.read())
f.close()#cierra el fichero 