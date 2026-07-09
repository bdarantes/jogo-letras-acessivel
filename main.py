import tkinter as tk
from app.repository import PalavraRepository
from app.game_engine import JogoEngine
from app.audio_service import AudioService
from app.game_view import JogoView

def main() -> None:
    repository = PalavraRepository()
    engine = JogoEngine(repository=repository)
    audio_service = AudioService(velocidade=150)

    root = tk.Tk()
    app = JogoView(root=root, engine=engine, audio_service=audio_service)
    root.mainloop()

if __name__ == "__main__":
    main()