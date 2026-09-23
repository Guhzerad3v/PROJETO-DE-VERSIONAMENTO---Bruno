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
        
        dano_causado = self.ataque
        alvo.receber_dano(dano_causado)
        print(f"{self.nome} atacou {alvo.nome} causando {dano_causado} de dano bruto.")

    def receber_dano(self, dano_bruto):
       
        porcentagem_reducao = self.defesa / 100.0
        dano_final = int(dano_bruto * (1 - porcentagem_reducao))
        
      
        if dano_final < 0:
            dano_final = 0

        self.vida -= dano_final
        if self.vida < 0:
            self.vida = 0
            
        print(f"{self.nome} defendeu parte do golpe! Recebeu {dano_final} de dano (Defesa: {self.defesa}).")
        print(f"Vida atual de {self.nome}: {self.vida}/{self.vida_maxima}")



class Jogador(Personagem):
    def __init__(self, nome, vida, ataque, defesa=0, experiencia=0):
        super().__init__(nome, vida, ataque, defesa)
        self.experiencia = experiencia

    def ganhar_experiencia(self, qtd):
        self.experiencia += qtd
        print(f"{self.nome} ganhou {qtd} pontos de experiência!")


class Espadachim(Jogador):
    def __init__(self, nome):
       
        super().__init__(nome, vida=120, ataque=22, defesa=15)
        print(f"[{self.nome}] entrou na batalha como um poderoso Espadachim!")


class Mago(Jogador):
    def __init__(self, nome):
        
        super().__init__(nome, vida=80, ataque=35, defesa=5)
        print(f"[{self.nome}] entrou na batalha como um sábio Mago!")


class Ladino(Jogador):
    def __init__(self, nome):
       
        super().__init__(nome, vida=95, ataque=25, defesa=20)
        print(f"[{self.nome}] entrou na batalha como um furtivo Ladino!")



class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, defesa=0, recompensa_ouro=10):
        super().__init__(nome, vida, ataque, defesa)
        self.recompensa_ouro = recompensa_ouro
        print(f"Cuidado! Um {self.nome} selvagem apareceu!")



if __name__ == "__main__":
    print("--- CRIAÇÃO DE PERSONAGENS ---")
    heroi = Ladino("Betinha")
    print("-" * 40)
    monstro = Inimigo("Orc Alfa", vida=60, ataque=30, defesa=10, recompensa_ouro=20)
    print("-" * 40)

    print("--- TURNO 1 ---")
   
    heroi.atacar(monstro)
    print("-" * 40)

    print("--- TURNO 2 ---")

    monstro.atacar(heroi)
