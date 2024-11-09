from .records import Experiment, Try
from IPython.display import HTML
from typing import Any, Self

__all__ = ['Builder', 'report_builder']

class _DisplayStr(str): ...

class Builder:
    @classmethod
    def create(cls, persist_path: str) -> Self: ...
    persist_path: str
    experiments: dict[Any, Experiment]
    aliases: dict[str, list[Any]]
    current_experiment: Experiment | None
    current_try: Try | None
    def __init__(self, persist_path: str) -> None: ...
    @property
    def current_version(self) -> str | None: ...
    def navigate(self, version: Any, try_number: int = -1) -> None: ...
    def experiment(self, name: str, navigate: bool = True) -> None: ...
    def alias(self, al: Any) -> None: ...
    def try_(self, navigate: bool = True) -> None: ...
    def goal(self, text: str) -> None: ...
    def result(self, text: str) -> None: ...
    def try_status(self, status: bool, status_message: str = '') -> None: ...
    def versions(self) -> str: ...
    def report(self, *, current_only: bool = False) -> HTML: ...
    def save(self) -> None: ...

def report_builder(persist_path: str) -> Builder: ...
