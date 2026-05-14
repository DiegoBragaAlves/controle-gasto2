import json

ARQUIVO = "dados.json"

def carregar_gastos():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar_gastos(gastos):
    with open(ARQUIVO, "w") as f:
        json.dump(gastos, f, indent=4)

def adicionar_gasto(descricao, valor):
    gastos = carregar_gastos()
    gastos.append({"descricao": descricao, "valor": valor})
    salvar_gastos(gastos)

def listar_gastos():
    return carregar_gastos()

def remover_gasto(indice):
    gastos = carregar_gastos()
    if 0 <= indice < len(gastos):
        gastos.pop(indice)
        salvar_gastos(gastos)
