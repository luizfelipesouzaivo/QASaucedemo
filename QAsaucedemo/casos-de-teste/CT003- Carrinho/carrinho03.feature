Funcionalidade: Gerenciamento do carrinho

Contexto:
Dado que o usuário está autenticado

Cenário: Adicionar múltiplos produtos ao carrinho

Quando o usuário adiciona "Sauce Labs Backpack"
E adiciona "Sauce Labs Bike Light"
Então os produtos devem ser apresentados no carrinho
E o contador deve indicar "2"