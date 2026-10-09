"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es."""


def main():

    correo = input("Introduce tu correo electronico: ")
    correo_edi = correo.split("@")[0]
    correo_ceu = correo_edi + "@ceu.es"


    print (f"El nuevo correo es: {correo_ceu}")


if __name__ == "__main__":
    main() 