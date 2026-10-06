Funcionalidade: Finalização de compra

Contexto:
Dado que o usuário está autenticado
E possui "Sauce Labs Backpack" no carrinho

Cenário: Finalizar compra com sucesso

Dado que o usuário preencheu os dados obrigatórios
E está na tela de resumo do pedido
Quando seleciona "Finish"
Então o sistema deve concluir a compra
E deve apresentar a confirmação do pedido