chamados = []

def registrar_chamado():
    nome = input("Nome do solicitante: ")
    problema = input("Descreva o problema: ")
    prioridade = input("Informe a prioridade (Baixa, Média ou Alta): ")

   chamado = {
    "solicitante": nome,
    "problema": problema,
    "status": "Aberto",
    "prioridade": prioridade
}

    chamados.append(chamado)
    print("Chamado registrado com sucesso!")

def listar_chamados():
    for chamado in chamados:
        print("--------------------")
        print("Solicitante:", chamado["solicitante"])
        print("Problema:", chamado["problema"])
        print("Status:", chamado["status"])
        print("Prioridade:", chamado["prioridade"])

print("SISTEMA DE GESTÃO DE CHAMADOS")

while True:
    print("\n1 - Registrar chamado")
    print("2 - Listar chamados")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_chamado()
    elif opcao == "2":
        listar_chamados()
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")