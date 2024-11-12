# Importa la clase ControladorCognify desde el módulo controller.main_controller
from controller.main_controller import ControladorCognify
# Importa la clase InterfazCognify desde el módulo view.interface
from view.interface import InterfazCognify

# Función principal del programa
def main():
    # Crea una instancia del controlador para gestionar la lógica de negocio
    controlador = ControladorCognify()
    # Crea una instancia de la interfaz para manejar la interacción con el usuario
    interfaz = InterfazCognify()

    # Bucle infinito para mostrar el menú y realizar acciones según la selección del usuario
    while True:
        # Muestra el menú de opciones al usuario
        interfaz.mostrar_menu()
        # Solicita una opción del menú al usuario
        opcion = input("Seleccione una opción: ")

        # Opción 1: Agregar un nuevo criminal
        if opcion == "1":
            # Solicita los datos del criminal al usuario
            nombre, tipo_delito = interfaz.pedir_datos_criminal()
            # Agrega el criminal al sistema usando el controlador
            controlador.agregar_criminal(nombre, tipo_delito)
            # Muestra un mensaje de confirmación al usuario
            interfaz.mostrar_mensaje("Criminal agregado correctamente.")

        # Opción 2: Asignar un recuerdo a un criminal
        elif opcion == "2":
            # Verifica si hay criminales registrados en el sistema
            if not controlador.criminales:
                interfaz.mostrar_mensaje("No hay criminales registrados.")
            else:
                # Permite al usuario seleccionar un criminal
                criminal = interfaz.seleccionar_criminal(controlador.criminales)
                # Asigna un recuerdo al criminal seleccionado
                controlador.asignar_recuerdo_a_criminal(criminal)
                # Muestra un mensaje confirmando la asignación
                interfaz.mostrar_mensaje(f"Recuerdo asignado a {criminal.nombre}.")

        # Opción 3: Mostrar recuerdos de un criminal
        elif opcion == "3":
            # Verifica si hay criminales registrados en el sistema
            if not controlador.criminales:
                interfaz.mostrar_mensaje("No hay criminales registrados.")
            else:
                # Permite al usuario seleccionar un criminal
                criminal = interfaz.seleccionar_criminal(controlador.criminales)
                # Muestra un mensaje indicando los recuerdos del criminal
                interfaz.mostrar_mensaje(f"Recuerdos de {criminal.nombre}:")
                # Llama a la función para mostrar los recuerdos del criminal
                criminal.mostrar_recuerdos()

        # Opción 4: Salir del programa
        elif opcion == "4":
            # Muestra un mensaje de despedida y sale del bucle
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        # Caso de opción inválida
        else:
            # Muestra un mensaje de error si la opción no es válida
            interfaz.mostrar_mensaje("Opción no válida. Intente de nuevo.")

# Ejecuta la función main solo si este archivo se ejecuta como script principal
if __name__ == "__main__":
    main()
