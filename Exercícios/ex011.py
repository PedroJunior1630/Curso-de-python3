print("\033[1;35m=-=" * 15)
print("NECESSARIO DE TINTA PARA PINTAR SUA PAREDE!")
print("=-=" * 15)
a = float(input('\033[1;97mDigite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
area = a * l
litros = area / 2
print("\033[1;36m=-=" * 15)
print(f'Sua area tem {area}m² \nSerá necessario {litros:.2f}L de tinta para pintar a parede')
print("=-=" * 15)
