# app.py
from random import choice

BANCO_PALABRAS = [
"perro", "gatos", "libro", "silla", "playa",
"noche", "verde", "rojos", "campo", "fuego",
"tarde", "dulce", "salud", "reloj", "fruta",
"amigo", "trigo", "botas", "coche", "minas"
]

def safe_input_n_char(
        n:int, 
        mensaje_input: str|None = "Introduzca su palabra:",
        mensaje_error: str|None = "La longitud no coincide, vuelva a intentarlo"
    )->str:
    # Retorna una cadena de caracteres de longitud n
    # Validamos que n sea un entero
    if not isinstance(n, int):
        raise TypeError(f"Se espera que n sea un numero entero, se recibio un <{type(n)}>")
    # Pedmos la palabra, hasta introducir n caracteres
    while True:
        s = input(f"{mensaje_input}\t").strip()
        if len(s) == n:
            break
        print(mensaje_error)
    if s:
        return s

def elegir_secreto(bank)->str:
    return choice(bank)

def verificar_palabra(
    palabra_objetivo:str, 
    palabra_ingresada:str
) -> list:
    # Verficamos que ambas cadenas tengan la misma longitud
    if len(palabra_objetivo) != len(palabra_ingresada):
        raise Exception("Las longitudes de las palabras no coinciden")
    # creamos la lista para almacenar las cadenas
    palabra_verificada = []
    # recorremos la palabra ingresada
    for ii in range(len(palabra_ingresada)):
        if palabra_ingresada[ii] == palabra_objetivo[ii]:
            palabra_verificada.append(f"[{palabra_ingresada[ii]}]")
        elif palabra_ingresada[ii] in palabra_objetivo:
            palabra_verificada.append(f"({palabra_ingresada[ii]})")
        else:
            palabra_verificada.append(f"{palabra_ingresada[ii]}")
    return palabra_verificada

def imprimir_grilla(
    grilla: list
) -> None:
    for fila in grilla:
        for columna in fila:
            print(columna, end=" ")
        print("\n")

def juego():
    # Setup
    secreto = elegir_secreto(BANCO_PALABRAS)
    longitud = 5 
    turnos = 5 # cantidad de turnos del jugador
    victoria = False # bandera que determina si el jugador gano o no
    lista_intentos = [] # lista para almacenar las listas de las palabras verificadas

    while victoria == False and turnos > 0:
        # Mostrar la cantidad de turnos restantes
        print(f"Quedan:\t{turnos} turnos" if turnos > 1 else f"Queda:\t{turnos} turno" )
        # pedir la palabra al usuario
        palabra_ingresada = safe_input_n_char(longitud, "Ingrese una palabra: ")
        # verificamos palabra_ingresada, y la agregamos a lista_intentos
        lista_intentos.append(verificar_palabra(secreto, palabra_ingresada))
        # Mostramo la lista de intentos
        imprimir_grilla(lista_intentos)
        # Verificamos si el jugador gano
        if secreto == palabra_ingresada:
            victoria = True
            break
        # reducir cantidad de turnos
        turnos -= 1

    if victoria == True:
        print("Ganaste!!")
    else:
        print(f"Perdiste. La palabra era {secreto}")


def main():
    juego()


if __name__ == "__main__":
    main()