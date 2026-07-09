import random
from typing import Dict, List

class PalavraRepository:
    def __init__(self) -> None:
        self._palavras: List[Dict[str, str]] = [
            {"palavra": "Casa", "letra": "c"},
            {"palavra": "Bola", "letra": "b"},
            {"palavra": "Dado", "letra": "d"},
            {"palavra": "Gato", "letra": "g"},
            {"palavra": "Janela", "letra": "j"},
            {"palavra": "Mesa", "letra": "m"},
            {"palavra": "Pato", "letra": "p"},
            {"palavra": "Rato", "letra": "r"},
            {"palavra": "Sapo", "letra": "s"},
            {"palavra": "Vaca", "letra": "v"},
            {"palavra": "Leão", "letra": "l"},
            {"palavra": "Foca", "letra": "f"},
            {"palavra": "Macaco", "letra": "m"},
            {"palavra": "Pássaro", "letra": "p"},
            {"palavra": "Tatu", "letra": "t"},
            {"palavra": "Lobo", "letra": "l"},
            {"palavra": "Urso", "letra": "u"},
            {"palavra": "Zebra", "letra": "z"},
            {"palavra": "Sol", "letra": "s"},
            {"palavra": "Lua", "letra": "l"},
            {"palavra": "Cama", "letra": "c"},
            {"palavra": "Copo", "letra": "c"},
            {"palavra": "Faca", "letra": "f"},
            {"palavra": "Bota", "letra": "b"},
            {"palavra": "Panela", "letra": "p"},
            {"palavra": "Peão", "letra": "p"},
            {"palavra": "Laço", "letra": "l"},
            {"palavra": "Sino", "letra": "s"},
            {"palavra": "Vela", "letra": "v"},
            {"palavra": "Roda", "letra": "r"},
            {"palavra": "Bolo", "letra": "b"},
            {"palavra": "Doce", "letra": "d"},
            {"palavra": "Suco", "letra": "s"},
            {"palavra": "Banana", "letra": "b"},
            {"palavra": "Uva", "letra": "u"},
            {"palavra": "Sopa", "letra": "s"}
        ]

    def obter_palavra_aleatoria(self) -> Dict[str, str]:
        return random.choice(self._palavras)