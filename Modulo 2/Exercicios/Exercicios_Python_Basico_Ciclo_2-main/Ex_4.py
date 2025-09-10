# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']

# LOOP WHILE

contador = 0
while contador < len(notas):
    print(notas[contador])
    contador = contador + 1



# LOOP FOR

soma=0
for i in notas:
    soma=soma +float(i)
    media=soma/4
print(media)

    



