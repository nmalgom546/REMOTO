""" Suponiendo que se han ejecutado las siguientes sentencias de asignación:"""

def main():
    horas = int(input("Escribe el numero de horas de trabajo: "))
    coste = float(input("Introduce el precio por hora: "))
    importotal = horas * coste

    print(f"El importe total del servicio es: {importotal}") 
           
if __name__ == "__main__":
    main() 