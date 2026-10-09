"""Escribir un programa que pida al usuario dos números enteros y muestre por pantalla lo siguiente: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente. Trata también la división entre cero."""


def main():

    numero_n = int(input("Introduce un numero: "))
    numero_m = int(input("Introduce un numero: "))

    print (f"La division de {numero_n} entre {numero_m} da un cociente de {numero_n / numero_m} y un resto de {numero_n % numero_m}")


if __name__ == "__main__":
    main() 