"""Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula."""


def main():

    frase = input("Introduce una frase: ")
    vocal = input ("Introduce una vocal: ")
    resultado = ""

    for letra in frase:
        if letra == vocal:
            resultado = resultado + vocal.upper()
        else:
            resultado = resultado + letra



  
    print (f"La frase introducida con la vocal en mayuscula: {resultado}") 



if __name__ == "__main__":
    main() 