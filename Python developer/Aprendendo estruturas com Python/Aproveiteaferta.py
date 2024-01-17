T = int(input())

for i in range(T):
    N, K = input().split()
    N = int(N)
    K = int(K)
    total = int(int((N/K) + int((N/K)))) 
    print (total)