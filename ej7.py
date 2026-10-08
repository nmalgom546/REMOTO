"""Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma."""


def main():
    num1 = float(input("Escribe el primer numero: "))
    num2 = float(input("Escribe el segundo numero: "))
    num3 = float(input("Escribe el tercer numero: "))

    suma = num1 + num2 + num3
    print  (f"El resultado de tu suma es: {suma}")

if __name__ == "__main__":
    main() 