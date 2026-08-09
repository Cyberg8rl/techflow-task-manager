import pytest
from src.task_manager import TaskManager

def test_add_task_success():
    """Testa a criação bem-sucedida de uma tarefa."""
    manager = TaskManager()
    task = manager.add_task("Testar Login", "Validar autenticação de usuários")
    assert task.id == 1
    assert task.title == "Testar Login"
    assert task.status == "Pendente"

def test_add_task_empty_title_error():
    """Testa se o sistema impede a criação de tarefas sem título."""
    manager = TaskManager()
    with pytest.raises(ValueError, match="O título da tarefa não pode estar vazio."):
        manager.add_task("", "Sem título")

def test_update_task_status():
    """Testa a alteração de status de uma tarefa."""
    manager = TaskManager()
    task = manager.add_task("Criar API", "Endpoints do CRUD")
    updated_task = manager.update_task_status(task.id, "Concluído")
    assert updated_task.status == "Concluído"

def test_delete_task():
    """Testa a exclusão de uma tarefa."""
    manager = TaskManager()
    task = manager.add_task("Tarefa Excluir", "Descrição")
    assert manager.delete_task(task.id) is True
    with pytest.raises(KeyError):
        manager.get_task(task.id)

def test_task_priority_change_of_scope():
    """Testa a nova funcionalidade de Prioridade (Mudança de Escopo)."""
    manager = TaskManager()
    task = manager.add_task("Serviço Crítico", "Ajustar banco", priority="Alta")
    assert task.priority == "Alta"