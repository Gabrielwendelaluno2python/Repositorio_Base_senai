nome =input('Qual é o produto?')
valor_total = float(input('Qual é o valor total do produto?'))
porcentagem =float(input('Qualé a porcentagem?'))
valor_parte = valor_total * (porcentagem / 100)

valor_novo = valor_total - valor_parte
print(f'O{nome} com {porcentagem}% ficou com o valor de {valor_novo}')