"""Desarrollo de algoritmo para manejo de archivos:"""

# Importamos los módulos.
from pathlib import Path
import errno
import os
import shutil

# Con cwd() identificamos la ruta hacia la carpeta donde nos encontramos.
current_path = Path.cwd()

# En una variable, almacenamos el nombre de la carpeta donde se localizan nuestros archivos.
archivos = 'Archivos'

# Concatenamos la ruta principal + la ruta de la carpeta con nuestros archivos.
carpeta_archivos = current_path / archivos

# En las variablea 'destination', indicamos nuevas las rutas hácia donde se moveran nuestros archivos. 
destination_txts = current_path / 'txts/'
destination_jpgs = current_path / 'jpgs/'
destination_jpegs = current_path / 'jpegs/'
destination_pngs = current_path / 'pngs/'
destination_pdfs = current_path / 'pdfs/'
destination_mp3s = current_path / 'mp3s/'
destination_mp4s = current_path / 'mp4s/'

# Con esta función, validamos que los datos que ingresa el usuario, son de tipo int().
def validar_numeros(message):

    while True:
        try:
            data = int(input("Selecciona " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")

# Definimos la función, en donde centramos todo nuestro programa.
def archivos():

    # En una variable indicamos que el valor inicial es de tipo Bool (True)
    preguntar = True

    # Con un ciclo while, repetiremos la misma acción mientras el valor ingresado por el usuario se encuentre en nuestro menú de opciones,
    # o indique que desea terminar el programa ingresando el valor de '5'.
    while preguntar:

        # Imprimimos nuestro menú de opciones.
        print('Seleccione del Menú lo que desea hacer: \n')
        print('1) Listar Archivos \n')
        print('2) Ver Archivos Clasificados \n')
        print('3) Crear Carpetas para los Archivos \n')
        print('4) Mover Archivos a Carpetas \n')
        print('5) Salir \n')

        # En una variable recibimos los valores u opciones que el usuario requiere.
        opcion = validar_numeros("una opción: \r\n")

        # Nuestra primer opción, y si el usuario ingresa el valor de '1',
        # será la de listar todos los archivos que se encuentran en nuestra carpeta de Archivos.
        if opcion == 1:

            print("Los archivos en la carpeta son: \n")
            # Iteramos la carpeta de archivos, para listar y mostrar por medio de un ciclo 'for' los archivos dentro de ésta.
            for fichero in carpeta_archivos.iterdir():
                # Imprimimos los archivos dentro de la carpeta, agregamos .name para que solo nos muestre los archivos sin la ruta.
                print(fichero.name)
            print('\n')

        # Nuestra segunda opción, lista los archivos, clasificándolos por medio de su extensión.
        elif opcion == 2:

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

        # Nuestra tercera opción, crea las carpetas para los archivos en base a su extensión.
        elif opcion == 3:

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

        # Nuestra cuarta ocpión, mueve los archivos desde la carpeta Archivos, a sus respectivas carpetas creadas por su tipo de extensión.
        elif opcion == 4:

            # Iteramos en nuestra carpeta de archivos.
            for fichero in carpeta_archivos.iterdir():

                # Condicionamos que si los archivos tienen la extensión '.txt', se muevan a su respectiva carpeta de destino.
                if fichero.suffix == ".txt":
                    # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
                    # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgando la nueva ruta de destino.
                    shutil.move(str(carpeta_archivos/fichero), str(destination_txts))

                # Condicionamos que si los archivos tienen la extensión '.jpg', se muevan a su respectiva carpeta de destino.
                if fichero.suffix == ".jpg":
                    # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
                    # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgando la nueva ruta de destino.
                    shutil.move(str(carpeta_archivos/fichero), str(destination_jpgs))

                # Condicionamos que si los archivos tienen la extensión '.jpeg', se muevan a su respectiva carpeta de destino.
                if fichero.suffix == ".jpeg":
                    # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
                    # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgando la nueva ruta de destino.
                    shutil.move(str(carpeta_archivos/fichero), str(destination_jpegs))

                # Condicionamos que si los archivos tienen la extensión '.png', se muevan a su respectiva carpeta de destino.
                if fichero.suffix == ".png":
                    # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
                    # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgando la nueva ruta de destino.
                    shutil.move(str(carpeta_archivos/fichero), str(destination_pngs))

                # Condicionamos que si los archivos tienen la extensión '.pdf', se muevan a su respectiva carpeta de destino.
                if fichero.suffix == ".pdf":
                    # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
                    # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgando la nueva ruta de destino.
                    shutil.move(str(carpeta_archivos/fichero), str(destination_pdfs))

                # Condicionamos que si los archivos tienen la extensión '.mp3', se muevan a su respectiva carpeta de destino.
                if fichero.suffix == ".mp3":
                    # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
                    # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgando la nueva ruta de destino.
                    shutil.move(str(carpeta_archivos/fichero), str(destination_mp3s))

                # Condicionamos que si los archivos tienen la extensión '.mp4', se muevan a su respectiva carpeta de destino.
                if fichero.suffix == ".mp4":
                    # La función de move() del Módulo Shutill, nos permite mover archivos y directorios,
                    # solo basta con asignarle la ruta donde se encuentra, así como el nombre de éstos, y aisgando la nueva ruta de destino.
                    shutil.move(str(carpeta_archivos/fichero), str(destination_mp4s))

        # Nuestra quinta y última extensión, termina el programa.
        elif opcion == 5:
            print("Programa terminado, ha sido un gusto servirte... \n")
            # Por medio de 'break' rompemos la iteración del ciclo while, terminando así nuestro programa.
            break

# Mandamos llamar a nuestra función.
archivos()