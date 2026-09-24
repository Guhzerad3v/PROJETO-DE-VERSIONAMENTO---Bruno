# inv-base-v1.03.py (Step 4 - Versão Final ISSUE 1)
from typing import List, Optional

# ==========================================
# 1. TRATAMENTO DE EXCEÇÕES CUSTOMIZADAS
# ==========================================
class ErroInventario(Exception): 
    """Classe base para erros do inventário."""
    pass

class IndiceInvalidoError(ErroInventario): 
    pass

class AcaoInvalidaError(ErroInventario): 
    pass

# ==========================================
# 2. CLASSES DE ITENS (Herdadas do Step 3)
# ==========================================
class Item:
    def __init__(self, nome: str, valor: int):
        self.nome = nome
        self.valor = valor
        
    def __str__(self) -> str:
        return f"{self.nome} (Valor: {self.valor})"

class Arma(Item):
    def __init__(self, nome: str, valor: int, dano: int):
        super().__init__(nome, valor)
        self.dano = dano
        
    def __str__(self) -> str:
        return f"⚔️ {self.nome} | Dano: +{self.dano} | Valor: {self.valor}"

class Consumavel(Item):
    def __init__(self, nome: str, valor: int, cura: int):
        super().__init__(nome, valor)
        self.cura = cura
        
    def __str__(self) -> str:
        return f"🧪 {self.nome} | Cura: +{self.cura} HP | Valor: {self.valor}"

# ==========================================
# 3. ENTIDADES (Ponte para a ISSUE 2)
# ==========================================
class Personagem:
    def __init__(self, nome: str, vida_maxima: int):
        self.nome = nome
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima

# ==========================================
# 4. GERENCIADOR DO INVENTÁRIO
# ==========================================
class Inventario:
    def __init__(self, capacidade: int = 5):
        self.capacidade = capacidade
        self.itens: List[Item] = []
        self.arma_equipada: Optional[Arma] = None

    def adicionar(self, item: Item) -> bool:
        if len(self.itens) >= self.capacidade:
            print(f"❌ A mochila está cheia! Deixe algo para pegar '{item.nome}'.")
            return False
        self.itens.append(item)
        print(f"✅ Você encontrou: {item.nome}")
        return True

    def _obter_item_por_indice(self, indice: int) -> Item:
        """Função interna para buscar um item de forma segura."""
        if 0 <= indice < len(self.itens):
            return self.itens[indice]
        raise IndiceInvalidoError(f"O espaço {indice} da mochila está vazio ou não existe.")

    def equipar(self, indice: int):
        """Agora o jogador equipa usando o número (índice) do item."""
        try:
            item = self._obter_item_por_indice(indice)
            if not isinstance(item, Arma):
                raise AcaoInvalidaError(f"Você não pode equipar '{item.nome}'.")
            
            self.arma_equipada = item
            print(f"🛡️ Você equipou: {item.nome}!")
            
        except ErroInventario as e:
            print(f"⚠️ Aviso: {e}")

    def usar_consumavel(self, indice: int, alvo: Personagem):
        """O jogador usa o item pelo número (índice)."""
        try:
            item = self._obter_item_por_indice(indice)
            if not isinstance(item, Consumavel):
                raise AcaoInvalidaError(f"Você não pode consumir '{item.nome}'.")
            
            # Aplica a cura sem passar da vida máxima
            alvo.vida_atual = min(alvo.vida_maxima, alvo.vida_atual + item.cura)
            self.itens.remove(item)
            
            print(f"💖 {alvo.nome} usou {item.nome} e curou {item.cura} HP!")
            print(f"   [Vida Atual: {alvo.vida_atual}/{alvo.vida_maxima}]")
            
        except ErroInventario as e:
            print(f"⚠️ Aviso: {e}")

    def mostrar_inventario(self):
        print("\n" + "="*50)
        print(f"🎒 INVENTÁRIO [{len(self.itens)}/{self.capacidade}]")
        print("="*50)
        
        if self.arma_equipada:
            print(f"Em mãos: {self.arma_equipada.nome} (+{self.arma_equipada.dano} Dano)")
        else:
            print("Em mãos: Nenhuma arma equipada (Punhos)")
        
        print("-" * 50)
        
        if not self.itens:
            print("   Sua mochila está vazia.")
        else:
            for i, item in enumerate(self.itens):
                tag_equipada = " [Equipada]" if item == self.arma_equipada else ""
                print(f"[{i}] {item}{tag_equipada}")
                
        print("="*50 + "\n")


# ==========================================
# Teste Final do Dia 4 (Simulando o Jogo)
# ==========================================
if __name__ == "__main__":
    # 1. Configurando o cenário
    inv = Inventario(capacidade=4)
    betinha = Personagem("Betinha", vida_maxima=100)
    betinha.vida_atual = 40 # Betinha apanhou em uma batalha
    
    # Adicionando itens na mochila
    inv.adicionar(Arma("Espada Longa", valor=20, dano=12))
    inv.adicionar(Consumavel("Poção Média", valor=15, cura=50))
    inv.adicionar(Item("Chave Enferrujada", valor=0)) # Item de Quest
    
    # 2. Mostrando a mochila para o jogador ver os índices
    inv.mostrar_inventario()
    
    # 3. Simulando a escolha do jogador pelo terminal (MAIN fará isso via input)
    print(">> O jogador digitou '0' para equipar a Espada:")
    inv.equipar(0)
    
    print("\n>> O jogador digitou '1' para beber a Poção:")
    inv.usar_consumavel(1, betinha)
    
    print("\n>> O jogador digitou '2' para tentar equipar a chave (Vai dar erro tratado):")
    inv.equipar(2)
    
    print("\n>> O jogador digitou '9' (Não existe na mochila):")
    inv.usar_consumavel(9, betinha)
    
    # Mostrando a mochila finalizada
    inv.mostrar_inventario()
