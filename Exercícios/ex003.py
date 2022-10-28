print("\033[1;34m=-=" * 20)
print("SOMANDO,SUBTRAINDO,MUTIPLICANDO,DIVIDINDO E POTENCIA")
print("=-=" * 20)

n1 = int(input("\033[1;37mDigite um numero: "))
n2 = int(input("Digite outro: "))

soma = n1 + n2
subtrair = n1 - n2
dividir = n1 / n2
mutitplicar = n1 * n2
potencia = n1 ** n2

print(f"\033[1;97mSoma : {n1} + {n2} = {soma}")
print(f"Subtração: {n1} - {n2} = {subtrair}")
print(f"Mutiplicação: {n1} x {n2} = {mutitplicar}")
print(f"Divisão: {n1} ÷ {n2} = {dividir} ")
print(f"Potência: {n1} ^ {n2} = {potencia}")
