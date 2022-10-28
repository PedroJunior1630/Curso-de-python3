print('\033[1;33m=+=' * 10)
print('IMPAR OU PAR')
print('=+=' * 10)
numero = int(input('\033[1;97mDigite um numero inteiro: '))
if numero % 2 == 0:
    print('\033[1;34mESTE NÚMERO É PAR')
else:
    print('\033[1;36mESTE NÚMERO É IMPAR')
