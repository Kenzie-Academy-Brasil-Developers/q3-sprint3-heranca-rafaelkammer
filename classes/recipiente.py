# Desenvolva sua classe Recipiente aqui.
class Recipiente:

    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = True) -> None:
        self.tamanho = tamanho if(tamanho >= 0) else 0
        self.conteudo = conteudo
        self.limpo = limpo

    def esvaziar(self) -> None:
        self.conteudo = 0

    def esta_vazio(self):
        return self.conteudo == 0

    def lavar(self) -> None:
        self.limpo = True
        self.conteudo = 0

    def esta_limpo(self):
        return self.limpo

    def estado(self):
        return "limpo" if self.limpo else "sujo"

    def sujar(self) -> None:
        self.limpo = False

    def __repr__(self) -> str:
        return f"Um recipiente {self.estado()} não especificado"

    def __str__(self) -> str:
        return f"Um recipiente {self.estado()} não especificado"