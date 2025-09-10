from colorama import init,Fore
init(autoreset=True)

print('|',30*'-','|')
print('| SISTEMA DE PROVAS')
print('|',30*'-','|')
nome = input('| Nome do aluno?')
n1 =float(input('| Qual a primeira nota?'))
n2 =float(input('| Qual a segunda nota? nota?'))
n3 =float(input('| Qual a terceira nota?'))
print('|',30*'-','|')
resultado=round((n1+n2+n3)/3,2)
print('| O aluno',nome,'\n|tirou a nota',resultado)
if resultado >= 5:
  print('|',Fore.GREEN +' aprovado')
else:
  print('|',Fore.RED +' reprovado')