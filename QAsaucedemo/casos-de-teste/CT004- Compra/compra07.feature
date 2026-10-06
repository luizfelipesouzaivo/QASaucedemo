Funcionalidade: Finalização de compra

Contexto:
Dado que o usuário está autenticado
E possui "Sauce Labs Backpack" no carrinho

Cenário: Cancelar checkout

Dado que o usuário está na etapa de checkout
Quando seleciona "Cancel"
Então o sistema deve retornar ao carrinho