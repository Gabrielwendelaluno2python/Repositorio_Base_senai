# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão
# |------------------------------|
# | Escolha uma das opções: 2
# | Digite o primeiro número:100
# | Digite o segundo número:30
# | O resultado é: 70.0
continuar = 's'
while continuar =='s':
     
    print('|',30 * '-','|')
    print('|''Calculadora')
    print('|',30 * '-','|')
    print(f'|1 - Soma')
    print(f'|2 - Subtração')
    print(f'|3 - Multiplicação')
    print(f'|4 - Divisão')
    print('|',30 * '-','|')
    opcao =int(input('| Escolha uma das opçoes:'))
    n1 =float(input('| Digite o primeiro numero:'))
    n2 = float(input('| Digite o segundo numero:'))
    if opcao == 1:
        print(f'| O resultado é: {n1 + n2}')
    if opcao == 2:
        print(f'| O resultado é: {n1 - n2}')
    if opcao == 3:
        print(f'| O resultado é: {n1 * n2}')
    if opcao == 4:
        print(f'| O resultado é: {n1 / n2}')
    
    continuar = input(f'| Deseja continuar? (s/n)')
    print(f'| Fim do programa')

 