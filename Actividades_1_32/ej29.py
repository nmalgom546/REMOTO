"""Cálculo de un número aleatorio entre dos valores"""


def main():

    import random
    
    numero_1 = int(input("Introduce el primer valor: "))
    numero_2 = int(input("Introduce el segundo valor: "))

    numero_ale = random.randint(numero_1, numero_2)


    print(f"El numero aleatorio es: {numero_ale}")

if __name__ == "__main__":
    main() 