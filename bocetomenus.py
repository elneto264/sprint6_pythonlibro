#!/usr/bin/python
# -*- coding: utf-8 -*-
class libros:
	titulo= ''
	autor= ''

	def consulta(self,titulo,autor): #aqui definimos lo que hara nuestro metodo
		print(self.titulo)
		print(self.autor)


	def agregar(self,titulo,autor):

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

l1= libros()

#con el siguiente bloque de codigo alojamos en las variables lo que el usuario escribe 
f = open("text.txt", "r")
print(f.read())#esta linea lee el fichero
print("****************************************")



import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Consultar listado")
	print ("\t2 - Agregar libro al listado")
	print ("\t3 - Salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")

	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
		l1.agregar(l1.titulo,l1.autor)

	elif opcionMenu=="3":
		f = open("text.txt", "r")
		print(f.read())
		f.close()#cierra el fichero 
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")