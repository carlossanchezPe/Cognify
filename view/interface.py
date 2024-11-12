# Clase de interfaz para interactuar con el usuario en el sistema Cognify
class InterfazCognify:
    
    # Método estático que muestra el menú principal del sistema
    @staticmethod
    def mostrar_menu():
        print("===== Sistema Cognify =====")
        print("1. Agregar criminal")
        print("2. Asignar recuerdo")
        print("3. Mostrar recuerdos de un criminal")
        print("4. Salir")

    # Método estático para pedir los datos de un criminal al usuario
    @staticmethod
    def pedir_datos_criminal():
        # Solicita el nombre del criminal
        nombre = input("Ingrese el nombre del criminal: ")
        # Solicita el tipo de delito, con opciones específicas
        tipo_delito = input("Ingrese el tipo de delito (violento/financiero/odio): ")
        # Devuelve los datos capturados (nombre y tipo de delito) como una tupla
        return nombre, tipo_delito

    # Método estático que permite al usuario seleccionar un criminal de una lista
    @staticmethod
    def seleccionar_criminal(criminales):
        # Muestra los criminales disponibles con un índice para seleccionar
        print("\nCriminales disponibles:")
        for idx, criminal in enumerate(criminales):
            # Muestra el índice, nombre y tipo de delito de cada criminal
            print(f"{idx + 1}. {criminal.nombre} ({criminal.tipo_delito})")
        # Solicita al usuario seleccionar un criminal mediante el índice
        seleccion = int(input("Seleccione el número del criminal: ")) - 1
        # Devuelve el criminal seleccionado
        return criminales[seleccion]

    # Método estático para mostrar un mensaje al usuario
    @staticmethod
    def mostrar_mensaje(mensaje):
        # Muestra el mensaje recibido, con un salto de línea
        print(f"\n{mensaje}\n")
