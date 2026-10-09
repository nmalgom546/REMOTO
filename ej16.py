"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas."""


def main():

    pan = 3.49
    pan_pasado = pan - (pan * 0.60)
    num_barras = int(input("Introduce el numero de barras que no son del dia vendidas hoy: "))
    
    print (f"El numero de barras que no son de hoy vendidas son {num_barras}, las barras tienen un descuento del 60% por lo tanto se le descuenta {pan_pasado:.2f} euros al precio original de la barra que es {pan} euros, el coste total de las barras es {num_barras * (pan - pan_pasado):.2f} euros")

if __name__ == "__main__":
    main() 