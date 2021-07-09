# Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)
# Steven David Ramos

numero = int(input('Ingresa un numero: '))

if numero == 0:
    print('Neutro')
elif numero < 0:
    print("Negativo")
else:
    print("Positivo")  