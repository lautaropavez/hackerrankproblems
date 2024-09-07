if __name__ == '__main__':
    n = int(input())
    cadena = ""
    for i in range(n):
        cadena += str(i+1)
        if i == (n-1):
            print(cadena)

# Otra forma mejor
# if __name__ == '__main__':
#    n = int(input())
#    cadena = ''.join(str(i) for i in range(1, n+1))
#    print(cadena)

# -------------------
# Ejemplo de como funciona
# palabras = ["aprender", "es", "divertido"]
# resultado_1 = " ".join(palabras)    # Separador: espacio
# resultado_2 = "-".join(palabras)    # Separador: guion
# resultado_3 = "".join(palabras)     # Sin separador

# print(resultado_1)  # aprender es divertido
# print(resultado_2)  # aprender-es-divertido
# print(resultado_3)  # aprenderesdivertido

