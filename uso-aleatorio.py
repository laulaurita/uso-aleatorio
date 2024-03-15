import random

def lanzamiento_de_dados():
    print("Bienvenido al juego de lanzamiento de dados.")
    input("Presiona Enter para lanzar los dados...")

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    print(f"El dado 1 muestra: {dado1}")
    print(f"El dado 2 muestra: {dado2}")

    total = dado1 + dado2
    print(f"Total: {total}")

    if dado1 == dado2:
        print("¡Dobles! ¡Lanzamiento extra!")

        dado_extra = random.randint(1, 6)
        print(f"Lanzamiento extra: {dado_extra}")

        total += dado_extra
        print(f"Total final: {total}")

    if total % 2 == 0:
        print("El total es par.")
    else:
        print("El total es impar.")

if __name__ == "__main__":
    lanzamiento_de_dados()