# Importa la clase Criminal desde el módulo model
from model.criminal import Criminal

# Clase que representa el controlador principal del sistema Cognify
class ControladorCognify:
    # Método constructor que inicializa la lista de criminales
    def __init__(self):
        self.criminales = []  # Lista para almacenar los criminales registrados

    # Método para agregar un nuevo criminal al sistema
    def agregar_criminal(self, nombre, tipo_delito):
        # Crea una nueva instancia de Criminal con el nombre y tipo de delito proporcionados
        nuevo_criminal = Criminal(nombre, tipo_delito)
        # Agrega el nuevo criminal a la lista de criminales
        self.criminales.append(nuevo_criminal)
        return nuevo_criminal  # Devuelve la instancia del criminal agregado

    # Método para crear un recuerdo específico basado en el tipo de delito
    def crear_recuerdo(self, tipo_delito):
        # Asigna un recuerdo específico según el tipo de delito
        if tipo_delito == "violento":
            return "Recuerdo: perspectiva de la víctima y su sufrimiento."
        elif tipo_delito == "financiero":
            return "Recuerdo: impacto económico y social de sus acciones."
        elif tipo_delito == "odio":
            return "Recuerdo: experiencias que promueven respeto y diversidad."
        else:
            # Retorna un recuerdo genérico si el tipo de delito no está especificado
            return "Recuerdo genérico: reflexión sobre las consecuencias del delito."

    # Método para asignar un recuerdo a un criminal específico
    def asignar_recuerdo_a_criminal(self, criminal):
        # Crea un recuerdo basado en el tipo de delito del criminal
        recuerdo = self.crear_recuerdo(criminal.tipo_delito)
        # Agrega el recuerdo al criminal utilizando su método agregar_recuerdo
        criminal.agregar_recuerdo(recuerdo)
