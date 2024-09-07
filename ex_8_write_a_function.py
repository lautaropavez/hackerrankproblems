"""
En el calendario gregoriano se utilizan tres condiciones para identificar los años bisiestos:

El año se puede dividir exactamente por 4, es un año bisiesto, a menos que:
El año se puede dividir exactamente por 100, NO es un año bisiesto, a menos que:
El año también es divisible exactamente por 400. En ese caso, es un año bisiesto.
Esto significa que en el calendario gregoriano, los años 2000 y 2400 son años bisiestos,
mientras que 1800, 1900, 2100, 2200, 2300 y 2500 NO son años bisiestos.
"""
def is_leap(year):

  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  if year % 4 == 0:
    return True
  else:
    return False

year = int(input())
print(is_leap(year))

"""
#Forma mas completa

year = int(input("Ingrese el año: "))

def es_bisiesto(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

if es_bisiesto(year):
    print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es bisiesto.")

#Practica

year = int(input("Ingrese el año: "))

if year == 0:
    print("Hola")
else:
    print("No")
"""

