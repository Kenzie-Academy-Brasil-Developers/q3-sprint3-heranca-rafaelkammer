# Desenvolva sua classe Copo aqui.
from classes.recipiente import Recipiente

class Copo(Recipiente):
    def __init__(self, tamanho: float) -> None:
        super().__init__(tamanho)

    def encher(self, bebida: str = "água"):

        if self.limpo:
            self.limpo = False
            self.conteudo = self.tamanho
            self.bebida = bebida

        return "Não se pode encher um copo sujo"

    def beber(self, quantidade: float):
        if quantidade <= 0:
            return "Quantidade deve ser positiva"

        if quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"

        self.conteudo = self.conteudo - quantidade

    def lavar(self)-> None:
        self.bebida = None
        self.conteudo = 0
        self.limpo = True

    def __repr__(self) -> str:
        return f"Um copo vazio de {self.tamanho}ml" if self.conteudo == 0 else f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"

    def __str__(self) -> str:
        return f"Um copo vazio de {self.tamanho}ml" if self.conteudo == 0 else f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"