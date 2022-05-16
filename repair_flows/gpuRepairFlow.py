from interfaceFlow import InterfaceFlow
from gpuRepairRules import first_rule
from ansi_helper import clear_console, green, red, reset_color

class GpuRepairFlow(InterfaceFlow):
    
    def execute(self) -> None:
        current_rule = first_rule
        while (True):
            print(clear_console, end="") # limpa a tela
            if (len(current_rule.next) == 0):
                break
            
            print(f'{current_rule.text}\n')

            user_in = input(f'{green}Y{reset_color}/{red}N{reset_color}: ')
            if (user_in.lower() == 'y'):
                current_rule = current_rule.next[1]
            elif (user_in.lower() == 'n'):
                current_rule = current_rule.next[0]
            else: 
                continue
        print(f'Resposta: {red}{current_rule.text}{reset_color}\n')

