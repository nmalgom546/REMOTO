"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión."""


def main():

    prefijo = input("Introduce el prefijo de tu pais: ")
    numero = int(input("Introduce el numero de telefono: "))
    extension = int(input("Introduce la extension de tu zona de trabajo: "))


    print (f"El numero es {numero}, y el numero que tiene en la empresa es +{prefijo}-{numero}-{extension}")






if __name__ == "__main__":
    main() 