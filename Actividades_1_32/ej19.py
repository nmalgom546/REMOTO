"""Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre."""


def main():

    nombre_completo = input("Introduce tu nombre: ")

    print (f"{nombre_completo} tiene {len(nombre_completo)} ")


if __name__ == "__main__":
    main() 