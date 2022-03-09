n = int(input())
a = [0]*(n+1)
for i in range(1,n):
    a[(i*i)%n] += 1

b = a[:]
c = a[:]
d = a[:]  
ans =0
for i in range(1,n):
    for j in range(i,n):
        tmp = (i*i+j*j)%n
        if a[tmp]:
            #print(i,j, tmp, a[tmp])
            ans+=a[tmp]
print(ans)