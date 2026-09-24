# --- CLASSE BASE ---
class Personagem:
    def __init__(self, nome, vida, ataque, defesa=0):
        self.nome = nome
        self.vida_maxima = vida
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo):
        if not self.esta_vivo():
            print(f"{self.nome} está derrotado e não pode atacar!")
            return
        
        dano = self.ataque
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} agora tem {self.vida}/{self.vida_maxima} de vida.")


# --- CLASSE JOGADOR ---
class Jogador(Personagem):
    def __init__(self, nome, vida, ataque, defesa=0, experiencia=0):
        super().__init__(nome, vida, ataque, defesa)
        self.experiencia = experiencia

    def ganhar_experiencia(self, qtd):
        self.experiencia += qtd
        print(f"{self.nome} ganhou {qtd} pontos de experiência!")


# --- CLASSES TEMÁTICAS ---
class Espadachim(Jogador):
    def __init__(self, nome):
        super().__init__(nome, vida=120, ataque=22, defesa=15)


class Mago(Jogador):
    def __init__(self, nome):
        super().__init__(nome, vida=80, ataque=35, defesa=5)


class Ladino(Jogador):
    def __init__(self, nome):
        super().__init__(nome, vida=95, ataque=25, defesa=10)


# --- CLASSE INIMIGO ---
class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, defesa=0, recompensa_ouro=10):
        super().__init__(nome, vida, ataque, defesa)
        self.recompensa_ouro = recompensa_ouro
        print(f"Cuidado! Um {self.nome} selvagem apareceu!")


# --- EXEMPLO DE USO (RODANDO O JOGO) ---
if __name__ == "__main__":
  
    heroi = Ladino(nome="betinha")
    print("-" * 30)
    goblin = Inimigo(nome="Goblin alfa", vida=40, ataque=10, recompensa_ouro=15)
    print("-" * 30)

    heroi.atacar(goblin)
    print("-" * 30)

    if goblin.esta_vivo():
        goblin.atacar(heroi)
