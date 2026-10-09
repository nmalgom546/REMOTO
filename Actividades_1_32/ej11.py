"""Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:"""


def main():

    numeropositivo = int(input("Introduce un número positivo: "))
    suma = 0

    if numeropositivo < 0:
        int(input("El numero debe de ser positivo"))
    else:
        suma = numeropositivo * (numeropositivo + 1)/2
        print (f"El resultado de todos los numeros es: {suma}" )

if __name__ == "__main__":
    main() 