"""Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta."""


def main():

    productos = input("Introduce los productos separados por comas: ")

    separar = productos.split(",")

    for productos in separar:
        print (productos)

if __name__ == "__main__":
    main() 