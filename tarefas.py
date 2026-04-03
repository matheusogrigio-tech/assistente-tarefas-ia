tarefas = []

def adicionar_tarefa(nome):
    tarefas.append({"nome": nome, "status": "pendente"})

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    for i, t in enumerate(tarefas):
        print(f"{i} - {t['nome']} ({t['status']})")

def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["status"] = "concluída"
        print("Tarefa concluída!")
    else:
        print("Índice inválido!")
