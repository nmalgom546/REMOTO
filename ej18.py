"""Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera."""


def main():

    nombre_completo = input("Introduce tu nombre completo: ")

    print (f"Tu nombre completo con todas las letras en minusculas: {nombre_completo.lower()}")
    print (f"Tu nombre completo con todas las letras en mayusculas: {nombre_completo.upper()}")
    print (f"Tu nombre completo con solo la primera letra de cada parte del nombre en mayusculas: {nombre_completo.title()}")









if __name__ == "__main__":
    main() 