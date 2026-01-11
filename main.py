from aluno import Aluno
from utils import ler_nota, ler_opcao

def cadastrar_aluno(alunos):
    nome = input("Digite o nome: ")
    nota = ler_nota()
    aluno = Aluno(nome, nota)
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")
def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        print(aluno.nome, "-", aluno.situacao())
def mostrar_media(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    media = sum(aluno.nota for aluno in alunos) / len(alunos)
    print("Média da turma:", media)
def mostrar_resumo(alunos):
    aprovados = sum(1 for aluno in alunos if aluno.situacao() == "Aprovado")
    reprovados = len(alunos) - aprovados
    print("\nResumo:")
    print("Total de alunos:", len(alunos))
    print("Aprovados:", aprovados)
    print("Reprovados:", reprovados)
alunos = []

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Mostrar média")
    print("0 - Sair")

    opcao = ler_opcao()
    if opcao is None:
        continue

    if opcao == "1":
        cadastrar_aluno(alunos)
    elif opcao == "2":
        listar_alunos(alunos)
    elif opcao == "3":
        mostrar_media(alunos)
        mostrar_resumo(alunos)
    elif opcao == "0":
        print("Encerrando sistema...")
        break
