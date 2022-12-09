from app.rutas import carpeta_archivos

def listar():

    """
    La función 'listar()' lista los archivos en la carpeta 'carpeta_archivos' y los imprime.
    """

    print("Los archivos en la carpeta son: \n")
    for fichero in carpeta_archivos.iterdir():
        if fichero.is_file():
            print(fichero.name)
    print('\n')