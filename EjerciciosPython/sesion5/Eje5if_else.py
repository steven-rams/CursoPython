#Estructura condicional compuesta  (SI - SINO).
#Ejercicio 7: Realizar un programa que solicite ingresar dos números distintos y muestre por pantalla el mayor de ellos.


num1 = int(input("Lea un numero: "))
num2 = int(input("Lea otro numero: "))

if (num1>num2):
    print(f"Numero {num1} es mayo que {num2}")
else:
    print(f"Numero {num2} es mayo que {num1}")

