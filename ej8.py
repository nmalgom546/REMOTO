"""Escribir el programa del ejercicio 1.2.7 usando solamente dos variables diferentes."""

def main():
    
    suma = 0

    num = float(input("Escribe el primer numero: "))
    suma = suma + num
    num = float(input("Escribe el segundo numero: "))
    suma = suma + num
    num3 = float(input("Escribe el tercer numero: "))
    suma = suma + num
    
    print  (f"El resultado de tu suma es: {suma}")




if __name__ == "__main__":
    main() 