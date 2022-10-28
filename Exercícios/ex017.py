from math import hypot
print('\033[1;32m==' * 10)
print("VENDO A HIPOTENUSA")
print('==' * 10)
co = float(input("\033[1;97mDigite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hipo = hypot(co, ca)
hipotenusa = (co**2 + ca**2) ** (1/2)
print(f"\033[1;33mA hipotenusa vai medir {hipotenusa:.2f}")
