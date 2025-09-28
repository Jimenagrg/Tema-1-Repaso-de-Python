
def calcular_notas(notas):
    if not notas:
        print("La lista de notas está vacía.")
        return

    media = sum(notas) / len(notas)
    nota_max = max(notas)
    nota_min = min(notas)

    print(f"Media: {media:.2f}")
    print(f"Nota más alta: {nota_max}")
    print(f"Nota más baja: {nota_min}")

    if any(nota < 5 for nota in notas):
        print(" Hay alguna nota suspensa (<5).")

if __name__ == "__main__":
    notas = [7.5, 4.0, 9.0, 6.5, 3.5]
    calcular_notas(notas)

    