# Utilizando tanto um loop while quanto um loop for, escreva um código que exiba na tela o resultado abaixo:

#ID: 354 | Aluno: Fabrício
#ID: 847 | Aluno: Leandro
#ID: 195 | Aluno: Marcela


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
lista = ['Fabrício', 'Leandro', 'Marcela', [354, 847, 195, 0]] # Não apague e nem altere essa 


# LOOP WHILE

contador = 0
while contador < len(lista)-1:
    print(f'ID: {lista[3][contador]} | Aluno: {lista[contador]}')
    contador = contador + 1




# LOOP FOR

for i in range(len(lista)-1): 
    print(f'ID: {lista[3][i]} | Aluno: {lista[i]}')

    

