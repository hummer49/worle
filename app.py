# app.py

def verificar_palabra(
    palabra_objetivo:str, 
    palabra_ingresada:str
) -> list|None:
    """
    Docstring for verificar_palabra
    
    :param palabra_objetivo: Description
    :type palabra_objetivo: str
    :param palabra_ingresada: Description
    :type palabra_ingresada: str
    :return: Description
    :rtype: str
    """
    # Verficamos que ambas cadenas tengan la misma longitud
    if len(palabra_objetivo) != len(palabra_ingresada):
        print(f"La palabra ingresada <{palabra_ingresada}> no tiene la longitud adecuada")
        return None # cambiar a raise Error o algo asi
    # creamos la lista para almacenar las cadenas
    palabra_verificada = []
    # recorremos la palabra ingresada
    for ii in range(len(palabra_ingresada)):
        if palabra_ingresada[ii] == palabra_objetivo[ii]:
            palabra_verificada.append(f"[{palabra_ingresada[ii]}]")
        elif palabra_ingresada[ii] in palabra_objetivo:
            palabra_verificada.appen(f"({palabra_verificada[ii]})")
        else:
            palabra_verificada.append(f"{palabra_ingresada[ii]}")
    return palabra_verificada

def imprimir_grilla(
    grilla: list
) -> None:
    """
    Docstring for imprimir_grilla
    
    :param grilla: Description
    :type grilla: list
    """
    for fila in grilla:
        for columna in fila:
            print(columna, end=" ")
        print("\n")

def juego():
    # Setup
    secreto = "perros" # a futuro elegir la palabra 'secreto' de un banco de palabras
    turnos = 5 # cantidad de turnos del jugador
    victoria = False # bandera que determina si el jugador gano o no
    lista_intentos = [] # lista para almacenar las listas de las palabras verificadas

    while victoria == False and turnos > 0:
        # Mostrar la cantidad de turnos restantes
        print(f"Quedan:\t{turnos} turnos" if turnos > 1 else f"Queda:\t{turnos} turno" )
        # pedir la palabra al usuario
        palabra_ingresada = input("Ingrese una palabra")
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
        print("Perdiste")


def main():
    juego()


if __name__ == "__main__":
    main()