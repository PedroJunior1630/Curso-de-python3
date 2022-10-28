print('\033[1;33m=+=' * 10)
print('AUMENTO SALARIAL')
print('=+=' * 10)

salario = int(input('\033[1;97mDigite seu salario: '))
aumento10 = salario + (salario * 10 / 100)
aumento15 = salario + (salario * 15 / 100)

if salario > 1250:
    print(f'\033[1;32mSeu novo salario com aumento de 10% será R${aumento10}')
else:
    print(f'\033[1;32mSeu novo salario com aumento de 15% será R${aumento15}')
