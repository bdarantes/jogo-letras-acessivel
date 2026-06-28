import pyttsx3
import threading

class AudioService:
    def __init__(self):
        self.engine = pyttsx3.init()
        self._configurar_voz()

    def _configurar_voz(self):
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)

    def falar(self, texto):
        def _executar():
            if not self.engine.inLoop():
                self.engine.say(texto)
                self.engine.runAndWait()

        threading.Thread(target=_executar, daemon=True).start()