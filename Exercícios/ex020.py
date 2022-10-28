from random import shuffle
print('\033[1;33m=+='*20)
print("ORDEM DE APRESENTAÇÃO NO TRABALHO")
print('=+='*20)
n1 = input('\033[1;97mDigite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
ordem = [n1, n2, n3, n4]
shuffle(ordem)
print(f"\033[1;34mA ordem de apresentação do trabalho será da seguinte maneira:\n{ordem}")
