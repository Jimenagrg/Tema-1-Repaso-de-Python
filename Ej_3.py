def clasificar_numeros(lista):
    pares = []
    impares = []
    negativos = []

    for num in lista:
        if num < 0:
            negativos.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    return pares, impares, negativos


if __name__ == "__main__":
    numeros = [10, -3, 7, -8, 0, 15, -2]
    pares, impares, negativos = clasificar_numeros(numeros)

    print("Pares:", pares)
    print("Impares:", impares)
    print("Negativos:", negativos)
