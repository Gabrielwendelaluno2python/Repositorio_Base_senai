# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE

quant=int(input('Quantos filmes deseja adicionar: '))
soma=1
while soma <=quant:
    nome=input(f'Digite o nome do filme {soma}: ')
    soma +=1
    filmes.append(nome)
print(filmes)





# LOOP FOR

quant=int(input('Quantos filmes deseja adicionar: '))
soma=1
for nome in range(quant):
    nome=input(f'Nome do filme {soma}: ')  
    soma=soma +1
    filmes.append(nome)
print(filmes)


