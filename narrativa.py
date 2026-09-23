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


if __name__ == "__main__":
    # teste rápido: só roda se você executar este arquivo direto
    escrever("Em um reino distante, uma sombra crescia...")
    pausa()
    dialogo("Velho Sábio", "Você finalmente chegou, jovem aventureiro.")
    dialogo("Betinha", "Quem é você? O que você quer de mim?")
    classe = escolher_classe()
    escrever(f'Você escolheu: {classe["nome"]}')