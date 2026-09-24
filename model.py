import sys
import time

# IMPORTAÇÕES - ISSUE 1 (Inventário já funcional)
from inv_base import Inventario, Personagem, Arma, Consumavel

# IMPORTAÇÕES FUTURAS - Preparadas com base na tua estrutura de ficheiros
# from entidades import Jogador, Inimigo
# from atributos import AtributosBase
# import armas
# import Habilidades
# import narrativa
# import turnos

def efeito_digitar(texto: str, atraso: float = 0.03):
    """Cria um efeito visual de RPG ao imprimir textos no ecrã."""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

def exibir_menu_principal():
    """Apresenta as opções principais do jogo."""
    print("\n" + "="*50)
    print("🐉  A LENDA DO BETINHA - MENU PRINCIPAL  🐉")
    print("="*50)
    print("[1] 📜 Iniciar História (narrativa.py)")
    print("[2] 🎒 Abrir Mochila (inv_base.py)")
    print("[3] ⚔️ Ir para a Batalha (turnos.py)")
    print("[4] ❌ Sair do Jogo")
    print("="*50)

def main():
    # 1. Instanciar os módulos principais (Estado do Jogo)
    mochila_betinha = Inventario(capacidade=5)
    betinha = Personagem("Betinha", vida_maxima=100)
    
    # Adicionar itens iniciais para testes
    mochila_betinha.adicionar(Arma("Espada Longa", valor=20, dano=12))
    mochila_betinha.adicionar(Consumavel("Poção de Cura", valor=10, cura=40))

    efeito_digitar("Bem-vindo ao mundo de Betinha! Prepara-te para a jornada...")
    time.sleep(1)

    # 2. Loop Principal de Gameplay
    while True:
        exibir_menu_principal()
        escolha = input("\nO que desejas fazer? (1-4): ")

        if escolha == '1':
            # Ligação com narrativa.py
            print("\n[Módulo de História a ser implementado]")
            efeito_digitar("Um velho sábio aproxima-se: 'Precisas de salvar o reino, Betinha!'")
            
        elif escolha == '2':
            # Ligação com inv_base.py
            print("\nA abrir a mochila...")
            mochila_betinha.mostrar_inventario()
            
            acao = input("Digita o número do item para equipar/usar ou prime ENTER para voltar: ")
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
            # Ligação com turnos.py, Habilidades.py e entidades.py
            print("\n[Módulo de Batalha a ser implementado]")
            arma_nome = mochila_betinha.arma_equipada.nome if mochila_betinha.arma_equipada else "Punhos"
            efeito_digitar(f"Um goblin aparece! Betinha prepara-se para lutar a usar: {arma_nome}!")
            
        elif escolha == '4':
            efeito_digitar("A guardar o progresso... Obrigado por jogares A Lenda do Betinha!")
            break
            
        else:
            print("❌ Escolha inválida. Tenta novamente.")

if __name__ == "__main__":
    main()
