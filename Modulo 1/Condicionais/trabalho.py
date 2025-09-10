from colorama import init,Fore
init(autoreset=True)






nome =input('Qual é o seu nome?')
n1 =float(input('Qual a primeira nota?'))
n2 =float(input('Qual a segunda nota? nota?'))
n3 =float(input('Qual a terceira nota?'))
resultado=round((n1+n2+n3)/3,2)
print('O aluno',nome,'\ntirou a nota',resultado)
if resultado >= 5:
  print(Fore.LIGHTMAGENTA_EX +'aprovado')
else:
  print(Fore.LIGHTRED_EX +'reprovado')