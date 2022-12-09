import shutil

from app.rutas import *

def mover():

    """
    Iteramos a través de nuestra carpeta de archivos, y si los archivos tienen la extensión '.txt','.jpg','.jpeg',
    '.png', '.pdf', '.mp3' ó '.mp4' los movemos a su respectiva carpeta de destino.
    """

    # Iteramos en nuestra carpeta de archivos.
    for fichero in carpeta_archivos.iterdir():

        if fichero.is_file():
            shutil.move(str(fichero), str(f"{carpeta_archivos}/{fichero.suffix[1:]}s"))