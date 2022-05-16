from rule import Rule

nodes: list[Rule] = [
    Rule('Retroiluminação ou o inversor da lâmpada flourescente', ()),
    Rule('Interferência. Verifique a área, verifique os periféricos e também veja se há transformadores perto do monitor', ()),
    Rule('Taxa de atualização errada, abaixe a resolução da tela e desligue as luzes da sala.', ()),
    Rule('O LCD está estragado, teste com um outro computadores antes de descartar de maneira apropriada', ()),
    Rule('Verifique a bateria dos óculos e se os drivers estão corretos', ()),
    Rule('Ajuste os controles da tela, verifique o comprimento do cabo e a sua qualidade', ()),
    Rule('Defina o LCD ou HDTV para uma taxa de atualização que é o dobro do da frequência da grid (BR 60hz, US 60hz, EU 50hz)', ()),
    Rule('Tente uma resolução de tela diferente. Talvez os componentes internos se ajustem mas isso geralmente indica problemas de um monitor falhando', ()),
    Rule('Corrupção de software', ()),
    Rule('Tente os últimos drivers, atualize a BIOS. Se isso não der certo você tem um adaptador de vídeo falhando.', ()),
    Rule('Problemas de drivers ou o adaptador de vídeo não é potente o suficiente para aguentar a nova resolução', ()),
    Rule('Conflito de memória RAM ou a memória de vídeo está ruim', ()),
    Rule('Verifique as configurações de tamanho se não tente selecionar uma resolução diferente', ()),
    Rule('Provavelmente problemas de placa-mãe', ()),
    Rule('Atualizar os drivers de vídeo, atualizar o windows, atualizar o DirectX e atualizar os softwares utilizados', ()),
    Rule('Instale as últimas atualizações do jogo, pare outras tarefas e feche outras janelas no windows enquanto joga e provavelmente seu hardware não é potente o suficiente para o jogo em questão', ()),
    Rule('Placas de vídeo vão diminuir o processamento quando estão sobre-aquecendo. Verifique as ventoinhas e o dissipador de calor, tente melhorar a circulação de ar no geral.', ())
]

partial_screen_freeze = Rule('Tela congelado parcialmente', 
    (
        Rule('Lag no jogo ou travadinhas?', 
            (
                Rule('Fragmentos de imagem ou lixo na tela?', 
                    (
                        Rule('Tamanho de texto pequeno, tela borrada ou mostrando apenas parte do desktop?',
                            (
                                Rule('Erros de OpenGL?', (nodes[13], nodes[14])),
                                nodes[-5]
                            )),
                        nodes[-6]
                    )),
                Rule('OK quando a resolução é diminuida?', 
                    (
                        Rule('Queda de quadros quando a placa de vídeo está quente?', (nodes[-2], nodes[-1])),
                        nodes[-7]
                    ))
            )),
        Rule('Tentou restaurar o sistema e verificar por malware?', (nodes[-8], nodes[-9])),
    ))

edges: dict[Rule] = {
    'pink':Rule('A tela está rosa, apagada ou desbalanceada?',
    (
        Rule('Linhas sólidas ou faixas pretas na tela?',
            (
                Rule('Falha no 3D?',
                (
                    Rule('O 3D está piscando?', (partial_screen_freeze, nodes[6])),
                    nodes[4]
                )),
                nodes[3]
            )),
            nodes[0]
    )),

    'wavy':Rule('A imagem está ondulada?',
    ( 
        Rule('Imagem distorcida ou piscando?', 
            (   Rule('A tela está escura ou as cores estão ruins?', 
                (
                    Rule('O desktop diminui?', 
                    (
                        partial_screen_freeze,
                        nodes[-10]
                    )),
                    nodes[5]
                )),
                nodes[2]
            )),
        nodes[1]
    ))
}

first_rule: Rule = Rule('O seu monitor é de tubo?', (edges['pink'], edges['wavy']))

