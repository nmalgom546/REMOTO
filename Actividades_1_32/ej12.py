"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales."""


def main():

    peso = float(input("Introduce el peso (kg): "))
    estatura = float(input("Introduce la estatura (metros): "))
    masa_corporal = peso / (estatura**2)

    print(f"Tu indice de masa corporal es: {masa_corporal:.2f}")

if __name__ == "__main__":
    main() 