import os

tarefas ={
    'Tarefas':['Trabalho de portugues','Prova Global'],
    'Datas':['01/07','08/07']
}

def mostrar_tarefas():
    for i in range(len(tarefas['Tarefas'])):
     print(f"|{i+1}. {tarefas['Tarefas'][i]} - Data: {tarefas['Datas'][i]}")


def adicionar_tarefas():
    ad_tarefas = input('Digite a tarefa que deseja adicionar:')
    ad_datas = input('Adicione a data:')
    tarefas['Tarefas'].append(ad_tarefas,)
    tarefas['Datas'].append(ad_datas)
    print('Tarefa adicionada com sucesso...')


def remover_tarefa():
    mostrar_tarefas()
    try:
        remover = int(input('Digite o numero da tarefa que deseja remover:'))
        tarefas['Tarefas'].pop(remover-1)
        tarefas['Datas'].pop(remover-1)
        print('Tarefa removido com sucesso...')
    except ValueError:
        print('Coloque um comando valido')


def mostrar_menu():
    while True:
        os.system('cls')
        barra = f'|{30*'-'} '
        print(barra)
        print('| TAREFAS')
        print(barra)
        print('|(1) Mostrar tarefas')
        print('|(2) Adicionar tarefas')
        print('|(3) Remover tarefa')
        print('|(4) Sair')
        print(barra)
        opcao = int(input('|Escolha um numero:'))

        try:
            if opcao == 1:
                os.system('cls')
                mostrar_tarefas()
                input('Pressione enter para continuar...')
            elif opcao == 2:
                os.system('cls')
                adicionar_tarefas()
                input('Pressione enter para continuar...')
            elif opcao == 3:
                os.system('cls')
                remover_tarefa()
                input('Pressione enter para continuar...') 
            elif opcao == 4:
                print('|saindo...')
                break
            else:
                print('Digite um numero valido...')
                input('Aperte enter para continuar:')  
        except ValueError:
            print('Digite um numero valido')
            input('Pressione enter para continuar...')

mostrar_menu()
