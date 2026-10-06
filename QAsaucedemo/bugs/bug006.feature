Funcionalidade: Validação de defeitos conhecidos

Cenário: Preencher o sobrenome no checkout

Dado que estou autenticado como "error_user"
E possuo um produto no carrinho
E estou na etapa de informações do checkout
Quando informo o sobrenome
Então o campo "Last Name" deve aceitar a informação