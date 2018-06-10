import random
import time

''' 

	"Adivina el Número".

	1) La computadora pensará un número aleatorio entre el 1 y el 20.
	2) Tendrás que intentar adivinar el número.
	3) La computadora te dirá si cada intento es muy alto o muy bajo.
	4) Ganas si adivinas el número en 6 intentos o menos.

'''

def main():

	print("Bienvenido")
	print("¿Cómo te llamas?")

	usuario = input(">>> ")

	numero = random.randint(1,20)

	time.sleep(1)

	print("Ok " + usuario + ", estoy pensando un número entre el 1 y el 20.")

	intentosRealizados = 0


	while intentosRealizados < 6:

		print("Intenta adivinar el número")

		numeroEstimado = input(">>> ")
		numeroEstimado = int(numeroEstimado)

		intentosRealizados = intentosRealizados + 1

		if numeroEstimado < numero:
			print("Tu número es muy bajo.")
		if numeroEstimado > numero:
			print("Tu número es muy alto.")

		if numeroEstimado == numero:
			break

	if numeroEstimado == numero:

		intentosRealizados = str(intentosRealizados)

		print ("Felicidades " + usuario + ". Has adivinado mi número en " + intentosRealizados + " intentos! ")

	if numeroEstimado != numero:

		numero = str(numero)

		print(" Suerte para la proxima. El número que estaba pensado era " + numero)



main()