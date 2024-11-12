# Clase que representa un recuerdo con contenido y nivel de emoción asociados
class Memory:
    # Método constructor que inicializa los atributos del recuerdo
    def __init__(self, content, emotion_level):
        self.content = content               # Almacena el contenido del recuerdo
        self.emotion_level = emotion_level   # Almacena el nivel de emoción asociado al recuerdo

    # Método especial para representar el objeto como una cadena
    def __str__(self):
        # Devuelve una representación en texto del recuerdo, mostrando su contenido y nivel de emoción
        return f"Memory(Content: {self.content}, Emotion Level: {self.emotion_level})"
