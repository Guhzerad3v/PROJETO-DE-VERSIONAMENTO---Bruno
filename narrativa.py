import time
import random


def escrever(texto, velocidade=0.03):
    # escreve o texto letra por letra
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidade)
    print()


def pausa(segundos=1):
    # espera um tempo antes de continuar
    time.sleep(segundos)


def dialogo(personagem, fala):
    # mostra a fala de um personagem
    escrever(f'{personagem}: "{fala}"')
    pausa(0.8)


# classes que o jogador pode escolher
CLASSES = {
    "1": {"nome": "Guerreiro", "vida": 120, "mana": 20, "ataque": 15,
          "descricao": "Forte e resistente, luta de perto."},
    "2": {"nome": "Mago", "vida": 70, "mana": 100, "ataque": 8,
          "descricao": "Frágil, mas domina a magia."},
    "3": {"nome": "Arqueiro", "vida": 90, "mana": 50, "ataque": 12,
          "descricao": "Rápido e preciso, ataca de longe."},
}


def barra(valor, divisor, tamanho=12):
    # barra com parte cheia (■) e parte vazia (□)
    cheio = min(valor // divisor, tamanho)
    return "■" * cheio + "□" * (tamanho - cheio)


def mostrar_classes():
    # desenha a tela de escolha de classes
    linha = "=" * 44
    print(linha)
    print("ESCOLHA SUA CLASSE".center(44))
    print(linha)
    for numero, classe in CLASSES.items():
        print(f'[{numero}] {classe["nome"].upper()}')
        print(f'    {classe["descricao"]}')
        print(f'    Vida   {barra(classe["vida"], 10)} {classe["vida"]}')
        print(f'    Mana   {barra(classe["mana"], 10)} {classe["mana"]}')
        print(f'    Ataque {barra(classe["ataque"], 2)} {classe["ataque"]}')
        print("-" * 44)


def escolher_classe():
    # mostra as classes e pede para o jogador escolher uma
    mostrar_classes()
    while True:
        opcao = input("Digite o número da classe: ")
        if opcao in CLASSES:
            return CLASSES[opcao]
        print("Opção inválida, tente de novo.")


# árvore de eventos: cada cena tem um texto e opções que levam a outras cenas
# extras: "item" (cena que dá um item), "requer" (opção que exige um item)
# e "combate" (cena que inicia uma luta)
EVENTOS = {
    "inicio": {
        "texto": "A praça de Cinzas está cheia de gente, e ninguém faz barulho. Todos estão "
                 "parados, sorrindo para o nada. Nenhum tem sombra. Só existe uma sombra em "
                 "toda a vila: a sua, esticada no chão, apontando para o poço velho no fim da "
                 "rua, como um cachorro puxando a coleira. Uma trilha de tinta preta e fresca "
                 "sai da praça na mesma direção.",
        "opcoes": {
            "1": {"texto": "Falar com Anselmo, o padeiro, que varre a mesma pedra há horas", "destino": "padeiro"},
            "2": {"texto": "Seguir a trilha de tinta preta", "destino": "trilha"},
            "3": {"texto": "Observar a sua própria sombra", "destino": "sombra"},
        },
    },
    "padeiro": {
        "texto": "Você pergunta a Anselmo onde está a sombra dele. Ele inclina a cabeça: "
                 "'Que sombra? Nunca me senti tão leve.' Então olha para os seus pés, e o "
                 "sorriso some por um segundo. 'A sua ainda está aí. Então ele ainda não quer "
                 "você.' Antes que você pergunte quem é ele, o sorriso volta, e Anselmo "
                 "continua varrendo a mesma pedra, como se nada tivesse sido dito.",
        "opcoes": {
            "1": {"texto": "Seguir a trilha de tinta preta", "destino": "trilha"},
            "2": {"texto": "Voltar para o centro da praça", "destino": "inicio"},
        },
    },
    "sombra": {
        "texto": "Você levanta o braço. A sombra levanta o dela... um instante depois. Você "
                 "dá um passo para trás. Ela dá um passo para a frente. Agora não há dúvida: "
                 "ela quer chegar ao poço e está tentando arrastar você junto.",
        "opcoes": {
            "1": {"texto": "Deixar a sombra guiar você", "destino": "poco"},
            "2": {"texto": "Pisar na sombra para prendê-la", "destino": "pisar_sombra"},
        },
    },
    "pisar_sombra": {
        "texto": "Você pisa com força na sombra. Ela não grita, mas o chão inteiro estremece. "
                 "Na praça, todos viram a cabeça ao mesmo tempo. E sorriem. Vêm andando "
                 "devagar, de braços abertos, e você entende tarde demais: a sua sombra era "
                 "a única coisa que ainda te fazia diferente deles. Quando o primeiro toca no "
                 "seu ombro, você sente uma paz enorme. E percebe que também está sorrindo. "
                 "FIM: agora você também está leve.",
        "opcoes": {},  # sem opções = fim de jogo
    },
    "trilha": {
        "texto": "A tinta preta serpenteia entre as casas. Em cada porta por onde passa, há "
                 "uma marca de mão na madeira, do tamanho de uma mão de criança. Você conta "
                 "doze marcas. Na porta da terceira casa, uma vela de cera preta ainda queima, "
                 "e a chama não projeta sombra nenhuma. A trilha termina no poço velho e para "
                 "de repente, como se o que a deixou tivesse descido.",
        "item": "Vela de Cera Preta",
        "opcoes": {
            "1": {"texto": "Ir até o poço", "destino": "poco"},
            "2": {"texto": "Voltar para a praça", "destino": "inicio"},
        },
    },
    "poco": {
        "texto": "O poço está seco há anos. Hoje, lá no fundo, existe uma luz fraca e alguém "
                 "cantarolando uma cantiga. Você conhece essa melodia. Ninguém em Cinzas "
                 "conhece essa cantiga. Ninguém, além de você.",
        "opcoes": {
            "1": {"texto": "Perguntar: quem está aí?", "destino": "eco"},
            "2": {"texto": "Descer pela corda", "destino": "descida"},
        },
    },
    "eco": {
        "texto": "A cantiga para. Silêncio. Então uma voz igualzinha à sua, só que mais lenta, "
                 "responde lá do fundo: 'Finalmente. Achei que você nunca viria buscar o "
                 "resto de você.' Aos seus pés, a sua sombra se encolhe, como se estivesse "
                 "com medo.",
        "opcoes": {
            "1": {"texto": "Descer pela corda", "destino": "descida"},
            "2": {"texto": "Recuar e voltar para a praça", "destino": "inicio"},
        },
    },
    "descida": {
        "texto": "A corda range. Quanto mais você desce, mais frio fica e mais forte é a luz. "
                 "No fundo, dezenas de sombras estão penduradas nas paredes, todas as da vila, "
                 "balançando devagar como roupas num varal. No meio delas, há uma figura de "
                 "costas, com a sua altura e o seu jeito de ficar em pé. Ela se vira devagar. "
                 "E a sua sombra, aos seus pés, estende a mão para ela.",
        "opcoes": {
            "1": {"texto": "Encarar a figura", "destino": "figura"},
            # esta opção só aparece se o jogador tiver a vela na mochila
            "2": {"texto": "Acender a vela de cera preta", "destino": "vela", "requer": "Vela de Cera Preta"},
        },
    },
    "vela": {
        "texto": "Você acende a vela. A chama preta não faz luz, faz memória. Todas as sombras "
                 "das paredes viram o rosto para a figura, e agora você vê o rosto dela: é você "
                 "aos sete anos, chorando. 'Eu fiquei aqui, sozinho, quando você foi embora', "
                 "ela sussurra. 'Não me deixa de novo.'",
        "opcoes": {
            "1": {"texto": "Estender a mão e trazê-lo de volta", "destino": "final_paz"},
            "2": {"texto": "Não confiar e enfrentá-lo", "destino": "figura"},
        },
    },
    "figura": {
        "texto": "A figura sorri com a sua boca. 'Eu sou a parte de você que ficou aqui "
                 "embaixo quando você cresceu e esqueceu de mim. Levei as sombras da vila "
                 "para fazer um corpo. Agora só falta a sua.' Ela avança.",
        # esta cena inicia um combate e depois vai para o final de vitória ou de derrota
        "combate": {"inimigo": "O Outro Betinha", "vitoria": "final_luta", "derrota": "final_derrota"},
        "opcoes": {},
    },
    "final_paz": {
        "texto": "Você estende a mão. A criança segura. Uma por uma, as sombras se soltam das "
                 "paredes e sobem pela corda até a superfície. Quando você sai do poço, a vila "
                 "inteira pisca como quem acorda: Anselmo olha para a vassoura e começa a rir. "
                 "Só você percebe que agora tem duas sombras no chão, e as duas estão sorrindo. "
                 "FIM: mas a lenda do Betinha continua.",
        "opcoes": {},
    },
    "final_luta": {
        "texto": "Seu golpe atravessa a figura, que se desfaz em fumaça preta. As sombras "
                 "sobem pela corda e a vila desperta. Mas, ao sair do poço, você nota que a "
                 "sua sombra demora um pouco para te seguir. E, no chão, ela não faz o mesmo "
                 "gesto que você. FIM... ou será que não?",
        "opcoes": {},
    },
    "final_derrota": {
        "texto": "Você cai de joelhos. A figura encosta a mão fria na sua testa: 'Descansa.' "
                 "Quando abre os olhos, você está na praça, varrendo uma pedra, sorrindo. Não "
                 "lembra por que sente tanta falta de alguma coisa. FIM: você esqueceu quem era.",
        "opcoes": {},
    },
}


def encontrar_item(item, jogador):
    # coloca o item na mochila (só uma vez)
    if item not in jogador["mochila"]:
        jogador["mochila"].append(item)
        print(f"*** Você guardou na mochila: {item} ***")
        pausa()


def iniciar_combate(nome_inimigo, jogador):
    # PROVISÓRIO: na integração final, a Main troca isto pelo sistema de luta da Issue 2
    # aqui a chance de vitória depende do ataque da classe escolhida
    classe = jogador["classe"]
    print()
    escrever(f"*** COMBATE: {classe['nome']} contra {nome_inimigo}! ***")
    pausa()
    chance = 0.4 + classe["ataque"] / 40
    return random.random() < chance


def opcoes_disponiveis(evento, jogador):
    # esconde opções que exigem um item que o jogador ainda não tem
    disponiveis = {}
    for numero, opcao in evento["opcoes"].items():
        item_exigido = opcao.get("requer")
        if item_exigido is None or item_exigido in jogador["mochila"]:
            disponiveis[numero] = opcao
    return disponiveis


def rodar_evento(nome_evento, jogador):
    # mostra o evento, dá itens, inicia combates e vai para o próximo até a história acabar
    while True:
        evento = EVENTOS[nome_evento]
        print()
        escrever(evento["texto"])
        pausa()

        if "item" in evento:
            encontrar_item(evento["item"], jogador)

        if "combate" in evento:
            combate = evento["combate"]
            if iniciar_combate(combate["inimigo"], jogador):
                nome_evento = combate["vitoria"]
            else:
                nome_evento = combate["derrota"]
            continue

        opcoes = opcoes_disponiveis(evento, jogador)
        if not opcoes:
            return
        for numero, opcao in opcoes.items():
            print(f'[{numero}] {opcao["texto"]}')
        escolha = input("O que você faz? ")
        while escolha not in opcoes:
            escolha = input("Opção inválida, tente de novo: ")
        nome_evento = opcoes[escolha]["destino"]


if __name__ == "__main__":
    # abertura da história
    escrever("Cinzas era uma vila pequena, onde todo mundo conhecia todo mundo.")
    pausa()
    escrever("Hoje de manhã, ninguém tinha sombra.")
    pausa(1.5)
    escrever("Ninguém, exceto você.")
    pausa(1.5)
    dialogo("Velho Sábio", "Ontem à noite, algo passou pela vila e levou todas as sombras. Menos a sua.")
    dialogo("Betinha", "Por que a minha ficou?")
    dialogo("Velho Sábio", "Ele deixou de propósito. E quem perde a sombra esquece que um dia teve uma.")
    dialogo("Velho Sábio", "Eu ainda me lembro, mas não por muito tempo. Descubra o porquê antes do pôr do sol.")
    print()
    classe = escolher_classe()
    print()
    escrever(f'Betinha, o {classe["nome"]}, respira fundo e caminha até a praça...')
    pausa()
    jogador = {"classe": classe, "mochila": []}
    rodar_evento("inicio", jogador)
    print()
    print("Itens na mochila:", ", ".join(jogador["mochila"]) or "nenhum")