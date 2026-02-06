# Tema 2 - Fundamentos e Técnicas Avançadas

def menu():
    print("\nMENU")
    print("1 - Somar números")
    print("2 - Listar números cadastrados")
    print("3 - Calcular média")
    print("0 - Sair")


numeros = []


def somar_numeros():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print("Resultado da soma:", a + b)


def adicionar_numero():
    n = float(input("Digite um número para cadastrar: "))
    numeros.append(n)
    print("Número adicionado com sucesso!")


def listar_numeros():
    if not numeros:
        print("Nenhum número cadastrado.")
    else:
        print("Números cadastrados:")
        for n in numeros:
            print(n)


def calcular_media():
    if not numeros:
        print("Não é possível calcular média.")
    else:
        media = sum(numeros) / len(numeros)
        print("Média:", media)


opcao = -1

while opcao != 0:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        somar_numeros()
    elif opcao == 2:
        adicionar_numero()
    elif opcao == 3:
        calcular_media()
    elif opcao == 0:
        print("Encerrando o programa.")
    else:
        print("Opção inválida.")
