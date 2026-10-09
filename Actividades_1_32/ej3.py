"""Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:"""

def main():

    ancho = int(input("Introduce el ancho: "))
    alto = float(input("Introduce el alto: "))

    print (f"Ancho = {ancho}")
    print (f"Alto = {alto}")


    print (f"1. {ancho/2}")
    print (f"2. {ancho//2}")
    print (f"3. {alto/3}")
    print (f"{1 + 2 * 5}")
    
if __name__ == "__main__":
    main() 