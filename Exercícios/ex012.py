print("\033[1;33m=-=" * 15)
print("ESTE PRODUTO CONTÉM 5% DE DESCONTO!")
print("=-=" * 15)
produto = float(input("\033[1;97mDigite o preço do produto: "))
desconto = produto - (produto * 5 / 100)
print("\033[1;32m===" * 25)
print(f"Seu produto com desconto de 5% ficou no valor de R${desconto:.2f}")
print("===" * 25)
