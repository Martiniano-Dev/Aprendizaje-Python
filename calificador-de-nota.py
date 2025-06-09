nota = int(input("Nota: "))

if nota >= 9:
    print("Excelente")
elif nota == 7 or nota == 8:
    print("Buena")
elif nota == 5 or nota == 6:
    print("Regular")
else:
    print("Insuficiente")