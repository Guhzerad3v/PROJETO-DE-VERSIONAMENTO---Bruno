import random
import time


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


class Jogador(Personagem):
    def __init__(self, nome, vida, mana, ataque, defesa=0):
        super().__init__(nome, vida, mana, ataque, defesa)


class Mago(Jogador):
    def __init__(self, nome):
        super().__init__(nome, vida=80, mana=60, ataque=20, defesa=5)
        print(f"[{self.nome}] entrou na batalha como Mago (60 MP)!")


class Espadachim(Jogador):
    def __init__(self, nome):
        super().__init__(nome, vida=120, mana=30, ataque=25, defesa=15)
        print(f"[{self.nome}] entrou na batalha como Espadachim (30 MP)!")


class Ladino(Jogador):
    def __init__(self, nome):
        super().__init__(nome, vida=95, mana=30, ataque=22, defesa=20)
        print(f"[{self.nome}] entrou na batalha como Ladino (30 MP)!")

class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, defesa=0):
        super().__init__(nome, vida, mana=0, ataque=ataque, defesa=defesa)
        print(f"Cuidado! Um {self.nome} selvagem apareceu!")


# --- LOOP DE BATALHA COM HABILIDADES PERSONALIZADAS ---
def iniciar_batalha_classes(jogador, inimigo, inventario_pocoes=2):
    print(f"\n🔥 INÍCIO DO COMBATE: {jogador.nome} vs {inimigo.nome} 🔥\n")
    
    turno = 1
    jogador_defendeu = False
    inimigo_defendeu = False
    efeito_veneno_ativo = False
    
    while jogador.esta_vivo() and inimigo.esta_vivo():
        print(f"==================================================")
        print(f" Turno {turno} | {jogador.nome} ({type(jogador).__name__})")
        print(f" HP: {jogador.vida}/{jogador.vida_maxima} | MP: {jogador.mana}/{jogador.mana_maxima}")
        print(f" Poções: {inventario_pocoes} | Inimigo: {inimigo.nome} ({inimigo.vida}/{inimigo.vida_maxima} HP)")
        print(f"==================================================")
        
       
        if efeito_veneno_ativo and inimigo.esta_vivo():
            dano_veneno = 8
            inimigo.vida -= dano_veneno
            if inimigo.vida < 0: inimigo.vida = 0
            print(f"🧪 O veneno corrói {inimigo.nome}, causando {dano_veneno} de dano contínuo!")
            if not inimigo.esta_vivo():
                break

        jogador_defendeu = False
        acao_realizada = False
        
     
        while not acao_realizada:
            print("\nEscolha sua ação:")
            print(f"[1] Ataque Físico/Melee (Básico) - Dano: ~{jogador.ataque} | Custo: 0 MP")
            
            if isinstance(jogador, Mago):
                print("[2] Bola de Fogo       - Dano: 35 | Custo: 6 MP")
                print("[3] Barreira de Mana   - Absorve dano | Custo: 4 MP")
                print("[4] Tempestade de Raios - Dano: 55 | Custo: 10 MP")
            
            elif isinstance(jogador, Espadachim):
                print("[2] Corte Cruzado      - Dano: 30 | Custo: 4 MP")
                print("[3] Postura Retaliação - Bloqueia e contra-ataca | Custo: 5 MP")
                print("[4] Golpe Despedaçador - Dano: 45 (Reduz Defesa) | Custo: 7 MP")
            
            elif isinstance(jogador, Ladino):
                print("[2] Apunhalada Sombria - Dano Crítico: 40 | Custo: 4 MP")
                print("[3] Lâmina Envenenada  - Dano: 25 + Veneno | Custo: 6 MP")
                print("[4] Passos de Sombra   - Esquiva total | Custo: 5 MP")

            print("[5] Defender (Reduz dano recebido)")
            print("[6] Usar Poção (Cura vida)")
            print("[7] Fugir")
            
            escolha = input("Digite o número da sua escolha (1-7): ").strip()
            
            if escolha == "1":
                dano = jogador.ataque
                print(f"\n⚔️ {jogador.nome} desferiu um ataque corpo a corpo!")
                if inimigo_defendeu:
                    print(f"🛡️ {inimigo.nome} usou Defesa e bloqueou o ataque!")
                else:
                    inimigo.vida -= dano
                    if inimigo.vida < 0: inimigo.vida = 0
                    print(f"💥 Causou {dano} de dano em {inimigo.nome}.")
                acao_realizada = True

      
            elif escolha == "2":
                if isinstance(jogador, Mago): 
                    custo, dano = 6, 35
                    if jogador.mana >= custo:
                        jogador.mana -= custo
                        print(f"\n🔥 {jogador.nome} lançou Bola de Fogo!")
                        inimigo.vida -= dano
                        acao_realizada = True
                    else: print(f"\n❌ Mana insuficiente ({jogador.mana}/{custo} MP).")
                
                elif isinstance(jogador, Espadachim): 
                    custo, dano = 4, 30
                    if jogador.mana >= custo:
                        jogador.mana -= custo
                        print(f"\n⚔️ {jogador.nome} executou um Corte Cruzado rápido!")
                        inimigo.vida -= dano
                        acao_realizada = True
                    else: print(f"\n❌ Mana insuficiente!")
                
                elif isinstance(jogador, Ladino):
                    custo, dano = 4, 40
                    if jogador.mana >= custo:
                        jogador.mana -= custo
                        print(f"\n🗡️ {jogador.nome} desferiu uma Apunhalada Sombria crítica pelas costas!")
                        inimigo.vida -= dano
                        acao_realizada = True
                    else: print(f"\n❌ Mana insuficiente!")

           
            elif escolha == "3":
                if isinstance(jogador, Mago): 
                    custo = 4
                    if jogador.mana >= custo:
                        jogador.mana -= custo
                        print(f"\n✨ {jogador.nome} ergueu uma Barreira de Mana protetora!")
                        jogador_defendeu = True 
                        acao_realizada = True
                    else: print(f"\n❌ Mana insuficiente!")
                
                elif isinstance(jogador, Espadachim): 
                    custo = 5
                    if jogador.mana >= custo:
                        jogador.mana -= custo
                        print(f"\n🛡️ {jogador.nome} entrou em Postura de Retaliação!")
                        jogador_defendeu = True
                        acao_realizada = True
                    else: print(f"\n❌ Mana insuficiente!")
                
                elif isinstance(jogador, Ladino): 
                    custo, dano = 6, 25
                    if jogador.mana >= custo:
                        jogador.mana -= custo
                        efeito_veneno_ativo = True
                        print(f"\n🧪 {jogador.nome} envenenou a lâmina! O inimigo começará a sofrer dano por turnos.")
                        inimigo.vida -= dano
                        acao_realizada = True
                    else: print(f"\n❌ Mana insuficiente!")

         
            elif escolha == "4":
                if isinstance(jogador, Mago): 
                    custo, dano = 10, 55
                    if jogador.mana >= custo:
                        jogador.mana -= custo
                        print(f"\n⚡ {jogador.nome} invocou uma Tempestade de Raios devastadora!")
                        inimigo.vida -= dano
                        acao_realizada = True
                    else: print(f"\n❌ Mana insuficiente!")
                
                elif isinstance(jogador, Espadachim): 
                    custo, dano = 7, 45
                    if jogador.mana >= custo:
                        jogador.mana -= custo
                        print(f"\n⚒️ {jogador.nome} desferiu um Golpe Despedaçador que esmagou a armadura!")
                        inimigo.defesa = max(0, inimigo.defesa - 5) 
                        inimigo.vida -= dano
                        acao_realizada = True
                    else: print(f"\n❌ Mana insuficiente!")
                
                elif isinstance(jogador, Ladino): 
                    custo = 5
                    if jogador.mana >= custo:
                        jogador.mana -= custo
                        print(f"\n👤 {jogador.nome} dissolveu-se nas sombras, esquivando-se de tudo neste turno!")
                        jogador_defendeu = True
                        acao_realizada = True
                    else: print(f"\n❌ Mana insuficiente!")

            elif escolha == "5":
                print(f"\n🛡️ {jogador.nome} adotou uma postura defensiva.")
                jogador_defendeu = True
                acao_realizada = True
                
            elif escolha == "6":
                if inventario_pocoes > 0:
                    cura = 40
                    jogador.vida = min(jogador.vida_maxima, jogador.vida + cura)
                    inventario_pocoes -= 1
                    print(f"\n🧪 Poção usada! Recuperou {cura} de HP (Restam: {inventario_pocoes}).")
                    acao_realizada = True
                else: print("\n❌ Suas poções acabaram!")
                    
            elif escolha == "7":
                print(f"\n🏃 {jogador.nome} fugiu da batalha com sucesso!")
                return "fugiu"
            else:
                print("\n❌ Opção inválida! Escolha entre 1 e 7.")

        time.sleep(1)

     
        if inimigo.vida < 0: inimigo.vida = 0

        if not inimigo.esta_vivo():
            print(f"\n🎉 Vitória! {inimigo.nome} foi derrotado!")
            return "vitoria"
            
        print()

        # --- TURNO DO INIMIGO ---
        print(f"Vez de {inimigo.nome}...")
        time.sleep(1)
        
        acao_inimigo = random.choices(["atacar", "defender"], weights=[75, 25], k=1)[0]
        inimigo_defendeu = False
        
        if acao_inimigo == "defender":
            inimigo_defendeu = True
            print(f"🛡️ {inimigo.nome} assumiu uma postura defensiva.")
        else:
            dano_inimigo = max(0, inimigo.ataque - jogador.defesa)
            if jogador_defendeu:
                print(f"🛡️ {jogador.nome} defendeu perfeitamente e anulou o dano do inimigo!")
            else:
                jogador.vida -= dano_inimigo
                print(f"💥 {inimigo.nome} atacou e causou {dano_inimigo} de dano em {jogador.nome}.")
        
        if jogador.vida < 0: jogador.vida = 0
        print(f"HP atual de {jogador.nome}: {jogador.vida}/{jogador.vida_maxima}\n")
        time.sleep(1)

        if not jogador.esta_vivo():
            print(f"\n💀 {jogador.nome} desmaiou... Fim de jogo!")
            return "derrota"
            
        turno += 1
