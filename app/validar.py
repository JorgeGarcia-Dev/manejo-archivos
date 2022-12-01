# Con esta función, validamos que los datos que ingresa el usuario, son de tipo int().
def validar_numeros(message):

    while True:
        try:
            data = int(input("Selecciona " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")