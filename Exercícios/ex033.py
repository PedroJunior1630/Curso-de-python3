print('\033[1;33m=+=' * 15)
print('QUAL DOS NÚMEROS É MAIOR')
print('=+=' * 15)

numero1 = int(input('\033[1;97mDigite um numero inteiro: '))
numero2 = int(input('Digite um segundo numero inteiro: '))
numero3 = int(input('Digite um terceiro numero inteiro: '))

if numero1 > numero2 > numero3 or numero1 > numero3 > numero2:
    print(f'\033[1;32mO maior número é {numero1}')

if numero2 > numero3 > numero1 or numero2 > numero1 > numero3:
    print(f'\033[1;32mO maior número é {numero2}')

if numero3 > numero1 > numero2 or numero3 > numero2 > numero1:
    print(f'\033[1;32mO maior número é {numero3}')

if numero1 < numero2 < numero3 or numero1 < numero3 < numero2:
    print(f'\033[1;31mO menor número é {numero1}')

if numero2 < numero3 < numero1 or numero2 < numero1 < numero3:
    print(f'\033[1;31mO menor número é {numero2}')

if numero3 < numero1 < numero2 or numero3 < numero2 < numero1:
    print(f'\033[1;31mO menor número é {numero3}')
