"""Calcular el área de un triángulo a partir de tres lados. Indica qué ocurre si las longitudes no pueden formar un triángulo."""


def main():

    lado_1 = float(input("Introduce el tamano del primer lado: "))
    lado_2 = float(input("Introduce el tamano del segundo lado: "))
    lado_3 = float(input("Introduce el tamano del tercer lado: "))

    if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    
        semi_peri = (lado_1 + lado_2 + lado_3) / 2
        area = (semi_peri * (semi_peri - lado_1) * (semi_peri - lado_2) * (semi_peri - lado_3)) ** 0.5
        
        print (f"El area del triangulo es: {area}")

    else:
        print("Las medidas no pueden formar un triangulo.")
if __name__ == "__main__":
    main() 