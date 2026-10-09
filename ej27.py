"""Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales."""


def main():

    producto = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    unidades = int(input("Introduce el numero de unidades: "))
    total = precio * unidades

    print(f"El precio unitario de {producto} es: {precio:09.2f} euros.")
    print(f"las unidades de {producto} son {unidades:03d}.")
    print(f"El precio total es: {total:011.2f} euros.")



if __name__ == "__main__":
    main() 