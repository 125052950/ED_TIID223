matriz = [
    [73, 12, 89, 34],
    [5, 61, 27, 94],
    [46, 18, 80, 3],
]

for i in matriz:
    if 61 in i:
        print(f"El número 61 esta en la fila {i}.")
        break

for fila in matriz:
    for numero in fila:
        if numero == 80:
            print(f"El 80 está en {fila}.")