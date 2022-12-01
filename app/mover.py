import shutil

from rutas import *

def mover():

    # Iteramos en nuestra carpeta de archivos.
    for fichero in carpeta_archivos.iterdir():

        # Condicionamos que si los archivos tienen la extensión '.txt', se muevan a su respectiva carpeta de destino.
        if fichero.suffix == ".txt":
            # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
            # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgnando la nueva ruta de destino.
            shutil.move(str(carpeta_archivos/fichero), str(destination_txts))

        # Condicionamos que si los archivos tienen la extensión '.jpg', se muevan a su respectiva carpeta de destino.
        if fichero.suffix == ".jpg":
            # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
            # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgnando la nueva ruta de destino.
            shutil.move(str(carpeta_archivos/fichero), str(destination_jpgs))

        # Condicionamos que si los archivos tienen la extensión '.jpeg', se muevan a su respectiva carpeta de destino.
        if fichero.suffix == ".jpeg":
            # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
            # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgnando la nueva ruta de destino.
            shutil.move(str(carpeta_archivos/fichero), str(destination_jpegs))

        # Condicionamos que si los archivos tienen la extensión '.png', se muevan a su respectiva carpeta de destino.
        if fichero.suffix == ".png":
            # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
            # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgnando la nueva ruta de destino.
            shutil.move(str(carpeta_archivos/fichero), str(destination_pngs))

        # Condicionamos que si los archivos tienen la extensión '.pdf', se muevan a su respectiva carpeta de destino.
        if fichero.suffix == ".pdf":
            # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
            # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgnando la nueva ruta de destino.
            shutil.move(str(carpeta_archivos/fichero), str(destination_pdfs))

        # Condicionamos que si los archivos tienen la extensión '.mp3', se muevan a su respectiva carpeta de destino.
        if fichero.suffix == ".mp3":
            # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
            # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgando la nueva ruta de destino.
            shutil.move(str(carpeta_archivos/fichero), str(destination_mp3s))

        # Condicionamos que si los archivos tienen la extensión '.mp4', se muevan a su respectiva carpeta de destino.
        if fichero.suffix == ".mp4":
            # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
            # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgnando la nueva ruta de destino.
            shutil.move(str(carpeta_archivos/fichero), str(destination_mp4s))