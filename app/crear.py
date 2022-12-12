import errno
import os

from app.rutas import carpeta_archivos

carpetas = []

def crear():
    """
    Iteramos sobre los archivos en la carpeta y luego creamos una nueva carpeta para cada extensión de archivo.
    """

    

    # Por medio de un ciclo for, iteramos sobre nuestra carpeta de archivos.
    for fichero in carpeta_archivos.iterdir():
        # Indicamos que agregue la extensión de los archivos a la lista(carpetas)
        carpetas.append(fichero.suffix[1:])

    # Recorremos los elementos de la lista (carpetas),
    # condicionando que si no se encuentra, cree una nueva carpeta,
    # o manejamos el error 'OSError' con errno.
    for c in carpetas:
        
        try:
            if not os.path.exists(f"{carpeta_archivos}/{c}s"):
                os.mkdir(f"{carpeta_archivos}/{c}s")
                
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    print("Se han creado las nuevas carpetas en base a su extensión: \n")

    # Iterando sobre la carpeta principal (carpeta_archivos) e imprimiendo los directorios.
    for fichero in carpeta_archivos.iterdir():
        if fichero.is_dir():
            print("·", fichero.name)