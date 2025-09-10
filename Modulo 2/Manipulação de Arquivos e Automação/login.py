import csv

Gmail =input('Digite seu gmail:')
Senha =input('Digite sua senha:')

with open('login.csv', 'r', encoding='utf-8') as arquivo:
    login = csv.reader(arquivo)
    for linha in login:
        if (linha[0]) == Gmail:
            print('Gmail valido')
            if(linha[1]) == Senha:
                print('Senha valida')
       
           





      

