"""Mostrar todos los divisores de un número"""



def main():

    numero = int(input("Introduce un numero entero: "))

    if numero == 0:
        print("El 0 tiene infinitos divisores.")
    else:
     for i in range(1, abs(numero) + 1):
        if numero % i == 0:
            print(i)



if __name__ == "__main__":
    main() 