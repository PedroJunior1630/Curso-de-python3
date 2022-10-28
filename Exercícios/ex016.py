from math import trunc
print('\033[1;34m=+='*15)
print("MOSTRANDO A PORÇÃO INTEIRA DE UM NUMERO")
print('=+='*15)
num = float(input('\033[1;97mDigite um numero flutuante: '))
porçao = trunc(num)
print('\033[1;33m=+='*15)
print(f"A porção inteira do numero {num} \nEquivale a {int(num)}")
print('=+='*15)
