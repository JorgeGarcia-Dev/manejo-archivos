import os

from app.rutas import carpeta_archivos

carpetas = []

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
        carpetas.append(fichero.suffix[1:])

    for c in carpetas:
        try:
            if not os.path.exists(f"{carpeta_archivos}/{c}s"):
                os.mkdir(f"{carpeta_archivos}/{c}s")
        except:
            continue

    print("Se han creado las nuevas carpetas en base a su extensión: \n")

    # Iterando sobre current_path e imprimiendo los directorios.
    for fichero in carpeta_archivos.iterdir():
        if fichero.is_dir():
            print("·", fichero.name)