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


if __name__ == "__main__":
    # teste rápido: só roda se você executar este arquivo direto
    escrever("Em um reino distante, uma sombra crescia...")
    pausa()
    dialogo("Velho Sábio", "Você finalmente chegou, jovem aventureiro.")
    dialogo("Betinha", "Quem é você? O que você quer de mim?")