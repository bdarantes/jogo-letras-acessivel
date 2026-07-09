from typing import Dict, Optional, Tuple
from app.repository import PalavraRepository

class JogoEngine:
    def __init__(self, repository: PalavraRepository) -> None:
        self.repository = repository
        self.acertos: int = 0
        self.erros: int = 0
        self.palavra_atual: Optional[Dict[str, str]] = None
        self.aguardando_resposta: bool = False
        
    def iniciar_novo_desafio(self) -> str:
        self.palavra_atual = self.repository.obter_palavra_aleatoria()
        self.aguardando_reposta = True
        return self.palavra_atual["palavra"]
    
    def validar_resposta(self, letra_digitada: str) -> Tuple[bool, str]:
        if not self.palavra_atual:
            return False, "Nenhum desafio iniciado."
        
        self.aguardando_reposta = False
        letra_correta = self.palavra_atual["letra"]
        palavra = self.palavra_atual["palavra"]
        
        if letra_digitada == letra_correta:
            self.acertos += 1
            feedback = f"Muito bem! Você acertou. {palavra} começa com a letra {letra_correta.upper()}."
            correto = True
        
        else:
            self.erros += 1
            feedback = f"Quase lá! Você digitou {letra_digitada.upper()}, mas {palavra} começa com a letra {letra_correta.upper()}."
            
        return correto, feedback