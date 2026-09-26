from fasthtml.common import Titled

from app.components import todo_form, todo_item, todo_list
from app.db import Todo, todos


def register(app) -> None:
    @app.get("/")
    def index():
        return Titled("My Todos", todo_form(), todo_list(todos()))

    @app.post("/todos")
    def create(title: str):
        return todo_item(todos.insert(Todo(title=title.strip())))

    @app.post("/todos/{id}/toggle")
    def toggle(id: int):
        todo = todos[id]
        todo.done = not todo.done
        return todo_item(todos.update(todo))

    @app.delete("/todos/{id}")
    def delete(id: int):
        todos.delete(id)
        return ""  # empty response + outerHTML swap removes the <li>
