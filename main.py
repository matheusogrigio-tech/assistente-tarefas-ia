from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa
from ia import sugerir_prioridade

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite a tarefa: ")
        adicionar_tarefa(nome)
        print("Sugestão da IA:", sugerir_prioridade(nome))

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        listar_tarefas()
        try:
            i = int(input("Digite o número da tarefa: "))
            concluir_tarefa(i)
        except:
            print("Digite um número válido!")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
