print('\033[1;34m=-=' * 15)
print('PRIMEIRO E ULTIMO NOME')
print('=-=' * 15)
nome = str(input('\033[1;97mDigite seu nome completo: ')).strip().split()
print(f"\033[1;36mSeu primeiro nome: {nome[0]} ")
print(f"Seu ultimo nome: {nome[-1]}")
