Funcionalidade: Gerenciamento do carrinho

Contexto:
Dado que o usuário está autenticado

Cenário: Consultar produto adicionado ao carrinho

Dado que o usuário adicionou "Sauce Labs Backpack" ao carrinho
Quando acessa o carrinho
Então o produto deve ser apresentado
E o nome e o preço devem corresponder ao produto selecionado