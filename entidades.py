# --- CLASSE BASE DE ENTIDADES ---
class Personagem:
    def __init__(self, nome, vida, mana, ataque, defesa=0):
        self.nome = nome
        self.vida_maxima = vida
        self.vida = vida
        self.mana_maxima = mana
        self.mana = mana
        self.ataque = ataque
        self.defesa = defesa

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo):
        if not self.esta_vivo():
            return
        dano_causado = self.ataque
        alvo.receber_dano(dano_causado)

    def receber_dano(self, dano_bruto):
        dano_final = dano_bruto - self.defesa
        if dano_final < 0:
            dano_final = 0
        self.vida -= dano_final
        if self.vida < 0:
            self.vida = 0


# --- CLASSE JOGADOR ---
class Jogador(Personagem):
    def __init__(self, nome, vida, mana, ataque, defesa=0):
        super().__init__(nome, vida, mana, ataque, defesa)


# --- CLASSE INIMIGO ---
class Inimigo(Personagem):
    def __init__(self, nome, vida, mana, ataque, defesa=0):
        super().__init__(nome, vida, mana, ataque, defesa)
