def sugerir_prioridade(tarefa):
    tarefa = tarefa.lower()

    if "estudar" in tarefa or "prova" in tarefa:
        return "🔥 Alta prioridade"
    elif "trabalho" in tarefa:
        return "⚠️ Média prioridade"
    else:
        return "✅ Baixa prioridade"
