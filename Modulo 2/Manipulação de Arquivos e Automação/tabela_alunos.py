import csv

tabela=[
    ["Aluno","Serie","Nota"],
    ["Sarah","2°A",8.5],
    ["Weslen","2°A",5.5],
    ["Victor","2°A",7.0],
    ["Beatris","2°A",8.8],
    ["Gabriel","2°A",9.0]
]


with open('tabela.csv', 'r', encoding='utf-8') as arquivo:
    tabela= csv.reader(arquivo)
    for i in tabela:
        print(i)

Aluno=input('Nome do aluno:')        
Serie=input('Serie do aluno:')
Nota=input('Nota do aluno:')


with open('tabela.csv', 'a', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([Aluno,Serie,Nota])

