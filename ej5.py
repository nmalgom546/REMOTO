"""Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo."""

def main():
    precionoiva = float(input ("Escribe el importe (sin IVA): "))
    iva = float(input("Escribe el tipo de IVA a aplicar: "))
    print (f"El precio final del artículo es {precionoiva * (1 +(iva / 100))}")


if __name__ == "__main__":
    main() 