"""Calcular la serie de Fibonacci hasta un número dado."""



def main():


    numero = int(input("Introduce el numero hasta el que vamos a llegar: "))

    numero_1 = 0
    numero_2 = 1

    while numero_1 <= numero:
        print(numero_1)
        paso = numero_1 + numero_2
        numero_1 = numero_2
        numero_2 = paso

if __name__ == "__main__":
    main() 