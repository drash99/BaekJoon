import heapq


for _ in range(int(input())):
    n = int(input())    
    c = list(map(int, input().split()))
    ans = 0
    while len(c) > 1:
        print(c)
        newc = []
        mini = 987654321
        pos = 0
        for i in range(len(c)-1):
            if mini > c[i]+c[i+1]:
                pos = i
                mini = c[i]+c[i+1]
        ans += c[pos]+c[pos+1]
        newc = c[:pos] +[c[pos]+c[pos+1]] + c[pos+2:]
        c = newc
    print(ans)