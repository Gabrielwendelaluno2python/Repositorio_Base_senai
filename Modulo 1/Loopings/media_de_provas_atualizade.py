# a = 1
# b = 7
# while a <= b:
#     print(a)
#     a = a+1


                                                            


print(60 * '-')
print('CALCULO DE MEDIA')
print(60 * '-')

provas = int(input('Quantas provas o aluno fez?'))
a=1
soma = 0
while a <=provas:
    

    nota =float(input(f'Qual a nota da prova{a}:'))
   
   
   
    soma = soma + nota
    a = a+1
media=round(soma/provas)
print(f'A media do aluno é {media}')


