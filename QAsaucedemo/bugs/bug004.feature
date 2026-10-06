Funcionalidade: Validação de defeitos conhecidos

Cenário: Preencher o sobrenome durante o checkout

Dado que estou autenticado como "problem_user"
E possuo um produto no carrinho
E estou na etapa de informações do checkout
Quando informo um sobrenome no campo "Last Name"
Então o sobrenome deve ser preenchido no campo correspondente
E o valor informado não deve alterar o campo "First Name"