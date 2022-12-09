import shutil

from app.rutas import *

def mover():

    """
    Iteramos a través de nuestra carpeta de archivos, y dependiendo de su extensión,
    éstos los movemos a su respectiva carpeta de destino antes creada.
    """

    # Iteramos en nuestra carpeta de archivos.
    for fichero in carpeta_archivos.iterdir():

        if fichero.is_file():
            shutil.move(str(fichero), str(f"{carpeta_archivos}/{fichero.suffix[1:]}s"))