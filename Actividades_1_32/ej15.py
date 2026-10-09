"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales."""


def main():

    cantidad = float(input("Introduce tu deposito: "))
    interes = 0.04
    cantidad_1 = cantidad * (1 + interes)
    cantidad_2 = cantidad_1 * (1 + interes)
    cantidad_3 = cantidad_2 * (1 + interes)
    
    print (f"La cantidad ahorrada en el primer ano es de: {cantidad_1:.2f}, el del segundo ano es de {cantidad_2:.2f} y el del tercer ano es {cantidad_3:.2f} ")



if __name__ == "__main__":
    main() 