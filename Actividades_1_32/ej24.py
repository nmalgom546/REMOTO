"""Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido."""


def main():

    precio = (input("Introduce el precio del producto: "))
    
    partes = precio.split(".")


    euros = partes[0]
    centimos = partes[1][:2]

    print (f"Euros: {euros}")
    print (f"Centimos: {centimos}")


if __name__ == "__main__":
    main() 