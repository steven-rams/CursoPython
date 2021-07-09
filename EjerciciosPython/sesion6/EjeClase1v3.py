# Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)
# Ana Maria Martinez Macea

num = int(input("Ingrese un valor entero: "))
if (num > 0):
    print(f"El numero {num} es positivo")
elif (num < 0):
    print(f"El numero {num} es negativo")
else:
    print(f"El numero {num} es nulo")