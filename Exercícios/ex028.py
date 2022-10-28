import random
print('\033[1;33m=+=' * 20)
print('JOGO DA ADIVINHAÇÃO')
print('=+=' * 20)

computador = random.randint(0, 5)
usuario = int(input('\033[1;97mTENTA ADIVINHAR UM NUMERO INTEIRO QUE ESTOU PENSANDO ENTRE 0 E 5: '))

if usuario == computador:
    print('\033[1;32mPARABÉNS! VOCÊ GANHOU')
else:
    print(f'\033[1;31mERRRROUUUU EU PENSEI NO NÚMERO {computador}')
