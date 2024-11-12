# Importa la clase Memory desde el módulo model
from model.memory import Memory

# Clase que representa una simulación de rehabilitación para un criminal con un recuerdo específico
class Simulation:
    # Método constructor que inicializa los atributos de la simulación
    def __init__(self, criminal, memory):
        self.criminal = criminal   # Almacena la instancia del criminal para la simulación
        self.memory = memory       # Almacena el recuerdo que se usará en la simulación

    # Método que ejecuta la simulación de rehabilitación
    def run(self):
        # Muestra un mensaje indicando que la simulación de rehabilitación ha comenzado
        print(f"Simulando la rehabilitación de {self.criminal.name}...")
        # Muestra el recuerdo asociado a la simulación
        print(f"Recuerdo: {self.memory}")
        # Marca al criminal como rehabilitado cambiando su atributo correspondiente
        self.criminal.rehabilitated = True
        # Muestra un mensaje indicando que el criminal ha sido rehabilitado
        print(f"¡{self.criminal.name} ha sido rehabilitado!")
