numeros = [0]
añadirnumero = 0

print("Introduce un número y se sumarán los que sean positivos, escribe 'Listo' para ver el resultado.")

while True:
    entrada = input("")
    if entrada.lower() == "listo":
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, introduce un número válido o 'Listo' para calcular.")

suma = 0

for n  in numeros:
    if n >= 0:
        suma = suma + n
print("El resultado es:", suma)