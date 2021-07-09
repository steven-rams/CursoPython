# Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)
# Julian Dario Franco Parra
num = int(input("ingrese un numero: "))

if num > 0:
    print("El numero", num, "Es positivo")
elif num < 0:
    print("El numero", num, "Es negativo")
else:
    print("El numero", num, "Es Cero")
print("***Elaborado por JF***")