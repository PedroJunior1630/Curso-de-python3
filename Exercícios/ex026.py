print('\033[1;31m=-=' * 10)
print('LETRAS')
print('=-=' * 10)
frase = str(input('\033[1;97mDigite uma frase: ')).strip().lower()
print(f"\033[1;33mA letra 'A' aparece {frase.count('a')} vezes")
print(f"A posiçao que a letra 'A' aparece pela primeira vez: {frase.find('a') + 1}")
print(f"A posiçao que a letra 'A' aparece pela ultima vez: {frase.rfind('a') + 1}")
