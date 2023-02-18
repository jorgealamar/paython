print("Bem-vindo à lanchonete!")

# Preços dos ingredientes
preco_pao = {"1": 5.00, "2": 6.00, "3": 7.00}
preco_recheio = {"1": 8.00, "2": 9.00, "3": 7.00}
preco_pagamento = {"1": 0.9, "2": 0.9, "3": 1.0}

# Solicita ao cliente as informações necessárias
tipo_pao = input("Qual será o pão? [1] - Pão Italiano; [2] - Pão Integral; [3] - Pão 4 queijos: ")
tipo_recheio = input("Qual será o recheio? [1] - Carne; [2] - Frango; [3] Vegetariano: ")
tipo_pagamento = input("Qual o método de pagamento? [1] - Dinheiro; [2] - Débito; [3] - Crédito: ")

# Calcula o valor do sanduíche
valor_sanduiche = preco_pao[tipo_pao] + preco_recheio[tipo_recheio]

# Aplica desconto se necessário
if tipo_pagamento in ["1", "2"]:
    valor_sanduiche = valor_sanduiche * preco_pagamento[tipo_pagamento]

# Exibe o valor final
print("O valor do seu sanduíche é R$", valor_sanduiche)
   