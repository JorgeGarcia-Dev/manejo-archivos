import errno
import os

from rutas import current_path
from rutas import carpeta_archivos

def crear():
    
    # Por medio de un ciclo for, iteramos sobre nuestra carpeta de archivos.
    for fichero in carpeta_archivos.iterdir():
        # Condicionamos que si el fichero(archivo) es igual a la extensión ('.txt'), creamos la carpeta de la extensión.
        # Esta la determinamos con .suffix.
        if fichero.suffix == ".txt":
            # En caso de encontrar el archivo, crea la parpeta.
            try:
                os.mkdir('txts')
            # En este caso, estamos manejando el error al crear la carpeta,
            # este surge en caso de ya tenerla creada y querer crearla de nuevo.
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        # Condicionamos que si el fichero(archivo) es igual a la extensión ('.jpg'), creamos la carpeta de la extensión.
        # Esta la determinamos con .suffix.
        if fichero.suffix == ".jpg":
            # En caso de encontrar el archivo, crea la parpeta.
            try:
                os.mkdir('jpgs')
            # En este caso, estamos manejando el error al crear la carpeta,
            # este surge en caso de ya tenerla creada y querer crearla de nuevo.
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        # Condicionamos que si el fichero(archivo) es igual a la extensión ('.jpeg'), creamos la carpeta de la extensión.
        if fichero.suffix == ".jpeg":
            # En caso de encontrar el archivo, crea la parpeta.
            try:
                os.mkdir('jpegs')
            # En este caso, estamos manejando el error al crear la carpeta,
            # este surge en caso de ya tenerla creada y querer crearla de nuevo.
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        # Condicionamos que si el fichero(archivo) es igual a la extensión ('.png'), creamos la carpeta de la extensión.
        if fichero.suffix == ".png":
            # En caso de encontrar el archivo, crea la parpeta.
            try:
                os.mkdir('pngs')
            # En este caso, estamos manejando el error al crear la carpeta,
            # este surge en caso de ya tenerla creada y querer crearla de nuevo.
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        # Condicionamos que si el fichero(archivo) es igual a la extensión ('.pdf'), creamos la carpeta de la extensión.
        if fichero.suffix == ".pdf":
            # En caso de encontrar el archivo, crea la parpeta.
            try:
                os.mkdir('pdfs')
            # En este caso, estamos manejando el error al crear la carpeta,
            # este surge en caso de ya tenerla creada y querer crearla de nuevo.
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        # Condicionamos que si el fichero(archivo) es igual a la extensión ('.mp3'), creamos la carpeta de la extensión.
        if fichero.suffix == ".mp3":
            # En caso de encontrar el archivo, crea la parpeta.
            try:
                os.mkdir('mp3s')
            # En este caso, estamos manejando el error al crear la carpeta,
            # este surge en caso de ya tenerla creada y querer crearla de nuevo.
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        # Condicionamos que si el fichero(archivo) es igual a la extensión ('.mp4'), creamos la carpeta de la extensión.
        if fichero.suffix == ".mp4":
            # En caso de encontrar el archivo, crea la parpeta.
            try:
                os.mkdir('mp4s')
            # En este caso, estamos manejando el error al crear la carpeta,
            # este surge en caso de ya tenerla creada y querer crearla de nuevo.
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

    print("Se han creado las nuevas carpetas en base a su extensión: \n")

    # Iteramos sobre nuestra carpeta principal(current_path). 
    for fichero in current_path.iterdir():
        # Si los ficheros son de tipo dir, los imprime en la terminal.
        if fichero.is_dir():
            print("·", fichero.name)