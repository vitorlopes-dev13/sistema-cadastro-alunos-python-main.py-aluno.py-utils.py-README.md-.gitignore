class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    def situacao(self):
        return "Aprovado" if self.nota >= 7 else "Reprovado"
