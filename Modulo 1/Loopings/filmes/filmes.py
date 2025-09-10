



fim=int(input('Quantos jogos voce deseja adicionar:'))
contador = 1
jogos = []
while contador <= fim:
    nome =input(f'Digite o nome de um jogo {contador}:')
    jogos.append(nome)
    contador = contador + 1

print(jogos)