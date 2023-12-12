def jugar_ahorcado():
    palabra_secreta = "python"  # Puedes cambiar la palabra según tu preferencia
    letras_adivinadas = []
    intentos_fallidos_maximos = 3

    print("¡Bienvenido al juego del ahorcado!")

    while intentos_fallidos_maximos > 0:
        palabra_mostrada = ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra_secreta)
        print(f"Palabra a adivinar: {palabra_mostrada}")

        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra.")
            break

        letra = input("Ingresa una letra: ").lower()

        if letra not in palabra_secreta:
            intentos_fallidos_maximos -= 1
            print(f"Incorrecto. Intentos fallidos restantes: {intentos_fallidos_maximos}" )
        
        letras_adivinadas.append(letra)

    if intentos_fallidos_maximos == 0:
        print(f"¡Oh no! Has agotado tus intentos fallidos. La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    jugar_ahorcado()
