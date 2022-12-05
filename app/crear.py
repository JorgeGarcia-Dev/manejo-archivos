import errno
import os

from rutas import current_path
from rutas import carpeta_archivos

def crear():

    """
    Si la extensión del archivo es .txt, cree una carpeta llamada txts. Si la extensión del archivo es .jpg, cree un
    carpeta llamada jpgs. Si la extensión del archivo es .jpeg, cree una carpeta llamada jpegs. Si el archivo
    extensión es .png, cree una carpeta llamada pngs. Si la extensión del archivo es .pdf, cree una carpeta
    llamados pdf. Si la extensión del archivo es .mp3, cree una carpeta llamada mp3s. Si la extensión del archivo es
    .mp4, crea una carpeta llamada mp4s
    """

    # Por medio de un ciclo for, iteramos sobre nuestra carpeta de archivos.
    for fichero in carpeta_archivos.iterdir():

        if fichero.suffix == ".txt":
            try:
                os.mkdir('txts')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        if fichero.suffix == ".jpg":
            try:
                os.mkdir('jpgs')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        if fichero.suffix == ".jpeg":
            try:
                os.mkdir('jpegs')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        if fichero.suffix == ".png":
            try:
                os.mkdir('pngs')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        if fichero.suffix == ".pdf":
            try:
                os.mkdir('pdfs')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        if fichero.suffix == ".mp3":
            try:
                os.mkdir('mp3s')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        if fichero.suffix == ".mp4":
            try:
                os.mkdir('mp4s')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

    print("Se han creado las nuevas carpetas en base a su extensión: \n")

    # Iterando sobre current_path e imprimiendo los directorios.
    for fichero in current_path.iterdir():
        if fichero.is_dir():
            print("·", fichero.name)