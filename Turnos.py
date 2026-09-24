import random
import time

def iniciar_batalha_pokemon(jogador, inimigo, inventario_pocoes=2):
    print(f"\n🔥 UM {inimigo.nome} SELVAGEM APARECEU! Fique atento! 🔥\n")
    
    turno = 1
    jogador_defendeu = False
    inimigo_defendeu = False
    
    while jogador.esta_vivo() and inimigo.esta_vivo():
        print(f"==========================================")
        print(f" Turno {turno} | {jogador.nome}: {jogador.vida}/{jogador.vida_maxima} HP | Poções: {inventario_pocoes}")
        print(f" Inimigo: {inimigo.nome} ({inimigo.vida}/{inimigo.vida_maxima} HP)")
        print(f"==========================================")
        
        jogador_defendeu = False
        acao_realizada = False
        
        # --- TURNO DO JOGADOR ---
        while not acao_realizada:
            print("\nO que o Jogador vai fazer?")
            print("[1] Atacar")
            print("[2] Defender (Anula o próximo ataque)")
            print("[3] Usar Poção (Cura vida)")
            print("[4] Fugir")
            
            escolha = input("Escolha sua opção (1-4): ").strip()
            
            if escolha == "1":
                print()
                dano = jogador.ataque
                
                if inimigo_defendeu:
                    print(f"🛡️ {inimigo.nome} usou Defesa e bloqueou totalmente o seu ataque!")
                else:
                    inimigo.vida -= dano
                    if inimigo.vida < 0: inimigo.vida = 0
                    print(f"⚔️ {jogador.nome} atacou e causou {dano} de dano em {inimigo.nome}.")
                acao_realizada = True
                
            elif escolha == "2":
                print(f"\n🛡️ {jogador.nome} adotou uma postura defensiva!")
                jogador_defendeu = True
                acao_realizada = True
                
            elif escolha == "3":
                if inventario_pocoes > 0:
                    cura = 30
                    jogador.vida += cura
                    if jogador.vida > jogador.vida_maxima:
                        jogador.vida = jogador.vida_maxima
                    inventario_pocoes -= 1
                    print(f"\n🧪 {jogador.nome} usou uma Poção e recuperou {cura} de HP! (Poções restantes: {inventario_pocoes})")
                    acao_realizada = True
                else:
                    print("\n❌ Suas poções acabaram! Escolha outra ação.")
                    
            elif escolha == "4":
                print(f"\n🏃 {jogador.nome} conseguiu fugir da batalha com segurança!")
                return "fugiu"
            else:
                print("\n❌ Opção inválida! Escolha um número de 1 a 4.")

        time.sleep(1)
      
        if not inimigo.esta_vivo():
            print(f"\n🎉 Vitória! {inimigo.nome} foi derrotado!")
            return "vitoria"
            
        print()

        print(f"Vez de {inimigo.nome}...")
        time.sleep(1)
        
        acao_inimigo = random.choices(["atacar", "defender"], weights=[70, 30], k=1)[0]
        
        inimigo_defendeu = False
        
        if acao_inimigo == "defender":
            inimigo_defendeu = True
            print(f"🛡️ {inimigo.nome} assumiu uma postura defensiva e está se protegendo!")
        else:
            dano_inimigo = inimigo.ataque
            
         
            if jogador_defendeu:
                print(f"🛡️ {jogador.nome} usou a Defesa perfeitamente e anulou 100% do ataque de {inimigo.nome}!")
            else:
                jogador.vida -= dano_inimigo
                if jogador.vida < 0: jogador.vida = 0
                print(f"💥 {inimigo.nome} atacou e causou {dano_inimigo} de dano em {jogador.nome}.")
        
        print(f"HP atual de {jogador.nome}: {jogador.vida}/{jogador.vida_maxima}\n")
        time.sleep(1)

        if not jogador.esta_vivo():
            print(f"\n💀 {jogador.nome} desmaiou... Fim de jogo!")
            return "derrota"
            
        turno += 1
