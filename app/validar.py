# Con esta función, validamos que los datos que ingresa el usuario, son de tipo int().
def validar_numeros(message):

    """
    Toma una cadena como argumento y devuelve un número entero
    :param.

    mensaje: El mensaje para mostrar al usuario
    :return: los datos.
    """

    while True:
        try:
            data = int(input("Selecciona " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")