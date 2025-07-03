casos = int(input())

for _ in range(casos):
    X, Y = map(int, input().split())

    menor = min(X, Y)
    maior = max(X, Y)

    soma = 0
    for i in range(menor + 1, maior):
        if i % 2 != 0:
            soma += i

    print(soma)

Para aceitar qualquer ordem — ou seja, tanto x > y quanto y > x — e sempre fazer a contagem do maior para o menor, basta usar as funções min() e max() para garantir isso.