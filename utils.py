def ler_nota():
    while True:
        try:
            nota = float(input("Digite a nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")
def ler_opcao():
    opcao = input("Escolha uma opção: ")
    if opcao in ["1", "2", "3", "0"]:
        return opcao
    print("Opção inválida!")
    return None
