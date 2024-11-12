# Importa la clase Enum para crear una enumeración de tipos de delitos
from enum import Enum

# Define una enumeración para los tipos de delitos
class TipoDelito(Enum):
    VIOLENTO = "Delito Violento"        # Representa un delito de tipo violento
    FINANCIERO = "Delito Financiero"     # Representa un delito de tipo financiero
    ODIO = "Delito de Odio"              # Representa un delito de odio
