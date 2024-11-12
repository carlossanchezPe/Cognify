# Clase que representa un criminal con su nombre, tipo de delito y recuerdos asociados
class Criminal:
    # Método constructor que inicializa los atributos del criminal
    def __init__(self, nombre, tipo_delito):
        self.nombre = nombre             # Almacena el nombre del criminal
        self.tipo_delito = tipo_delito   # Almacena el tipo de delito del criminal
        self.recuerdos = []              # Inicializa una lista vacía para almacenar recuerdos

    # Método para agregar un recuerdo a la lista de recuerdos del criminal
    def agregar_recuerdo(self, recuerdo):
        self.recuerdos.append(recuerdo)  # Agrega el recuerdo a la lista de recuerdos

    # Método para mostrar los recuerdos del criminal
    def mostrar_recuerdos(self):
        for recuerdo in self.recuerdos:  # Itera sobre cada recuerdo en la lista
            print(f"- {recuerdo}")       # Imprime cada recuerdo en una línea con formato
