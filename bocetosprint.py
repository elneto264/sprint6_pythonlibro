#creamos la clase con los atributos que queremos
class libros:
	titulo= ''
	autor= ''

	def consulta(self,titulo,autor): #aqui definimos lo que hara nuestro metodo
		print(self.titulo)
		print(self.autor)
#con el siguiente bloque de codigo alojamos en las variables lo que el usuario escribe 
f = open("text.txt", "r")
print(f.read())
print("****************************************")

l1= libros()
l1.titulo=input("Introduce el título: ")
l1.autor=input("Introduce el autor: ")


#Con el siguiente bloque de codigo escribimos usando las variables anteriores al txt
f = open("text.txt", "a")
f.write(l1.titulo+" - ")#esta línea escribe el título
f.write(l1.autor+"\n")#esta línea escribe el autor, el \n crea un salto de línea para la siguiente entrada 
f.close()#cierra el fichero 
#abre y lee el fichero después de haber grabado el último libro
f = open("text.txt", "r")
print(f.read())
f.close()