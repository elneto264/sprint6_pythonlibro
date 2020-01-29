#!/usr/bin/python
# -*- coding: utf-8 -*-
class Libro:
	titulo= ''
	autor= ''


	def agregar(self,titulo,autor):

		n=int(input("Cuantos Libros Deseas Agregar"))#se pregunta cuantos elementos agregar
		for i in range(n):# el ciclo for ejecuta el rango de veces de n, permite agregar mas de un libro
		#Con el siguiente bloque de codigo escribimos usando las variables anteriores al txt
			self.titulo=input("Introduce el título: ")
			self.autor=input("Introduce el autor: ")
			f = open("text.txt", "a")
			f.write(l1.titulo+" - ")#esta línea escribe el título
			f.write(l1.autor)#esta línea escribe el autor 
			f.write("\n")#el \n crea un salto de línea para la siguiente entrada
			f.close()
	def buscarTitulo(self,titulo,autor): #funccion para busqueda de Titulo, pasamos el parametro de la lista
		print ("Busca Titulo")
		#f = open("text.txt", "r")
    #recorre la lista
		busqueda = input("Ingrese Titulo : ") #ingresamos el titulo a buscar agregar atributos(titulo y autor)
		with open("text.txt") as a:
			if busqueda in a.read():
				print(busqueda)
			else:
				print("no existe")


#abre y lee el fichero después de haber grabado el último libro

l1= Libro()

#con el siguiente bloque de codigo alojamos en las variables lo que el usuario escribe 




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
	print ("\t4 - Buscar")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
		f = open("text.txt", "r")
		print(f.read())#esta linea lee el fichero
		print("****************************************")
		#l1.buscarTitulo(l1.titulo,l1.autor)

	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
		l1.agregar(l1.titulo,l1.autor)

	elif opcionMenu=="3":
		f.close()#cierra el fichero 
		break
	elif opcionMenu=="4":
		l1.buscarTitulo(l1.titulo,l1.autor)
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
