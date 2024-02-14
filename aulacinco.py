'''
Exercício Proposto:
O custo de um carro novo para o consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e os impostos
(aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos sejam de 45%, escreva
um código no qual o usuário deve informar o custo de fábrica de um carro e, em seguida, calcular e apresentar no console 
o custo final para o consumidor.

Louyse Macedo
Faculdade Descomplica
'''
# Solicita ao usuário que informe o custo de fábrica do carro
custo_de_fabrica = int(input("Informe o custo de fábrica do carro: "))

# Define as taxas percentuais do distribuidor e dos impostos
percentual_distribuidor = 0.28
percentual_impostos = 0.45

# Calcula o custo final para o consumidor
custo_final = custo_de_fabrica + (custo_de_fabrica * percentual_distribuidor) + (custo_de_fabrica * percentual_impostos)

# Imprime o custo final para o consumidor
print("O custo final para o consumidor é de R$", custo_final)

