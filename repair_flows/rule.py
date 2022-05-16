from __future__ import annotations
from interfaceFlow import InterfaceFlow

class Rule:                           # Tupla <Regra caso Falso, Regra caso Verdadeiro>
    def __init__(self, text: str, next: tuple['Rule', 'Rule']) -> None:
        self.text: str = text
        self.next: tuple[Rule, Rule] = next
