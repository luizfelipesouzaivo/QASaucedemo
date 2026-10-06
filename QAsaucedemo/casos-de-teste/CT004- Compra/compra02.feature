Funcionalidade: Finalização de compra

Contexto:
Dado que o usuário está autenticado
E possui "Sauce Labs Backpack" no carrinho

Cenário: Preencher dados obrigatórios

Quando o usuário informa "Luiz" no campo primeiro nome
E informa "Felipe" no campo sobrenome
E informa "20000000" no campo CEP
E seleciona "Continue"
Então o sistema deve apresentar o resumo do pedido