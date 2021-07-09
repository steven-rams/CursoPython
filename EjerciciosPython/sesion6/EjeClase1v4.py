# Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)
# Henry Alberto Calderon Ferez

numero = int(input("Ingrese un numero: "))
if numero > 0 :
    print(f"El numero {numero} es POSITIVO")
else:
    if numero < 0 :
        print(f"El numero {numero} es NEGATIVO")
    else:
        print(f"El numero {numero} es NULO")