from gastos import adicionar_gasto, listar_gastos, remover_gasto
from api import obter_cotacao

def menu():
    print("\n--- CONTROLE DE GASTOS ---")
    print("1 - Adicionar gasto")
    print("2 - Listar gastos")
    print("3 - Remover gasto")
    print("4 - Ver total")
    print("5 - Ver cotação do dólar")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        adicionar_gasto(descricao, valor)

    elif opcao == "2":
        gastos = listar_gastos()
        for i, g in enumerate(gastos):
            print(f"{i} - {g['descricao']} | R$ {g['valor']}")

    elif opcao == "3":
        indice = int(input("Índice para remover: "))
        remover_gasto(indice)

    elif opcao == "4":
        gastos = listar_gastos()
        total = sum(g["valor"] for g in gastos)
        print(f"Total: R$ {total}")

    elif opcao == "5":
        cotacao = obter_cotacao("USD")
        if cotacao:
            print(f"Dólar hoje: R$ {cotacao}")
        else:
            print("Erro ao buscar cotação")

    elif opcao == "0":
        break

    else:
        print("Opção inválida")
