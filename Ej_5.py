import random

def generar_adn(n):
    bases = ['A', 'T', 'C', 'G']
    cadena = ''.join(random.choices(bases, k=n))
    conteo = {}
    for base in bases:
        conteo[base] = cadena.count(base)
    return cadena, conteo

# Ejemplo
if __name__ == "__main__":
    longitud = 50  
    adn, conteo = generar_adn(longitud)
    print(f"Cadena de ADN: {adn}")
    print("Conteo de bases:")
    for base, cantidad in conteo.items():
        print(f"{base}: {cantidad}")