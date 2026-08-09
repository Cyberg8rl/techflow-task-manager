class Task:
    """
    Representa uma tarefa individual dentro do sistema.
    """
    def __init__(self, task_id: int, title: str, description: str, priority: str = "Média"):
        if not title.strip():
            raise ValueError("O título da tarefa não pode estar vazio.")
        
        self.id = task_id
        self.title = title
        self.description = description
        self.status = "Pendente"
        self.priority = priority  # Campo incluído para a Mudança de Escopo

    def to_dict(self):
        """Retorna os dados da tarefa em formato de dicionário."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority
        }


class TaskManager:
    """
    Gerencia o ciclo de vida e a coleção de tarefas (CRUD).
    """
    def __init__(self):
        self.tasks = {}
        self._next_id = 1

    def add_task(self, title: str, description: str, priority: str = "Média") -> Task:
        """Cria e armazena uma nova tarefa."""
        task = Task(self._next_id, title, description, priority)
        self.tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Task:
        """Busca uma tarefa pelo seu ID."""
        if task_id not in self.tasks:
            raise KeyError("Tarefa não encontrada.")
        return self.tasks[task_id]

    def list_tasks(self):
        """Retorna todas as tarefas cadastradas."""
        return [task.to_dict() for task in self.tasks.values()]

    def update_task_status(self, task_id: int, new_status: str):
        """Atualiza o status de uma tarefa existente."""
        task = self.get_task(task_id)
        task.status = new_status
        return task

    def delete_task(self, task_id: int):
        """Remove uma tarefa do sistema."""
        if task_id not in self.tasks:
            raise KeyError("Tarefa não encontrada.")
        del self.tasks[task_id]
        return True