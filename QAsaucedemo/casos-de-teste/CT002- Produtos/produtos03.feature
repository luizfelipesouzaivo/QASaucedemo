Funcionalidade: Consulta de produtos

Contexto:
Dado que o usuário está autenticado

Cenário: Adicionar produto ao carrinho

Quando o usuário seleciona "Add to cart" para o produto "Sauce Labs Backpack"
Então o produto deve ser adicionado ao carrinho
E o contador do carrinho deve ser atualizado