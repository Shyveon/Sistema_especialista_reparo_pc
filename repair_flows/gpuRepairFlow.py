from interfaceFlow import InterfaceFlow
from gpuRepairRules import gpuRepairRules

class GpuRepairFlow(InterfaceFlow):
    
    def execute(self) -> None:
        current_rule = gpuRepairRules.first_rule
        while (True):
            print(f'{current_rule.text}\n')
            if (current_rule.next.count == 0):
                break
            user_in = input('Y/N')
            if (user_in.lower() == 'y'):
                current_rule = current_rule.next[1]
            elif (user_in.lower() == 'n'):
                current_rule = current_rule.next[0]
            else: 
                continue
        print(f'Resposta: {current_rule.text}\n')

