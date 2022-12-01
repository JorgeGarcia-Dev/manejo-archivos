"""Desarrollo de algoritmo para manejo de archivos:"""

# Importamos los módulos.
from app.rutas import *
from app.validar import validar_numeros

from app.crear import crear
from app.mover import mover
from app.listar import listar
from app.clasificar import clasificar

# Definimos la función, en donde centramos todo nuestro programa.
def archivos():
    """
    La función "archivos()" pide al usuario que seleccione una opción de un menú y luego realiza la
    acción correspondiente
    """

    # En una variable indicamos que el valor inicial es de tipo Bool (True)
    preguntar = True

    # Con un ciclo while, repetiremos la misma acción mientras el valor ingresado por el usuario se encuentre en nuestro menú de opciones,
    # o indique que desea terminar el programa ingresando el valor de '5'.
    while preguntar:

        # Imprimimos nuestro menú de opciones.
        print('Seleccione del Menú lo que desea hacer: \n')
        print('1) Listar Archivos \n')
        print('2) Ver Archivos Clasificados \n')
        print('3) Crear Carpetas para los Archivos \n')
        print('4) Mover Archivos a Carpetas \n')
        print('5) Salir \n')

        # En una variable recibimos los valores u opciones que el usuario requiere.
        opcion = validar_numeros("una opción: \r\n")

        # Nuestra primer opción, y si el usuario ingresa el valor de '1',
        # será la de listar todos los archivos que se encuentran en nuestra carpeta de Archivos.
        if opcion == 1:

            listar()

        # Nuestra segunda opción, lista los archivos, clasificándolos por medio de su extensión.
        elif opcion == 2:

            clasificar()

        # Nuestra tercera opción, crea las carpetas para los archivos en base a su extensión.
        elif opcion == 3:

            crear()

        # Nuestra cuarta opción, mueve los archivos desde la carpeta Archivos, a sus respectivas carpetas creadas por su tipo de extensión.
        elif opcion == 4:

            mover()

        # Nuestra quinta y última opción, termina el programa.
        elif opcion == 5:
            print("Programa terminado, ha sido un gusto servirte... \n")
            # Por medio de 'break' rompemos la iteración del ciclo while, terminando así nuestro programa.
            break

# Mandamos llamar a nuestra función.
archivos()