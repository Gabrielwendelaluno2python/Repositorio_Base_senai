# Aluguel de carros:

# # Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# # Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado


# 1 - (dias) Pedir a quantidade de dias
# 2 - (km) Pedir a quantidade de km percorridos

# 3 - (valor_dias) Calcular o valor total dos dias (dias * 60)
# 4 - (valor_km) Calcular o valor total da quilometragem (km * 0.15)


# 5 - (valor_total) Calcular o valor total somando o valor dos dias + o valor dos km

# 6 - Mostrar na tela a frase formatada

print("| ALUGUEL DE CARROS")
print(60 *'-')
carro = input('Qual o marca do carro desejado?')
valor_dia = 0
if carro == 'hb20':
    valor_dia =150
elif carro == 'ferrari':
    valor_dia = 1099
elif carro == 'lamborghini':
    valor_dia = 3400   
elif carro == 'mustang':
    valor_dia = 1295   
else:
    valor_dia =100

dias =float(input('| Quantos dias o carro foi alugado?'))
km =float(input('| Quantos quilometros percorridos'))
print(60 *'-')
valor_dias= dias * valor_dia
valor_km = km * 0.15

valor_total = valor_dias + valor_km

print(f'| O carro {carro} alugado por {dias} dias que percorreu cerca de {km} quilometros,ficou com o preço de R${valor_total}')