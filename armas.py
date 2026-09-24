import random
import time

# ==========================================
# 1. CLASSES DE ITENS E INVENTÁRIO (ISSUE 1)
# ==========================================
class Item:
    def __init__(self, nome: str, valor: int):
        self.nome = nome
        self.valor = valor

class Arma(Item):
    def __init__(self, nome: str, valor: int, dano: int):
        super().__init__(nome, valor)
        self.dano = dano

class Consumavel(Item):
    def __init__(self, nome: str, valor: int, cura: int):
        super().__init__(nome, valor)
        self.cura = cura

class Inventario:
    def __init__(self, capacidade: int = 5):
        self.capacidade = capacidade
        self.itens = []
        self.arma_equipada = None  # Guarda a arma que está a ser usada

    def adicionar(self, item):
        if len(self.itens) >= self.capacidade:
            return False
        self.itens.append(item)
        return True


# ==========================================
# 2. CLASSES BASE DE PERSONAGENS (ISSUE 2)
# ==========================================
class Personagem:
    def __init__(self, nome, vida, mana, ataque, defesa=0):
        self.nome = nome
        self.vida_maxima = vida
        self.vida = vida
        self.vida_atual = vida  # Compatibilidade com a Issue 1
        self.mana_maxima = mana
        self.mana = mana
        self.ataque = ataque
        self.defesa = defesa
        self.inventario = Inventario()  # Cada personagem tem a sua mochila da Issue 1

    def esta_vivo(self):
        return self.vida > 0


class Jogador(Personagem):
    def __init__(self, nome, vida, mana, ataque, defesa=0):
        super().__init__(nome, vida, mana, ataque, defesa)


class Mago(Jogador):
    def __init__(self, nome):
        super().__init__(nome, vida=80, mana=60, ataque=15, defesa=5)
        print(f"[{self.nome}] entrou na batalha como Mago (60 MP)!")


class Espadachim(Jogador):
    def __init__(self, nome):
        super().__init__(nome, vida=120, mana=30, ataque=20, defesa=15)
        print(f"[{self.nome}] entrou na batalha como Espadachim (30 MP)!")


class Ladino(Jogador):
    def __init__(self, nome):
        super().__init__(nome, vida=95, mana=30, ataque=18, defesa=20)
        print(f"[{self.nome}] entrou na batalha como Ladino (30 MP)!")


class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, defesa=0):
        super().__init__(nome, vida, mana=0, ataque=ataque, defesa=defesa)
        print(f"Cuidado! Um {self.nome} selvagem apareceu!")


# ==========================================
# 3. LOOP DE BATALHA INTEGRADO (COM DANO DA ARMA)
# ==========================================
def iniciar_batalha_integrada(jogador, inimigo):
    print(f"\n🔥 INÍCIO DO COMBATE: {jogador.nome} vs {inimigo.nome} 🔥\n")
    
    # Exemplo: Vamos dar uma espada inicial ao jogador para testar a integração
    espada_iniciante and jogador.inventario.adicionar(Arma("Espada Longa", 15, 12))
    jogador.inventario.arma_equipada = jogador.inventario.itens[0] # Equipa automaticamente a espada
    
    turno = 1
    jogador_defendeu = False
    inimigo_defendeu = False
    
    while jogador.esta_vivo() and inimigo.esta_vivo():
        print(f"==================================================")
        print(f" Turno {turno} | {jogador.nome}")
        print(f" HP: {jogador.vida}/{jogador.vida_maxima} | MP: {jogador.mana}/{jogador.mana_maxima}")
        
        # Mostra a arma equipada atual (Integração Issue 1)
        if jogador.inventario.arma_equipada:
            arma_atual = jogador.inventario.arma_equipada
            print(f" Arma Equipada: {arma_atual.nome} (+{arma_atual.dano} Dano)")
        else:
            print(f" Arma Equipada: Nenhuma (Apenas Punhos)")
            
        print(f" Inimigo: {inimigo.nome} ({inimigo.vida}/{inimigo.vida_maxima} HP)")
        print(f"==================================================")
        
        jogador_defendeu = False
        acao_realizada = False
        
        while not acao_realizada:
            print("\nEscolha sua ação:")
            
            # Calcula o dano total da arma + ataque base para mostrar no menu
            dano_arma = jogador.inventario.arma_equipada.dano if jogador.inventario.arma_equipada else 0
            dano_fisico_total = jogador.ataque + dano_arma
            
            print(f"[1] Ataque Físico/Melee  - Dano: ~{dano_fisico_total} | Custo: 0 MP")
            print("[2] Habilidade Mágica 1   - Dano: 35 | Custo: 6 MP")
            print("[3] Defender")
            print("[4] Fugir")
            
            escolha = input("Digite o número da sua escolha (1-4): ").strip()
            
            # OPÇÃO 1: ATAQUE FÍSICO INTEGRADO COM A ARMA DA ISSUE 1
            if escolha == "1":
                # Pega o dano da arma equipada no inventário da Issue 1 (se houver)
                dano_extra_arma = jogador.inventario.arma_equipada.dano if jogador.inventario.arma_equipada else 0
                dano_total = jogador.ataque + dano_extra_arma
                
                nome_arma_str = f" com a sua {jogador.inventario.arma_equipada.nome}" if jogador.inventario.arma_equipada else " desarmado (com os punhos)"
                
                print(f"\n⚔️ {jogador.nome} atacou{nome_arma_str}!")
                
                if inimigo_defendeu:
                    print(f"🛡️ {inimigo.nome} usou Defesa e bloqueou o ataque físico!")
                else:
                    inimigo.vida -= dano_total
                    if inimigo.vida < 0: inimigo.vida = 0
                    print(f"💥 Causou {dano_total} de dano total em {inimigo.nome} (Base: {jogador.ataque} + Arma: {dano_extra_arma}).")
                acao_realizada = True
                
            elif escolha == "2":
                custo, dano_magia = 6, 35
                if jogador.mana >= custo:
                    jogador.mana -= custo
                    print(f"\n🔥 {jogador.nome} lançou uma magia!")
                    inimigo.vida -= dano_magia
                    if inimigo.vida < 0: inimigo.vida = 0
                    print(f"💥 Causou {dano_magia} de dano mágico!")
                    acao_realizada = True
                else:
                    print(f"\n❌ Mana insuficiente!")
                    
            elif escolha == "3":
                print(f"\n🛡️ {jogador.nome} adotou uma postura defensiva.")
                jogador_defendeu = True
                acao_realizada = True
                
            elif escolha == "4":
                print(f"\n🏃 {jogador.nome} fugiu da batalha!")
                return "fugiu"
            else:
                print("\n❌ Opção inválida.")

        time.sleep(1)

        if not inimigo.esta_vivo():
            print(f"\n🎉 Vitória! {inimigo.nome} foi derrotado!")
            return "vitoria"
            
        print()

        # Turno do Inimigo
        dano_inimigo = max(0, inimigo.ataque - jogador.defesa)
        if jogador_defendeu:
            print(f"🛡️ {jogador.nome} bloqueou o ataque do inimigo!")
        else:
            jogador.vida -= dano_inimigo
            print(f"💥 {inimigo.nome} atacou e causou {dano_inimigo} de dano.")
            
        if jogador.vida < 0: jogador.vida = 0
        if not jogador.esta_vivo():
            print(f"\n💀 {jogador.nome} foi derrotado...")
            return "derrota"
            
        turno += 1
