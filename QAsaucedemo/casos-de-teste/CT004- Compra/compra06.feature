Funcionalidade: Finalização de compra

Contexto:
Dado que o usuário está autenticado
E possui "Sauce Labs Backpack" no carrinho

Cenário: Validar resumo do pedido

Dado que o usuário preencheu os dados obrigatórios
Quando seleciona "Continue"
Então o sistema deve apresentar o produto selecionado
E deve apresentar o valor do produto
E deve apresentar o imposto
E deve apresentar o valor total