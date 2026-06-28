import tkinter as tk

class GameView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo das Letras Acessível")
        self.geometry("800x600")
        self.configure(bg="black")


        self.label_instrucao = tk.Label(
            self,
            text="Pressione ESPAÇO para ouvir a palavra.",
            font=("Arial", 24, "bold"),
            bg="black",
            fg="yellow"
        )
        self.label_instrucao.pack(expand=True)

        self.label_feedback  = tk.Label(
            self,
            text="",
            font=("Arial", 28, "bold"),
            bg = "black",
            fg="white"
        )
        self.label_feedback.pack(expand=True)


    def atualizar_tela(self, texto, cor="white"):
        self.label_feedback.config(text=texto, fg=cor)
