print("\033[1;33m=-=" * 8)
print("TUDO SOBRE A VARIÁVEL")
print("=-=" * 8)

algo = input("\033[1;30mDigitar algo: ")
print('\033[1;97m=-=' * 13)
print(f"O seu tipo de classe é : {type(algo)}")
print(f"Está em Numérico:{algo.isnumeric()} ")
print(f"Está em Alfanumérico: {algo.isalnum()}")
print(f"Está em Alfabetico: {algo.isalpha()}")
print(f"Está em Maiusculo: {algo.isupper()}")
print(f"Está em Minusculo: {algo.islower()}")
print(f"Está Capitalizada: {algo.istitle()}")
print(f"Apenas espaços: {algo.isspace()}")
print('=-=' * 13)
