# inv-base-v1.02.py
from typing import List, Optional, Dict

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

class Inventario:
    def __init__(self, capacidade: int = 5):
        self.capacidade = capacidade
        self.itens: List[Item] = []
        self.arma_equipada: Optional[Arma] = None

    def adicionar(self, item: Item) -> bool:
        if len(self.itens) >= self.capacidade:
            print(f"❌ Inventário cheio! Não foi possível guardar '{item.nome}'.")
            return False
        self.itens.append(item)
        print(f"✅ Você encontrou: {item.nome}")
        return True

    def remover(self, item: Item) -> bool:
        if item in self.itens:
            if item == self.arma_equipada:
                self.arma_equipada = None
            self.itens.remove(item)
            return True
        return False

    def equipar(self, item: Item) -> bool:
        if not isinstance(item, Arma):
            print(f"❌ Você não pode equipar '{item.nome}'.")
            return False
        
        if item in self.itens:
            self.arma_equipada = item
            print(f"🛡️ Você equipou: {item.nome}!")
            return True
            
        return False

    def usar_consumavel(self, item: Item, personagem: Dict[str, int]) -> bool:
        if not isinstance(item, Consumavel):
            print(f"❌ Você não pode beber ou comer '{item.nome}'.")
            return False
            
        if item in self.itens:
            personagem['vida'] += item.cura
            self.remover(item)
            print(f"💖 Você usou {item.nome} e recuperou {item.cura} de Vida.")
            return True
            
        return False

    # --- NOVIDADE DO STEP 3: INTERFACE VISUAL ---
    def mostrar_inventario(self):
        print("\n" + "="*45)
        print(f"🎒 INVENTÁRIO DO BETINHA [{len(self.itens)}/{self.capacidade}]")
        print("="*45)
        
        # Exibe a arma atual
        if self.arma_equipada:
            print(f"Em mãos: {self.arma_equipada.nome} (+{self.arma_equipada.dano} Dano)")
        else:
            print("Em mãos: Nenhuma arma equipada (Punhos)")
        
        print("-" * 45)
        
        # Lista os itens
        if not self.itens:
            print("   Sua mochila está vazia.")
        else:
            for i, item in enumerate(self.itens):
                tag_equipada = " [Equipada]" if item == self.arma_equipada else ""
                print(f"[{i}] {item}{tag_equipada}")
                
        print("="*45 + "\n")

# ==========================================
# Teste Step 3
# ==========================================
if __name__ == "__main__":
    inv = Inventario(capacidade=4)
    
    # Criando os itens
    faca = Arma("Faca de Cozinha", valor=5, dano=3)
    espada = Arma("Espada Enferrujada", valor=15, dano=8)
    pocao = Consumavel("Poção Pequena", valor=10, cura=25)
    anel = Item("Anel de Prata", valor=50) # Apenas um item de venda
    
    # Adicionando na mochila
    inv.adicionar(faca)
    inv.adicionar(espada)
    inv.adicionar(pocao)
    inv.adicionar(anel)
    
    # Ações
    inv.equipar(espada)
    
    # Mostra a tela bonita do inventário
    inv.mostrar_inventario()
    
    # Simula usar um item e mostra de novo
    personagem_mock = {'vida': 20}
    inv.usar_consumavel(pocao, personagem_mock)
    
    # Vendo como ficou após usar a poção
    inv.mostrar_inventario()
