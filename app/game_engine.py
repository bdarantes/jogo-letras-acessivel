class GameEngine:
    def __init__(self, repository, audio_service, view):
        self.repository = repository
        self.audio = audio_service
        self.view = view

        self.palavra_atual = ""
        self.letra_correta = ""
        self.pontuacao = 0

        self.view.bind("<space>", self.reproduzir_palavra)
        self.view.bind("<key>", self.analisar_entrada_teclado)

        self.iniciar_nova_rodada()

    def iniciar_nova_rodada(self):
        dados_palavra = self.repository.obter_palavra_aleatoria()
        self.palavra_atual = dados_palavra["palavra"]
        self.letra_correta = dados_palavra["letra"].lower() 
        
    def reproduziar_palavra(self, event=None):
        self.audio.falar(f"A palavra é: {self.palavra_atual}. Repito: {self.palavra_atual}. Digite a primeira letra.")

    def analisar_entrada_teclado(self, event):
        if event.keysym == "space":
            return
        
        letra_digitada = event.char.lower()

        if not letra_digitada.isalpha() or len(letra_digitada) != 1:
            return
        
        if letra_digitada == self.letra_correta:
            self.pontuacao += 10
            self.view.atualizar_tela(f"Acertou! Letra {letra_digitada.upper()}", "green")
            self.audio.falar(f"Muito bem! Você acertou. Letra {letra_digitada}. Você ganhou dez pontos.")
            self.view.after(2500, self.iniciar_nova_rodada)
        else:
             self.view.atualizar_tela("Tente outra vez!", "red")
             self.audio.falar(f"Letra {letra_digitada} incorreta. Tente novamente.")