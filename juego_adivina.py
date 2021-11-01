#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# -*- coding: utf-8 -*-
#1. Desarrolle la estructura de un juego donde se use al menos 2 tipos diferentes de estructuras algorítmicas y 2 estructuras de datos.

#Lista con productos alimenticios, simulación de un juego de adivinanza
intentos=2
print("Adivina que hay en tu cesta dec compras/ tienes 2 vidas")

def game(respuesta):
	lista=['manzanas','peras','Sandias','bananas','mangos','pepinos','Jocote']
	correcto = False
	for x in range(0,len(lista)):
		if lista[x]==respuesta:
			correcto = True
	return correcto

if game(input("Cual es tu respuesta: ")):
	print("Has acertado ala primera. Felicidades")
else:
	intentos= intentos-1
	if intentos>0:
		print("Aun tienes una vida??")
		if game(input("Cual es tu respuesta: ")):
			print("Has acertado ala segunda. Felicidades")
		else:
			print("Perdistes")	
