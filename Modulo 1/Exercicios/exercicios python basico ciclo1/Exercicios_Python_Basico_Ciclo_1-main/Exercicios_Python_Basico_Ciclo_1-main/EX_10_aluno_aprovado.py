# Escreva um código que pede a nota de duas provas do aluno e verifique se o aluno foi aprovado com as condições abaixo:
# O aluno precisa ter média maior que 7 e não pode ter tirado zero em nenhuma nota.
# Não é necessário usar estruturas condicionais, apenas expressões lógicas conforme estudado no material de expressões lógicas.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite a primeira nota: 10
# Digite a segunda nota: 8
# Aluno aprovado? True

# Exemplo 2:

# Digite a primeira nota: 10
# Digite a segunda nota: 0
# Aluno aprovado? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|' ,30 * '-', '|')
print('MEDIA DE PROVAS')
print('|' ,30 * '-', '|')

nome = input('| nome do aluno:')
n1 = float(input('| Nota da primeira prova:'))
n2 = float(input('| Nota da segunda prova:'))
n3 = float(input('| Nota da terceira prova:'))
media =(n1+n2+n3) /3
print('|', 30 * '-', '|')
print(f'| Aluno: {nome}')
print(f'| media: {media}')

if (media >=7) and (n1 != 0) and (n2 != 0) and (n3 !=0):
   print('Aluno aprovado')
else:
    print('Aluno reprovado')
