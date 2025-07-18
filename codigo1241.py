valores = int(input())

for _ in range(valores):
    valor_A, valor_B = input().split()
    if valor_A[-len(valor_B):] == valor_B:
        print("encaixa")
    else:
        print("nao encaixa")