from rutas import carpeta_archivos

def listar():
    
    print("Los archivos en la carpeta son: \n")
    # Iteramos la carpeta de archivos, para listar y mostrar por medio de un ciclo 'for' los archivos dentro de ésta.
    for fichero in carpeta_archivos.iterdir():
        # Imprimimos los archivos dentro de la carpeta, agregamos .name para que solo nos muestre los archivos sin la ruta.
        print(fichero.name)
    print('\n')