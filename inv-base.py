# inv-base-v1.01.py
from typing import List, Optional, Dict

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
        self.itens: List[Item] = []
        self.arma_equipada: Optional[Arma] = None

    def adicionar(self, item: Item) -> bool:
        if len(self.itens) >= self.capacidade:
            print(f"[Erro] Inventário cheio! Não foi possível adicionar {item.nome}.")
            return False
        self.itens.append(item)
        print(f"[OK] {item.nome} adicionado.")
        return True

    def remover(self, item: Item) -> bool:
        if item in self.itens:
            if item == self.arma_equipada:
                self.arma_equipada = None # Desequipa se a arma for removida
            self.itens.remove(item)
            return True
        return False

    def equipar(self, item: Item) -> bool:
        if not isinstance(item, Arma):
            print(f"[Erro] {item.nome} não é uma arma equipável!")
            return False
        
        if item in self.itens:
            self.arma_equipada = item
            print(f"[OK] {item.nome} equipada com sucesso!")
            return True
            
        print("[Erro] Item não está no inventário.")
        return False

    def usar_consumavel(self, item: Item, personagem: Dict[str, int]) -> bool:
        if not isinstance(item, Consumavel):
            print(f"[Erro] {item.nome} não é um item consumível!")
            return False
            
        if item in self.itens:
            personagem['vida'] += item.cura
            self.remover(item)
            print(f"[OK] {item.nome} consumido! Vida recuperada: {item.cura}.")
            return True
            
        return False

if __name__ == "__main__":
    inv = Inventario(capacidade=2)
    espada = Arma("Espada de Ferro", 50, 15)
    pocao = Consumavel("Poção Maior", 20, 50)
    escudo = Item("Escudo Quebrado", 5) # Item comum, não é arma nem consumível
    
    # Testando capacidade limite
    inv.adicionar(espada)
    inv.adicionar(pocao)
    inv.adicionar(escudo) # Deve falhar (limite 2)
    
    # Testando validações de tipo
    inv.equipar(pocao) # Deve falhar (poção não é arma)
    inv.equipar(espada) # Deve funcionar
    
    personagem_mock = {'vida': 10}
    inv.usar_consumavel(espada, personagem_mock) # Deve falhar (espada não é de beber)
    inv.usar_consumavel(pocao, personagem_mock) # Deve funcionar
