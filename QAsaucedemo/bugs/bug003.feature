Funcionalidade: Validação de defeitos conhecidos

Cenário: Adicionar produtos específicos ao carrinho

Dado que estou autenticado como "problem_user"
Quando adiciono "Sauce Labs Bolt T-Shirt" ao carrinho
E adiciono "Sauce Labs Fleece Jacket" ao carrinho
E adiciono "Test.allTheThings() T-Shirt (Red)" ao carrinho
Então os três produtos devem ser adicionados ao carrinho