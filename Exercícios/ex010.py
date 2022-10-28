print('\033[1;32m=-=' * 20)
print('CONVERTENDO REAIS PARA DOLARES E EUROS')
print('=-=' * 20)
real = float(int(input('\033[1;33mQuantos R$ tem em sua carteira? ')))
dolar = real / 4.83
euro = real / 5.15
print(f'Atualmente R${real} está valendo: ')
print('\033[1;36m=-=' * 10)
print(f'Dolár : {dolar:.2f} \nEuro : {euro:.2f}')
print('=-=' * 10)
