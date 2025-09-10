continuar = 's'
while continuar =='s':
    roupa = input('Qual a marca da roupa?')
    valor = float(input('Qual o valor da roupa?'))
    porcentagem =float(input('Desconto?'))
    valor_parte = valor * (porcentagem / 100)
    valor_novo = valor - valor_parte
    print(f'A peça de roupa {roupa} com {porcentagem}% ficou com o valor de {valor_novo}')

    continuar = input('Continuar? (s/n)')
print('fim do programa')


