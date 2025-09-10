# Crie uma lista com 3 dicionários, cada um representando uma pessoa (contendo nome, idade, cidade). Use um laço para imprimir o nome de cada pessoa.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dados=[
    {
        'nome':'bianca',
        'idade':22,
        'cidade':'salvador'
    },
    {
        'nome':'fernando',
        'idade':36,
        'cidade':'bonito'
    },
    {
        'nome':'gabriel',
        'idade':18,
        'cidade':'santana de parnaiba'
    }
]

for i in dados:
    print(i['nome'])
    print(i.values())