def analizar_url(url):
    try:
        # Eliminar espacios
        url = url.strip()
        # Buscar protocolo
        if "://" not in url:
            raise ValueError("URL inválida: falta el protocolo")
        protocolo, resto = url.split("://", 1)
        # Buscar dominio y recurso
        partes = resto.split("/", 1)
        dominio = partes[0]
        recurso = partes[1] if len(partes) > 1 and partes[1] else None
        return protocolo, dominio, recurso
    except Exception as e:
        print(f"Error al analizar la URL: {e}")
        return None, None, None

# Ejemplo de uso
if __name__ == "__main__":
    url = input("Introduce una URL: ")
    protocolo, dominio, recurso = analizar_url(url)
    print(f"Protocolo: {protocolo}")
    print(f"Dominio: {dominio}")
    print(f"Recurso: {recurso if recurso else 'No hay recurso'}")