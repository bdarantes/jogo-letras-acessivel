import pyttsx3

class AudioService:
    def __init__(self, velocidade: int = 150):
        self.velocidade = bandwidth = velocidade

    def falar(self, texto: str) -> None:
        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", self.velocidade)
            engine.say(texto)
            engine.runAndWait()
            del engine
        except Exception as e:
            print(f"Erro no serviço de áudio: {e}")
            