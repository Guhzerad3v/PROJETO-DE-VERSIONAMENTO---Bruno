import time


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
                 "doze marcas. A trilha termina no poço velho e para de repente, como se o "
                 "que a deixou tivesse descido.",
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
                 "E a sua sombra, aos seus pés, estende a mão para ela... (continua)",
        "opcoes": {},  # sem opções = fim da história por enquanto
    },
}


def rodar_evento(nome_evento):
    # mostra o evento, pede a escolha e vai para o próximo até a história acabar
    while True:
        evento = EVENTOS[nome_evento]
        print()
        escrever(evento["texto"])
        pausa()
        if not evento["opcoes"]:
            return
        for numero, opcao in evento["opcoes"].items():
            print(f'[{numero}] {opcao["texto"]}')
        escolha = input("O que você faz? ")
        while escolha not in evento["opcoes"]:
            escolha = input("Opção inválida, tente de novo: ")
        nome_evento = evento["opcoes"][escolha]["destino"]


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
    rodar_evento("inicio")