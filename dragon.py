import time
import random

def mostrarIntroduccion():
	print('Estás en una tierra llena de dragones. Frente a tí ')
	print('hay dos cuevas. En una de ellas, el dragón es generoso y amigable ')
	print('y compartirá su tesoro contigo. El otro dragón ')
	print('es codicioso y está hambriento, y te devorará inmediatamente. ')
	

def seleccionarCueva():
	cueva = 0
	while cueva != 1 and cueva != 2:
		print('¿A qué cueva quieres entrar? (1 ó 2)')
		cueva = input()
		cueva = int(cueva)
	return cueva

def explorarCueva(cuevaSeleccionada):
	print('Te aproximas a la cueva...')
	print('Es oscura y espeluznante...')
	print('¡Un gran dragon aparece súbitamente frente a tí! Abre sus fauces ...')
	print('')

	dragon_amigable = random.randint(1,2)

	if cuevaSeleccionada == dragon_amigable:
		print('¡Te regala su tesoro!')
	else:
		print('¡Te engulle de un bocado!')

def main():

	volverAJugar = "s"
	while volverAJugar == "s":
		mostrarIntroduccion()
		cuevaSeleccionada = seleccionarCueva()
		explorarCueva(cuevaSeleccionada)
		print('¿Quieres jugar de nuevo? (sí o no)')
		volverAJugar = input()

main()
