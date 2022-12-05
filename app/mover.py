import shutil

from rutas import *

def mover():

    """
    Iteramos a través de nuestra carpeta de archivos, y si los archivos tienen la extensión '.txt','.jpg','.jpeg',
    '.png', '.pdf', '.mp3' ó '.mp4' los movemos a su respectiva carpeta de destino.
    """

    # Iteramos en nuestra carpeta de archivos.
    for fichero in carpeta_archivos.iterdir():

        if fichero.suffix == ".txt":
            shutil.move(str(carpeta_archivos/fichero), str(destination_txts))

        if fichero.suffix == ".jpg":
            shutil.move(str(carpeta_archivos/fichero), str(destination_jpgs))

        if fichero.suffix == ".jpeg":
            shutil.move(str(carpeta_archivos/fichero), str(destination_jpegs))

        if fichero.suffix == ".png":
            shutil.move(str(carpeta_archivos/fichero), str(destination_pngs))

        if fichero.suffix == ".pdf":
            shutil.move(str(carpeta_archivos/fichero), str(destination_pdfs))

        if fichero.suffix == ".mp3":
            shutil.move(str(carpeta_archivos/fichero), str(destination_mp3s))

        if fichero.suffix == ".mp4":
            shutil.move(str(carpeta_archivos/fichero), str(destination_mp4s))