
n = int(input())


tmp = 0

for i in range(2,n+1):
    if i%2==0:
        tmp = (tmp*i+1)%1000000000
    else:
        tmp = (tmp*i-1)%1000000000

print(tmp)