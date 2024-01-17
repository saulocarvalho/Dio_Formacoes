N = int(input()) # numero de casos de testes

while(N > 0):
    N -= 1
    A, B = input().split() # entrada A e B

    if A.endswith(B):
        print('encaixa')
    else:
        print('nao encaixa')