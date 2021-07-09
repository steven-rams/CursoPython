# Estructura condicional simple (SI).
# Ejercicio 6: Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos.

sueldo = int(input("Ingrese el sueldo: "))

if (sueldo > 3000):
    print(f"el sueldo de {sueldo} Debe abonar impuestos")