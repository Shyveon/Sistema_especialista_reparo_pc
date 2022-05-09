from rule import Rule

end_rules: list[Rule] = [
    Rule('Retroiluminação ou o inversor da lâmpada flourescente', (), None),
    Rule('Interferência. Verifique a área, verifique os periféricos e também veja se há transformadores perto do monitor', (), None),
    Rule('Taxa de atualização errada, abaixe a resolução da tela e desligue as luzes da sala.', (), None),
    Rule('O LCD está estragado, teste com um outro computadores antes de descartar de maneira apropriada', (), None),
    Rule('Verifique a bateria dos óculos e se os drivers estão corretos', (), None),
    Rule('Ajuste os controles da tela e verifique o comprimento do cabo e qualidade', (), None),
    Rule('Defina o LCD ou HDTV para uma taxa de atualização que é o dobro do da frequência da grid (BR 60hz, US 60hz, EU 50hz)', (), None),
    Rule('Tente uma resolução de tela diferente. Talvez os componentes internos se ajustem mas isso geralmente indica problemas de um monitor falhando', (), None),
    Rule('Corrupção de software', (), None),
    Rule('Tente os últimos drivers, atualize a BIOS. Se isso não der certo você tem um adaptador de vídeo falhando.', (), None),
    Rule('Problemas de drivers ou o adaptador de vídeo não é potente o suficiente para aguentar a nova resolução', (), None),
    Rule('Conflito de memória RAM ou a memória de vídeo está ruim', (), None),
    Rule('Verifique as configurações de tamanho se não tente selecionar uma resolução diferente', (), None),
    Rule('Prosseguir para perguntas de placa-mãe', (), None), # Aqui tem que fazer as regras de placa-mãe e redirecionar para lá
    Rule('Atualizar os drivers de vídeo, atualizar o windows, atualizar o DirectX e atualizar os softwares utilizados', None, None),
    Rule('Instale as últimas atualizações do jogo, pare outras tarefas e feche outras janelas no windows enquanto joga e provavelmente seu hardware não é potente o suficiente para o jogo em questão', (), None),
    Rule('Placas de vídeo vão diminuir o processamento quando estão sobre-aquecendo. Verifique as ventoinhas e o dissipador de calor, tente melhorar a circulação de ar no geral.', (), None)
]

question_rules: list[Rule] = [
    Rule('Erros de OpenGL?', (end_rules[13], end_rules[14]), None),
    Rule('Queda de quadros quando a placa de vídeo está quente?', (end_rules[-2], end_rules[-1]), None),
    Rule('Tamanho de texto pequeno, tela borrada ou mostrando apenas parte do desktop?', (question_rules[0], end_rules[-5]), None),
    Rule('Fragmentos de imagem ou lixo na tela?', (question_rules[2], end_rules[-6]), None),
    Rule('OK quando a resolução é diminuida?', (question_rules[1], end_rules[-7]), None),
    Rule('Lag no jogo ou travadinhas?', (question_rules[3], question_rules[4]), None),
    Rule('Tentou restaurar o sistema e verificar por malware?', (end_rules[-8], end_rules[-9]), None),
    Rule('Tela congelado parcialmente', (question_rules[5], question_rules[6]), None),
    Rule('O desktop diminui?', (question_rules[7], end_rules[-10]), None),
    
]

first_rule: Rule = Rule('O seu monitor é de tubo?', (), None)

