print('\033[1;31m=-=' * 10)
print('SEU NOME TEM..?')
print('=-=' * 10)
nome = str(input('\033[1;97mDigite seu nome: ')).strip().upper()
print(f"\033[1;36mSeu nome contém 'SILVA'? {'SILVA' in nome}")
