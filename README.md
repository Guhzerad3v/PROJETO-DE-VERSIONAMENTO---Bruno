# A Lenda do Betinha (RPG de Texto)

Um jogo de RPG em formato de texto desenvolvido inteiramente em **Python**. O projeto tem como foco uma arquitetura modular e versionamento, onde os sistemas de inventário, combate e narrativa funcionam de forma independente e se conectam na interface principal. A Princípio a ideia de utilizar a separação modular é incentivar a cada usuário lidar com suas próprias branches e objetivos próprios.

##  Tecnologias
- Python 3.1

##  Estrutura do Projeto

O desenvolvimento foi dividido em 3 Grandes **Issues** (Pilares), além do arquivo MAIN que orquestra tudo. Cada Issue é desenvolvida em *Steps* graduais (um commit por etapa).

###  ISSUE 1 - Inventário e Itens
Responsável pelo gerenciamento de itens, limites da mochila e equipamentos.
- [x] **Step 1:** Estrutura Base das Classes (MVP) - `inv-base.py`
- [x] **Step 2:** Regras de Negócio, Tipagem e Limites de Slots
- [x] **Step 3:** Interface visual no console e formatação
- [x] **Step 4:** Tratamento de erros, modularização e Integração final

###  ISSUE 2 - Sistema de Luta e Magia
Responsável pela matemática do combate, vida, mana e turnos.
- [x] **Step 1:** Classes base de Entidades (Personagem e Inimigos) com atributos. -`Classes Base.py`
- [x] **Step 2:** Loop principal do Sistema de Turnos (Atacar, Defender, Fugir).
- [ ] **Step 3:** Sistema de Magias e consumo de Mana.
- [ ] **Step 4:** Integração com a Issue 1 (Uso de itens em combate e cálculo de dano com arma equipada).

###  ISSUE 3 - Narrativa, Storytelling e Diálogos
Responsável pela alma do jogo, classes do jogador e a progressão da história.
- [x] **Step 1:** Motor básico de textos, pausas dramáticas e exibição de diálogos.
- [x] **Step 2:** Sistema de Seleção de Classes iniciais.
- [x] **Step 3:** Árvore de Eventos (Decisões e ramificações da história).
- [x] **Step 4:** Eventos dinâmicos (Encontrar itens, iniciar combates).

###  MAIN - O Coração do Jogo
- [ ] Construir o Menu Principal.
- [ ] Instanciar os módulos (Mochila, Personagem, História).
- [ ] Loop principal de gameplay (O jogo rodando do início ao fim).


##  Como Executar o Jogo

*(As instruções de execução serão adicionadas aqui conforme o projeto for tomando forma).*
