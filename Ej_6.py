def clasificar_personajes(personajes):
    humanos = []
    criaturas = []
    for nombre, tipo in personajes.items():
        if tipo == "humano":
            humanos.append(nombre)
        elif tipo == "criatura":
            criaturas.append(nombre)

    humanos_ordenados = sorted(humanos)
    criaturas_ordenadas = sorted(criaturas, key=len)

    return humanos_ordenados, criaturas_ordenadas

# Ejemplo de uso:
if __name__ == "__main__":
    inventario = {
        "Ana": "humano",
        "Luis": "humano",
        "Marta": "humano",
        "Draco": "criatura",
        "Basilisco": "criatura",
        "Pedro": "humano",
        "Grifo": "criatura"
    }

    humanos, criaturas = clasificar_personajes(inventario)
    print("Humanos ordenados de forma alfabética:", humanos)
    print("Criaturas ordenadas por longitud de nombre:", criaturas)