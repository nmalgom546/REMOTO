"""Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida."""

def main():
    temp = float(input("Escribe la temperatura (celcius): "))
    print (f"La temperatura en fahrenheit es: {(temp * (9/5)) + 32} ºF")

if __name__ == "__main__":
    main()
    