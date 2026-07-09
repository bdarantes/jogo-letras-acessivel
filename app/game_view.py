import tkinter as tk
from app.game_engine import JogoEngine
from app.audio_service import AudioService

class JogoView:
    def __init__(self, root: tk.Tk, engine: JogoEngine, audio_service: AudioService) -> None:
        self.root = root
        self.engine = engine
        self.audio = audio_service

        self._configurar_janela()
        self._criar_componentes_visuais()
        self.root.bind("<Key>", self._gerenciar_teclado)

        self.root.update()
        self.audio.falar("Bem vindo ao jogo das letras! Pressione a barra de espaço para começar.")

    def _configurar_janela(self) -> None:
        self.root.title("Jogo das Letras Faladas")
        self.root.geometry("600x400")
        self.root.configure(bg="#1e1e1e")

    def _criar_componentes_visuais(self) -> None:
        tk.Label(self.root, text="Jogo das Letras", font=("Arial", 24, "bold"), fg="#ffffff", bg="#1e1e1e").pack(pady=20)

        self.label_instrucao = tk.Label(
            self.root,
            text="Pressione ESPAÇO para ouvir o desafio\nOu Esc para sair.",
            font=("Arial", 16), fg="#00ff00", bg="#1e1e1e"
        )
        self.label_instrucao.pack(pady=40)

        self.label_placar = tk.Label(self.root, text="Acertos: 0  |  Erros: 0", font=("Arial", 14), fg="#ffff00", bg="#1e1e1e")
        self.label_placar.pack(side="bottom", pady=20)

    def _gerenciar_teclado(self, event: tk.Event) -> None:
        tecla: str = event.keysym.lower()

        if tecla == "escape":
            self.root.quit()
            return

        if tecla == "space" and not self.engine.aguardando_resposta:
            palavra = self.engine.iniciar_novo_desafio()
            self.label_instrucao.config(text=f"Palavra: {palavra}\nDigite a primeira letra!", fg="#ffffff")
            self.root.update()
            self.audio.falar(f"A palavra é: {palavra}. Qual é a primeira letra?")
            return

        if self.engine.aguardando_resposta and len(tecla) == 1 and tecla.isalpha():
            correto, feedback = self.engine.validar_resposta(tecla)
            cor_feedback = "#00ff00" if correto else "#ff0000"
            
            if self.engine.palavra_atual:
                texto_tela = "Correto!" if correto else f"Era a letra {self.engine.palavra_atual['letra'].upper()}"
            else:
                texto_tela = ""

            self.label_instrucao.config(text=f"{texto_tela}\nPressione ESPAÇO para continuar.", fg=cor_feedback)
            self.label_placar.config(text=f"Acertos: {self.engine.acertos}  |  Erros: {self.engine.erros}")
            self.root.update()
            self.audio.falar(feedback + " Pressione espaço para continuar.")