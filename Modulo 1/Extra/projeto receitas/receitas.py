import streamlit as st

st.sidebar.title('Gabis Receitas')
receitas =['DOCES','SALGADOS','FIT','VEGANAS']
receita = st.sidebar.selectbox(f'Selecione o tipo de receita:',receitas)


st.title('GABIS RECEITAS')
st.write('seja bem vindo ao gabis receitas')


ingredientes, modo_preparo = st.tabs(['Ingredientes','Modo de preparo'])

with ingredientes:
    col1, col2 = st.columns(2)

    # --------------------------------------------------- Salgados
    if receita == 'SALGADOS':
        with col1:
        
            st.markdown('''Torta de frango
                        Massa:
- 3 xícaras (chá) de Farinha de trigo Super Premium Renata Tipo 1
- 3 ovos
- 3 xícaras (chá) de leite
- 1 colher (sopa) de fermento químico
Recheio:
- 1 xícara (chá) de frango desfiado
- 1 lata de milho verde em conserva escorrido
- 2 tomates sem sementes picados
- 10 azeitonas verdes em rodelas
- 1 colher (chá) de sal
- 3 colheres (sopa) de salsa picada ''')
            
        with col2:
            st.image('torta de frango.png')
    # ------------------------------------------------- DOCES
    elif receita == 'DOCES':
        with col1:
            st.markdown(''' Mousse de chocolate
- 1 lata de Creme de Leite
- 200 g de Chocolate Meio Amargo picado
- 3 claras
- 3 colheres (sopa) de açúcar''')

        with col2:    
            st.image('MOUSSE DE CHOCOLATE.png')


    # ------------------------------------------------- FIT
    elif receita == 'FIT':
        with col1:
            st.markdown('''Empada de frango fit
- 3 ovos
- 80 ml de leite desnatado
- 1 colher de sopa açúcar mascavo
- 8 colheres de sopa de farinha de aveia
- 3 colheres de sopa de farelo de aveia
- 2 colheres de sopa de azeite
- Sal a gosto
- 1 colher de sobremesa de fermento químico em pó
- Azeite para untar
- Farinha de aveia para enfarinhar
- Recheio:

- 1 peito de frango desfiado, cozido e temperado a gosto
- Ricota a gosto
- Azeite para pincelar''')

        with col2:    
            st.image('empada fit.png')
            

    # ------------------------------------------------- VEGANAS

    elif receita == 'VEGANAS':
        with col1:
         st.markdown(''' Pavlova:
- Massa da pavlova (merengue):
- 1 colher de sopa de proteína de soja isolada
- 1 colher de chá de goma xantana
- 1 xícara de açúcar de confeiteiro peneirado
- 6 colheres de sopa de água

- Recheio:
- 2 xícaras de leite de coco
- 90g de chocolate meio amargo vegano
- 3 colheres de sopa de amido de milho
- Frutas vermelhas da preferência''')
         
        with col2:    
            st.image('palvova.png')






#-------------------------------------------------------------------
with modo_preparo:
    col1, col2 = st.columns(2)
    if receita == 'SALGADOS':
        with col1:
        
                
            st.markdown('''MODO DE PREPARO:
- 1
Recheio:

Em uma travessa, junte o frango, os tomates, o milho e as azeitonas.

Acrescente o sal e salsa picada, misture bem e reserve.

- 2
Massa:

Em um liquidificador, bata todos os ingredientes líquidos e, em seguida, acrescente o restante dos ingredientes até obter uma massa homogênea.

- 3
Montagem:

Unte uma assadeira retangular grande. Espalhe metade da massa na forma, adicione o recheio e finalize com o restante de massa.

Polvilhe o queijo parmesão e leve ao forno a 180°C, já preaquecido por cerca de 40 minutos ou até dourar.

Espere esfriar para cortar em quadradinhos e sirva! ''')
            

        with col2:
            st.video('https://www.youtube.com/watch?v=QYm0HkdFN_c')
#--------------------------------------------------------------------------------------------
with modo_preparo:
    col1, col2 = st.columns(2)
    if receita == 'DOCES':
        with col1:
            
            st.markdown(''' MODO DE PREPARO:
- 1.
Em uma panela em banho-maria, aqueça o NESTLÉ Creme de Leite.
- 2.Junte o Chocolate NESTLÉ CLASSIC e mexa até que fique uma mistura homogênea. Reserve.
- 3.Em uma panela, misture as claras e o açúcar e leve ao fogo baixo, mexendo vigorosamente sem parar, por cerca de 3 minutos, tirando a panela do fogo por alguns instantes a cada minuto, continuando a mexer, para não cozinhar.
- 4.Transfira para uma batedeira e bata por 5 minutos ou até dobrar de volume.
- 5.Misture levemente ao creme de Chocolate.
- 6.Coloque em taças e leve à geladeira por cerca de 3 horas.
- 7.Decore com cerejas, chantilly ou raspas de chocolate''')
            with col2:
             st.video('https://www.youtube.com/watch?v=rG1osb8STH0')
#----------------------------------------------------------------------------------------

with modo_preparo:
    col1, col2 = st.columns(2)
    if receita == 'FIT':
        with col1:

            st.markdown(''' MODO DE PREPARO:
- Massa

Em um recipiente, coloque os ovos, o leite e o açúcar mascavo e misture bem. Adicione a farinha, o farelo de aveia, o azeite e o sal e mexa até obter uma consistência homogênea. Por último, coloque o fermento químico e misture delicadamente. Reserve.

- Recheio

Em um recipiente, coloque o frango e a ricota e misture bem. Reserve. Unte formas de empada com azeite e enfarinhe com farinha de aveia, disponha um pouco de massa sobre elas e preencha o fundo e as laterais. Cubra com o recheio e finalize com restante da massa, pressionando as laterais para fechar. Pincele com o azeite e leve ao forno preaquecido a 200°C até dourar. Sirva em seguida.''')

with modo_preparo:
    
    if receita == 'FIT':
        with col2:
         st.video('https://www.youtube.com/watch?v=aZEHLzohzJI')

#--------------------------------------------------------------------------------------
with modo_preparo:
    col1, col2 = st.columns(2)
    if receita == 'VEGANAS':
        with col1:
        
                
            st.markdown('''MODO DE PREPARO:
- Na batedeira, misture a água e a proteína de soja isolada até desmanchar totalmente, batendo na potência máxima. Isso evita que fique com pedacinhos de soja na goma. Acrescente a goma xantana e bata, ainda em potência máxima por alguns minutos. Vai virar uma goma mesmo. Vá acrescentando o açúcar, de colher em colher e esperando que se dissolva. Desligue. A goma estará grudada, praticamente toda, na pá da batedeira. Numa assadeira forrada com papel próprio para forno, coloque a mistura, formando uma bola. Tente deixar um buraco no meio, onde colocará o recheio depois de assada. Leve ao forno a 130 °C ou o mais baixo possível por cerca de 1 h 15min. Desligue e deixe esfriar.

Para o recheio:

- Junte o leite e o chocolate. Leve ao fogo até derreter o chocolate. Dissolva o amido em um pouquinho de água e junte ao leite. Deixe que engrosse bem. Leve à geladeira.
Depois que o suspiro estiver frio, coloque o creme no buraco que fez, enfeite com frutas diversas, salpique coco ralado e sirva.''')

with modo_preparo:

    if receita == 'VEGANAS':
        with col2:
         st.video('https://www.youtube.com/watch?v=GCvzzJiljS4')
