from pathlib import Path
from rutas import carpeta_archivos

def clasificar():

    print("Los archivos con extensión .txt son: \n")
    # Por medio de un ciclo for, iteramos sobre la carpeta con nuestros archivos, y por medio del módulo .glob()
    # buscamos los archivos que coincidan con determinado patrón, en este caso, la extensión '.txt'
    for archivo_path in Path(carpeta_archivos).glob("*.txt"):
        print(archivo_path.name)

    print("Los archivos con extensión .jpg son: \n")
    # Por medio de un ciclo for, iteramos sobre la carpeta con nuestros archivos, y por medio del módulo .glob()
    # buscamos los archivos que coincidan con determinado patrón, en este caso, la extensión '.jpg'
    for archivo_path in Path(carpeta_archivos).glob("*.jpg"):
        print(archivo_path.name)

    print("Los archivos con extensión .jpeg son: \n")
    # Por medio de un ciclo for, iteramos sobre la carpeta con nuestros archivos, y por medio del módulo .glob()
    # buscamos los archivos que coincidan con determinado patrón, en este caso, la extensión '.jpeg'
    for archivo_path in Path(carpeta_archivos).glob("*.jpeg"):
        print(archivo_path.name)

    print("Los archivos con extensión .png son: \n")
    # Por medio de un ciclo for, iteramos sobre la carpeta con nuestros archivos, y por medio del módulo .glob()
    # buscamos los archivos que coincidan con determinado patrón, en este caso, la extensión '.png'
    for archivo_path in Path(carpeta_archivos).glob("*.png"):
        print(archivo_path.name)

    print("Los archivos con extensión .pdf son: \n")
    # Por medio de un ciclo for, iteramos sobre la carpeta con nuestros archivos, y por medio del módulo .glob()
    # buscamos los archivos que coincidan con determinado patrón, en este caso, la extensión '.pdf'
    for archivo_path in Path(carpeta_archivos).glob("*.pdf"):
        print(archivo_path.name)

    print("Los archivos con extensión .mp3 son: \n")
    # Por medio de un ciclo for, iteramos sobre la carpeta con nuestros archivos, y por medio del módulo .glob()
    # buscamos los archivos que coincidan con determinado patrón, en este caso, la extensión '.mp3'
    for archivo_path in Path(carpeta_archivos).glob("*.mp3"):
        print(archivo_path.name)

    print("Los archivos con extensión .mp4 son: \n")
    # Por medio de un ciclo for, iteramos sobre la carpeta con nuestros archivos, y por medio del módulo .glob()
    # buscamos los archivos que coincidan con determinado patrón, en este caso, la extensión '.mp4'
    for archivo_path in Path(carpeta_archivos).glob("*.mp4"):
        print(archivo_path.name)