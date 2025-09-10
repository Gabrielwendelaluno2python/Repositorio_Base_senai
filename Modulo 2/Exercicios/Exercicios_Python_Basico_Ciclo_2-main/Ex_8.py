# Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Crie um dicionário com duas chaves: "pares" e "ímpares", onde cada chave terá uma lista com os números correspondentes.


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

correspondente={
    'pares':[],
    'impares':[]
}

for i in numeros:
    if i % 2 ==0:
        correspondente['pares'].append(i)
    else:
        correspondente['impares'].append(i)
print(correspondente)  
        
