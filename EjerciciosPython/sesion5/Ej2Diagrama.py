# Ejercicio 2 : Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el pago por hora.

horasTrabajadas = int(input("Horas trabajadas: "))
CostoHora = int(input("Costo Hora: "))

sueldo = horasTrabajadas * CostoHora

print(f"El sueldo mensual es horas {horasTrabajadas} * costo de hora {CostoHora} = ${sueldo} ")