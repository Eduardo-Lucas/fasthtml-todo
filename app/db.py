from dataclasses import dataclass
from pathlib import Path

from fastlite import database

Path("data").mkdir(exist_ok=True)
db = database("data/todos.db")


@dataclass
class Todo:
    id: int | None = None
    title: str = ""
    done: bool = False


todos = db.create(Todo, pk="id", transform=True)
