def formatear_cadena(cadena_corrupta):
    invertido = cadena_corrupta[::-1]
    cadena_limpia = ""
    for c in invertido:
        if c.isalpha():
            cadena_limpia += c
    print(cadena_limpia)

if __name__ == "__main__":
    mensaje = "odnuMaloH!**"
    formatear_cadena(mensaje)






