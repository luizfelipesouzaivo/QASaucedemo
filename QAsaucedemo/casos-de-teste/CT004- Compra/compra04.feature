Funcionalidade: Finalização de compra

Contexto:
Dado que o usuário está autenticado
E possui "Sauce Labs Backpack" no carrinho

Cenário: Tentar avançar sem informar o sobrenome

Quando o usuário informa "Luiz" no campo primeiro nome
E deixa o sobrenome em branco
E informa "20000000" no campo CEP
E seleciona "Continue"
Então o sistema deve apresentar uma mensagem de validação
E não deve permitir o avanço