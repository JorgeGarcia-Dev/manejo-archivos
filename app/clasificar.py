from pathlib import Path
from rutas import carpeta_archivos

def clasificar():

    """
    Imprime los nombres de todos los archivos de la carpeta en base a las extensiones .txt, .jpg, .jpeg, .png,
    .pdf, .mp3 y .mp4.
    """

    print("Los archivos con extensión .txt son: \n")
    for archivo_path in Path(carpeta_archivos).glob("*.txt"):
        print(archivo_path.name)

    print("Los archivos con extensión .jpg son: \n")
    for archivo_path in Path(carpeta_archivos).glob("*.jpg"):
        print(archivo_path.name)

    print("Los archivos con extensión .jpeg son: \n")
    for archivo_path in Path(carpeta_archivos).glob("*.jpeg"):
        print(archivo_path.name)

    print("Los archivos con extensión .png son: \n")
    for archivo_path in Path(carpeta_archivos).glob("*.png"):
        print(archivo_path.name)

    print("Los archivos con extensión .pdf son: \n")
    for archivo_path in Path(carpeta_archivos).glob("*.pdf"):
        print(archivo_path.name)

    print("Los archivos con extensión .mp3 son: \n")
    for archivo_path in Path(carpeta_archivos).glob("*.mp3"):
        print(archivo_path.name)

    print("Los archivos con extensión .mp4 son: \n")
    for archivo_path in Path(carpeta_archivos).glob("*.mp4"):
        print(archivo_path.name)