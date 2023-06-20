"""Desarrollo de algoritmo para manejo de archivos:"""

# Importamos los módulos.
from app.validar import validar_numeros

from app.crear import crear
from app.mover import mover
from app.listar import listar


# Definimos la función, en donde centramos todo nuestro programa.
def archivos():
    """
    La función "archivos()" pide al usuario que seleccione
    una opción de un menú y luego realiza la acción
    correspondiente
    """

    # En una variable indicamos que el valor inicial es de tipo Bool (True)
    preguntar = True

    """
    Con un ciclo while, repetiremos la misma acción mientras
    el valor ingresado por el usuario se encuentre
    en nuestro menú de opciones, o indique que desea
    terminar el programa ingresando el valor de '5'.
    """
    while preguntar:
        # Imprimimos nuestro menú de opciones.
        print("Seleccione del Menú lo que desea hacer: \n")
        print("1) Listar Archivos \n")
        print("2) Crear Carpetas para los Archivos \n")
        print("3) Mover Archivos a Carpetas \n")
        print("4) Salir \n")

        # En una variable recibimos los valores u
        # opciones que el usuario requiere.
        opcion = validar_numeros("una opción: \r\n")

        # Nuestra primer opción, y si el usuario ingresa el valor de '1',
        # será la de listar todos los archivos que se encuentran en
        # nuestra carpeta principal (carpeta_archivos).
        if opcion == 1:
            listar()

        # Nuestra segunda opción, crea las carpetas
        # para los archivos en base a su extensión.
        elif opcion == 2:
            crear()

        # Nuestra tercera opción, mueve los archivos hacia su nueva carpeta,
        # creada en el paso 2.
        elif opcion == 3:
            mover()

        # Nuestra cuarta y última opción, termina el programa.
        elif opcion == 4:
            print("Programa terminado, ha sido un gusto servirte... \n")
            # Por medio de 'break' rompemos la iteración del ciclo while,
            # terminando así nuestro programa.
            break


# Mandamos llamar a nuestra función.
archivos()
