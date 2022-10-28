import math
print('\033[1;33m==' * 20)
print("SENO,COSSENO E TANGENTE DE UM ANGULO")
print('==' * 20)
angulo = float(input("\033[1;97mDigite o angulo que deseja: "))
radianos = angulo * 3.14 / 180
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print(f"\033[1;36mCom o angulo de {angulo} temos:\nSeno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}")
