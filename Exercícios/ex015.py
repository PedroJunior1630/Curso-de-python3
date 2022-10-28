print("\033[1;33m=_-_=" * 10)
print("ALUGUEL DE CARROS")
print("=_-_=" * 10)
km = int(input("\033[1;97mDigite a quantidade de km rodados: "))
dia = int(input('Digite a quantidade de dias alugados: '))
taxakm = km * 0.15
taxadia = dia * 60
print("\033[1;32m=_-_=" * 10)
print(f"Com {dia} dias alugados e {km} km rodados o aluguel custará: \nR${taxakm + taxadia:.2f}")
print("=_-_=" * 10)
