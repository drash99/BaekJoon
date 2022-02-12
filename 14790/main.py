t = int(input())

for k in range(t):
    n = list(map(int, list(input())))
    for i in range(len(n)-2,-1,-1):
        if n[i] > n[i+1]:
            n[i] -= 1
            for j in range(i+1,len(n)):
                n[j] = 9
    while(n[0] == 0):
        n.pop(0)
    print(f"Case #{k+1}: "+''.join(map(str,n)))