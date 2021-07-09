#Estructuras condicionales anidadas (SI – SINO - SI)
#Ejercicio 8: Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos mensajes:
"""
nota1 = float(input("Digite la primera nota: "))
nota2 = float(input("Digite la segunda nota: "))
nota3 = float(input("Digite la tercera nota: "))

prom = (nota1+nota2+nota3)/3

if (prom >= 7):
    print(f"Promocionado su promedio fue: {round(prom,3)}")
elif (prom >= 4):
    print(f"Regular su promedio fue: {prom}")
else:
    print(f"Reprobado su promedio fue: {prom}")
"""
# Forma Tradicional 

nota1 = float(input("Digite la primera nota: "))
nota2 = float(input("Digite la segunda nota: "))
nota3 = float(input("Digite la tercera nota: "))

prom = (nota1+nota2+nota3)/3

if (prom >= 7):
    print(f"Promocionado su promedio fue: {round(prom,3)}")
else:
    if (prom >= 4):
        print(f"Regular su promedio fue: {prom}")
    else:
        print(f"Reprobado su promedio fue: {prom}")
