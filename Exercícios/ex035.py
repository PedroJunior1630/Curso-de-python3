print('\033[1;32m=+=' * 15)
print('FORMA UM TRIANGULO?...')
print('=+=' * 15)

ab = float(input('\033[1;97mDigite o comprimento da primeira reta: '))
cd = float(input('Digite o comprimento da segunda reta: '))
ef = float(input('Digite o comprimento da terceira reta: '))

formula = ab + cd
formula2 = cd + ab
formula3 = ef + ab
formula4 = cd + ef

if formula > ef and formula2 > ef and formula3 > cd and formula4 > ab:

    print(f'\033[1;34mEstes segmentos PODEM formar um triangulo!')

else:
    print(f'\033[1;31mEstes segmentos NÃO PODEM formar um triangulo!')
