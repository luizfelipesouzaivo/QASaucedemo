Funcionalidade: Finalização de compra

Contexto:
Dado que o usuário está autenticado
E possui "Sauce Labs Backpack" no carrinho

Cenário: Tentar avançar sem informar o CEP

Quando o usuário informa "Luiz" no campo primeiro nome
E informa "Felipe" no campo sobrenome
E deixa o CEP em branco
E seleciona "Continue"
Então o sistema deve apresentar uma mensagem de validação
E não deve permitir o avanço