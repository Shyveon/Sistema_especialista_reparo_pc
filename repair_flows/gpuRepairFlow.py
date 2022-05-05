import typing
from interfaceFlow import InterfaceFlow
from rule import Rule

class GpuRepairFlow(InterfaceFlow):
    
    list_rules: list[Rule] = [
        Rule('O seu monitor está rosa, apagado ou irregular?', (), None),
        Rule('A imagem está ondulada?', (), None),
        Rule('Aparecem linhas sólidas ou faixas')
    ]
    firstRule: Rule = Rule('O seu monitor é de tubo?', (list_rules[0], list_rules[1]), None)
    
    def execute(self) -> None:
        """Override do execute de InterfaceFlow"""

