# import random

# """Escribir un programa en Python que implemente el juego Ahorcado."""

# # Lista de palabras para el juego
# palabras = ["diego", "juan pablo", "mario", "santiago", "oscar", "sergio", "edwin", "alejandro"]
# palabra = random.choice(palabras)  # Seleccionar palabra al azar
# palabra_oculta = ["_"] * len(palabra)  # Palabra oculta con guiones
# intentos = 6  # Intentos máximos

# # Mensaje de bienvenida
# print(" ".join(palabra_oculta)) # convertir de lista a string con espacios y mostrar en pantalla

# #while intentos > 0:

#     # Mensaje pidiendo una letra

#     # verificar si la letra ingresada está en la palabra

#     # por cada vez que se encuentre la letra, reemplazar el guión por la letra adivinada

#     # si la letra no estaba, disminuir el número de intentos

#     # verificar si perdió o si ganó
import random

"""Escribir un programa en Python que implemente el juego Ahorcado."""
def obtener_palabra():
    palabras = ["diego", "juan pablo", "mario", "santiago", "oscar", "sergio", "edwin", "alejandro"]
    palabra=random.choice(palabras)
    return palabra

def mostrar_tablero(palabra_secreta,letras_adivinadas):
    palabra_oculta=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_oculta+=letra
        else:
            palabra_oculta+="_"
    print(palabra_oculta)
def jugar_ahorcado():
    palabra_secreta=obtener_palabra()
    letras_adivinadas=[]
    intentos_restantes=6
    
    while intentos_restantes>0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra=input("Introduce una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya  has introducido  esa letra. Prueba otra.")
            continue
        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas)==set(palabra_secreta):
                print("Felicidades, has acertado la palabra")
                break 
        else: 
            intentos_restantes-=1
            print(f"Letra incorrecta. Te quedan {intentos_restantes}")
    if intentos_restantes==0:
        print(f"Has perdido la palabra secreta era: {palabra_secreta}")
jugar_ahorcado()
                