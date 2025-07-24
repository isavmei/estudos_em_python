import random 

onde_esta_a_mosca = random.randint(1, 5)
sapo = int(input("digite o valor"))
if sapo == onde_esta_a_mosca:
    print("BROGUET!")
else:
    print("fome!")