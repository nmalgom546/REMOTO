"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""


def main():

    usuario = input("Escribe tu nombre de usuario: ")
    numero = int(input("Introduce el numero de veces que quieras que se repita el usuario: "))

    while numero != 0:

        numero = numero - 1
        print (f"Tu nombre de usuario es: {usuario}")




if __name__ == "__main__":
    main() 