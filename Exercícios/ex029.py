print('\033[1;33m=+=' * 20)
print('FISCALIZÇÃO DE VELOCIDADE')
print('=+=' * 20)
kilometros = int(input('\033[1;97mDigite a quantos km/h esta de velocidade: '))
multa = (kilometros - 80) * 7
if kilometros <= 80:
    print('\033[1;32mVocê está dentro do limite da rodovia,dirija com segurança!')
else:
    print(f'\033[1;31mATENÇÃO!\nVocê ultrapassou o limite de velocidade,estando a {kilometros}km/h! \n{kilometros - 80}km/h acima do limite,sua multa será de R${multa},00')