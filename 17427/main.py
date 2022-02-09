N = int(input())

res = 0

for i in range(N):
    res += (i+1) *( N//(i+1))
print(res)