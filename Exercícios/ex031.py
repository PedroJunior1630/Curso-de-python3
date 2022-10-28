print('\033[1;33m=+=' * 15)
print('VIAGEM AÉREA PREÇOS - TABELA \nViagens até 200km: R$0.50\nViagens acima de 200km: R$0.45 por km')
print('=+=' * 15)
print('VIAGEM AÉREA PEÇOS  - TABELA INTERNACIONAL\nViagens até 1500km: R$1.75\nViagens acima de 1500km: R$1.25')
print('=+=' * 15)

local = str(input('\033[1;97mDigite se sua viagem é internacional ou nacional: ')).strip().lower()
distância = int(input('Digite a distância em km da sua viagem: '))

preço1 = distância * 0.50
preço2 = distância * 0.45
preço3 = distância * 1.75
preço4 = distância * 1.25

if local == 'nacional':

    if distância <= 200:
        print(f'\033[1;32mSua viagem {local} de {distância}km custará o valor de R${preço1}')

    else:
        print(f'\033[1;32mSua viagem {local} de {distância}km custara o valor de R${preço2}')

if local == 'internacional':

    if distância <= 1500:
        print(f'\033[1;32mSua viagem {local} de {distância}km custará o valor de R${preço3}')

    else:
        print(f'\033[1;32mSua viagem {local} de {distância}km custará o valor de R${preço4}')
