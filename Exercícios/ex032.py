from datetime import date
print('\033[1;33m=+=' * 20)
print('VERIFICANDO SE ESTE ANO É BISSEXTO')
print('=+=' * 20)
ano = int(input('\033[1;97mDigite um ano: '))
ano2 = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;32mO ano {ano} é bissexto')
else:
    print(f'\033[1;31mO ano {ano} não é bissexto')
