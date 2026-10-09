"""Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter."""


def main():

    fecha = input("Introduce tu fecha de nacimiento en el formato dd/mm/aaaa: ")

    separar = fecha.split("/")

    dia = separar [0]
    mes = separar [1]
    ano = separar [2]

    print (f"El dia de tu nacimiento es {dia}, el mes es {mes}, y el ano {ano}")

if __name__ == "__main__":
    main() 