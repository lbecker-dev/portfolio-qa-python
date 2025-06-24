# to_do_list.py
tarefas = []

def mostrar_menu():
    print("\n📋 Menu de Tarefas:")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("✅ Tarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n📌 Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")

def remover_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= indice <= len(tarefas):
            tarefa = tarefas.pop(indice - 1)
            print(f"❌ Tarefa '{tarefa}' removida.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        print("Saindo... 👋")
        break
    else:
        print("Opção inválida.")
