# inv-base.py

class Item:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class Arma(Item):
    def __init__(self, nome, valor, dano):
        super().__init__(nome, valor)
        self.dano = dano

class Consumavel(Item):
    def __init__(self, nome, valor, cura):
        super().__init__(nome, valor)
        self.cura = cura

class Inventario:
    def __init__(self):
        self.itens = []
        self.arma_equipada = None

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self, item):
        self.itens.remove(item)

    def equipar(self, arma):
        self.arma_equipada = arma

    def usar_consumavel(self, consumavel, personagem):
        personagem['vida'] += consumavel.cura
        self.remover(consumavel)

# ==========================================
# Teste básico do Dia 1 (Rodando o arquivo)
# ==========================================
if __name__ == "__main__":
    # 1. Cria o inventário
    inv = Inventario()
    
    # 2. Cria os itens
    espada = Arma("Espada de Madeira", 10, 5)
    pocao = Consumavel("Poção de Vida", 5, 20)
    
    # 3. Adiciona os itens na mochila
    inv.adicionar(espada)
    inv.adicionar(pocao)
    
    # 4. Equipa a arma
    inv.equipar(espada)
    
    # 5. Cria um boneco de testes (Mock) e usa a poção
    personagem_mock = {'vida': 50}
    print(f"Vida antes da poção: {personagem_mock['vida']}")
    
    inv.usar_consumavel(pocao, personagem_mock)
    
    # 6. Exibe os resultados
    print(f"Vida depois da poção: {personagem_mock['vida']}")
    print(f"Arma equipada no momento: {inv.arma_equipada.nome}")