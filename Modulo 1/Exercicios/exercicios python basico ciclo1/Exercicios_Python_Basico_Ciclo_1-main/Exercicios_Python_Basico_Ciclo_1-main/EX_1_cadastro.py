# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|', 30 *'-','|')
print('|',15 *'-','CADASTRO',15 *'-','|' )
print('|', 30 *'-','|')
nome = input('| nome:')
idade = input('| idade:')
email = input('| email:')
senha = input('| senha:')

print('|', 30 *'-','|')
print('|',15 *'-','USUARIO CADASTRADO',15 *'-','|' )
print(f'| seja bem vindo(a) {nome}!')
print('|','email:',email)
print('|', 30 *'-','|')