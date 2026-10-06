Funcionalidade: Consulta de produtos

Contexto:
Dado que o usuário está autenticado

Cenário: Remover produto do carrinho pela página de produtos

Dado que o produto "Sauce Labs Backpack" está no carrinho
Quando o usuário seleciona "Remove"
Então o produto deve ser removido do carrinho
