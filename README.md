# TechFlow Task Manager

Projeto em Python para gerenciar tarefas em memória, com operações de criação, consulta, listagem, atualização de status e exclusão. O código também valida títulos vazios e permite definir prioridade para cada tarefa.

## Funcionalidades implementadas

- Criar tarefas com título, descrição e prioridade.
- Gerar IDs sequenciais para as tarefas.
- Consultar uma tarefa pelo ID e listar as tarefas cadastradas.
- Atualizar o status e excluir tarefas.
- Retornar erros explícitos para título vazio e ID inexistente.

## Tecnologias

- Python
- pytest

## Estrutura

- `src/task_manager.py`: classes `Task` e `TaskManager`.
- `tests/test_task_manager.py`: testes automatizados para criação, validação, atualização, exclusão e prioridade.
- `requirements.txt`: dependências do projeto.
- `.github/workflows/ci.yml`: configuração de integração contínua.

## Como executar os testes

Com Python instalado, crie e ative um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
```

No Windows:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -v
```

No macOS/Linux, ative o ambiente com `source .venv/bin/activate` antes de instalar as dependências.

## Limitações atuais

As tarefas ficam apenas na memória durante a execução: não há persistência em arquivo ou banco de dados, nem interface web. O projeto demonstra lógica de negócio e testes, não um gerenciador pronto para produção.
