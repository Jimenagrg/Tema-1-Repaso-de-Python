ahorro = input("Introduce la cantidad incial, cantidad menusal, número de meses")
datos = ahorro.split(",")
cantidad_inicial = float(datos[0])
cantidad_mensual = float(datos[1])
número_meses = int(datos[2])

cantidad_ahorrada = cantidad_inicial + cantidad_mensual * número_meses 
print("Total ahorrado: {}".format(cantidad_ahorrada))

if cantidad_ahorrada > 5000:
    print("Felicidades has superado los 5000€")
else:
    print("No has conseguido el objetivo de ahorro :(")

