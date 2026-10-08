"""Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)."""


def main():
    imporfinal = float(input("Escribe el importe final: "))
    iva = 10
    print (f"El IVA que se ha aplicado es de {iva}%")
    print (f"El importe del artículo sin IVA es {imporfinal - (iva * imporfinal / 100)} € ")


if __name__ == "__main__":
    main() 