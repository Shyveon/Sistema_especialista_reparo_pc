from repair_flows.interfaceFlow import InterfaceFlow

class Rule:                           # Tupla <Regra caso Falso, Regra caso Verdadeiro>
    def __init__(self, text: str, next: tuple[Rule, Rule], next_flow: InterfaceFlow) -> None:
        self.text: str = text
        self.next: tuple[Rule, Rule] = next
        self.next_flow: InterfaceFlow = next_flow
    
    answered: bool = False
    value: bool = False

    def answer(self):
        result: str = input(self.text)
        self.answered = True
        if result == 'T':
            self.value = True
