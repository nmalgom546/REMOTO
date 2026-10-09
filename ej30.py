"""Escribir un programa que determine si un número es primo, incluyendo 0, 1 y los números negativos."""


def main():

    numero = int(input("Introduce un numero: "))   

    if numero < 2:
        print("El numero introducido no es primo.")
    else:
        primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False

    if primo:
        print("El numero es primo")
    else:
        print("El numero no es primo")


if __name__ == "__main__":
    main() 