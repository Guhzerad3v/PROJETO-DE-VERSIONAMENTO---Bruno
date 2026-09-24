# main.py
import sys
import time
# Importando o inventário (Lembre-se de renomear o arquivo para inv_base.py)
from inv_base import Inventario, Personagem, Arma, Consumavel 

# No futuro, importaremos os outros módulos assim:
# from narrativa import iniciar_historia, exibir_dialogo
# from Turnos import iniciar_batalha

def efeito_digitar(texto, atraso=0.03):
    """Cria um efeito visual de RPG ao imprimir textos."""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

def exibir_menu_principal():
    print("\n" + "="*50)
    print("🐉  A LENDA DO BETINHA - MENU PRINCIPAL  🐉")
    print("="*50)
    print("[1] 📜 Iniciar História")
    print("[2] 🎒 Abrir Mochila")
    print("[3] ⚔️ Ir para a Batalha (Simulação)")
    print("[4] ❌ Sair do Jogo")
    print("="*50)

def main():
    # 1. Instanciando os módulos principais
    mochila_betinha = Inventario(capacidade=5)
    betinha = Personagem("Betinha", vida_maxima=100)
    
    # Dando uns itens iniciais para teste
    mochila_betinha.adicionar(Arma("Espada Longa", valor=20, dano=12))
    mochila_betinha.adicionar(Consumavel("Poção de Cura", valor=10, cura=40))

    efeito_digitar("Bem-vindo ao mundo de Betinha! Prepare-se para a jornada...")
    time.sleep(1)

    # 2. Loop Principal de Gameplay
    while True:
        exibir_menu_principal()
        escolha = input("\nO que você deseja fazer? (1-4): ")

        if escolha == '1':
            # ISSUE 3 - Narrativa
            print("\n[Módulo de História ainda será conectado]")
            efeito_digitar("Um velho sábio se aproxima: 'Você precisa salvar o reino, Betinha!'")
            
        elif escolha == '2':
            # ISSUE 1 - Inventário (Já funcionando!)
            print("\nAbrindo a mochila...")
            mochila_betinha.mostrar_inventario()
            
            # Sub-menu rápido para testar o uso de itens
            acao = input("Digite o número do item para equipar/usar ou pressione ENTER para voltar: ")
            if acao.isdigit():
                try:
                    item = mochila_betinha._obter_item_por_indice(int(acao))
                    if isinstance(item, Arma):
                        mochila_betinha.equipar(int(acao))
                    else:
                        mochila_betinha.usar_consumavel(int(acao), betinha)
                except Exception as e:
                    print(f"⚠️ {e}")
                    
        elif escolha == '3':
            # ISSUE 2 - Sistema de Luta
            print("\n[Módulo de Batalha ainda será conectado]")
            arma_nome = mochila_betinha.arma_equipada.nome if mochila_betinha.arma_equipada else "Punhos"
            efeito_digitar(f"Um goblin aparece! Betinha se prepara para lutar usando: {arma_nome}!")
            
        elif escolha == '4':
            efeito_digitar("Salvando o jogo... Obrigado por jogar A Lenda do Betinha!")
            break
            
        else:
            print("❌ Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()