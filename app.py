# app.py

def verificar_palabra(
    palabra_objetivo:str, 
    palabra_ingresada:str
) -> list:
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
        return
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
    pass








def juego():
    verificar_palabra('a',"b")




















def main():
    pass


if __name__ == "__main__":
    main()