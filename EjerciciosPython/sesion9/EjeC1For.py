"""•	Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
"""

CantNeg = 0
CantPos = 0
CantM15 = 0
acumpares = 0

for x in range(10):  
    valor = int(input(f"Ingrese el {x+1} valor "))
    if (valor < 0):
        CantNeg += 1
    else:
        CantPos += 1
    
    if (valor % 15) == 0: 
        CantM15 += 1
    
    if (valor % 2) == 0: 
        acumpares = acumpares + valor

print("Cantidad de valores negativos: ", CantNeg)
print("Cantidad de valores positivos: ", CantPos)
print("Cantidad de valores multiplos de 15: ", CantM15)
print("Acumulado de valores pares: ", acumpares)


