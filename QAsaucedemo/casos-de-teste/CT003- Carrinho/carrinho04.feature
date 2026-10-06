Funcionalidade: Gerenciamento do carrinho

Contexto:
Dado que o usuário está autenticado

Cenário: Remover produto do carrinho

Dado que o usuário adicionou "Sauce Labs Backpack" ao carrinho
Quando seleciona "Remove"
Então o produto não deve mais ser apresentado no carrinho