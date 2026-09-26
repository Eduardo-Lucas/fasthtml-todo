from fasthtml.common import Button, Form, Input, Li, Span, Ul
from fasthtml.pico import Group

from app.db import Todo


def todo_item(todo: Todo) -> Li:
    target = f"#todo-{todo.id}"
    return Li(
        Input(
            type="checkbox",
            checked=bool(todo.done),
            hx_post=f"/todos/{todo.id}/toggle",
            hx_target=target,
            hx_swap="outerHTML",
        ),
        Span(todo.title, cls="done" if todo.done else None),
        Button(
            "✕",
            hx_delete=f"/todos/{todo.id}",
            hx_target=target,
            hx_swap="outerHTML",
            cls="secondary outline",
        ),
        id=f"todo-{todo.id}",
    )


def todo_form() -> Form:
    return Form(
        Group(
            Input(name="title", placeholder="What needs doing?", required=True),
            Button("Add"),
        ),
        hx_post="/todos",
        hx_target="#todo-list",
        hx_swap="beforeend",
        **{"hx-on::after-request": "this.reset()"},
    )


def todo_list(items: list[Todo]) -> Ul:
    return Ul(*map(todo_item, items), id="todo-list")
