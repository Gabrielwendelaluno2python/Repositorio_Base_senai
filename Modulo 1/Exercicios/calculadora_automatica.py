import streamlit as st

st.sidebar.title('Tipos de calculos')
calculos = ['SOMA','SUBTRAÇÃO','DIVISÃO','MULTIPLICAÇÃO']
calculos = st.sidebar.selectbox('Selecione o tipo de calculo:',calculos)


st.title('Calculadora-automatica-2.0')
st.write('seja bem vindo')

n1 = st.text_input('Digite o primeiro numero:')
n2 = st.text_input('Digite o segundo numero:')

if st.button('Calcular'):
    n1 = int(n1)
    n2 = int(n2)

    if calculos == 'SOMA':
        resultado = n1+n2
    elif calculos == 'SUBTRAÇÃO':    
        resultado = n1-n2
    elif calculos == 'DIVISÃO':
        resultado = n1*n2
    elif calculos == 'MULTIPLICAÇÃO':
        resultado = n1/n2

    st.warning(f'O calculo da sua expressão numerica ficou {resultado}')















# st.sidebar.image('movida_logo.png')
# st.sidebar.title('Movida - Aluguel de carros')
# st.sidebar.write('Seja bem vindo(a)')

# carros = ['BMW','MUSTANG','HB20','FUSCA','CIVIC']
# carro = st.sidebar. selectbox('Selecione o carro alugado',carros)
# valor_do_dia =0

# if carro == 'BMW':
#     valor_do_dia = 500
# elif carro == 'MUSTANG':    
#     valor_do_dia = 2000
# elif carro == 'HB20':
#     valor_do_dia = 130
# elif carro == 'FUSCA':
#     valor_do_dia = 250
# elif carro == 'CIVIC':
#     valor_do_dia = 180            


# st. title('Movida - Aluguel de carros')
# st. write('Seja bem vindo(a)')
# st.write(f'Voce alugou {carro}')
# st.image(f'{carro}.png')

# dias = st.text_input('Informe a quantidade de dias')
# km = st.text_input('Informe a quantidade kilometros percorridos')

# if st.button('Calcular'):
#     dias = int(dias)
#     km = float(km)

#     valor_dias = dias * valor_do_dia
#     valor_km = km * 0.15
#     total = valor_dias + valor_km

#     st.warning(f'Voce rodou{km} km com o {carro} por {dias} dias. O valor do aluguel sera R${total}')
