import streamlit as st
#------------------------------------------------------------------------------
st.sidebar.title('games insanos')
st.sidebar.write('escolha uma opçao de jogo')
jogos =['GOD OF WAR 3','SILENT HILL','HORIZON','GOD OF WAR RAGNAROK']
jogos = st.sidebar.selectbox(f'Selecione o tipo de receita:',jogos)

#----------------------------------------------------------------------------- god of war
st.title('games insanos')
st.write('bem vindos ao games insanos')

descrição, video_do_jogo = st.tabs(['descrição','video_do_jogo'])

with descrição:
    col1, col2 = st.columns(2)

    if jogos == 'GOD OF WAR 3':
        with col1:(''' God of War 3 é um jogo de ação e aventura com elementos de hack and slash,
     onde o jogador controla Kratos em sua jornada de vingança contra os deuses do Olimpo. O jogo é ambientado na mitologia grega, com Kratos lutando contra monstros,
     deuses e Titãs para chegar ao Monte Olimpo e derrubar Zeus. ''')
            
        with col2:
            st.image('god of war 3.png')

with video_do_jogo:
    if jogos == 'GOD OF WAR 3':
        st.video('https://www.youtube.com/watch?v=Jb2YhOD0wq4')

#------------------------------------------------------------------------------------------------------silent hill
with descrição:
    col1, col2 = st.columns(2)

    if jogos == 'SILENT HILL':
        with col1:('''Silent Hill é uma franquia de jogos eletrônicos de survival horror que se destaca por seu terror psicológico e atmosfera sombria.
A série se passa na cidade fictícia de Silent Hill, um local que reflete os traumas e conflitos internos de seus personagens,
distorcendo-os em formas de monstros e cenários perturbadores.''')
        with col2:
            st.image('silent hill.png')

with video_do_jogo:
    if jogos == 'SILENT HILL':
        st.video('https://www.youtube.com/watch?v=V1vcKv6sMH0')
#-------------------------------------------------------------------------------------------------------HORIZON
with descrição:
    col1, col2 = st.columns(2)

    if jogos == 'HORIZON':
        with col1:('''  Horizon, desenvolvida pela Guerrilla Games, é ambientada num futuro distante,
         onde máquinas colossais dominam a Terra e a civilização humana regrediu a tribos de caçadores e coletores. A protagonista Aloy,
         uma jovem caçadora, explora este mundo pós-apocalíptico, enfrentando perigosas máquinas e tribos rivais, enquanto busca descobrir os segredos do passado e o futuro do mundo. ''')
        with col2:
            st.image('horizon.png')

with video_do_jogo:
    if jogos == 'HORIZON':
        st.video('https://www.youtube.com/watch?v=3lP409r_iqo')          
#--------------------------------------------------------------------------------------------------------RAGNAROK
with descrição:
    col1, col2 = st.columns(2)

    if jogos == 'GOD OF WAR RAGNAROK':
        with col1:(''' God of War Ragnarök é um jogo de ação e aventura que segue Kratos e seu filho Atreus em uma jornada pelos Nove Reinos, visando impedir o iminente Ragnarök.
 A história do jogo explora a busca de Atreus por conhecimento e a decisão de Kratos em lidar com seu passado para se tornar o pai que Atreus precisa.
 O jogo permite que os jogadores explorem paisagens perigosas, lutem contra deuses e monstros nórdicos, e usem as armas e habilidades de Kratos e Atreus para proteger sua família''')
        with col2:
            st.image('ragnarok.png')

with video_do_jogo:
    if jogos == 'GOD OF WAR RAGNAROK':
        st.video('https://www.youtube.com/watch?v=XenErbIUHq4')              

