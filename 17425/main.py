import math
N = int(input())
inputs = []
fs = [1]*1000001
resdata = [0]*1000001


for i in range(2,1000001):
    for j in range(i,1000001,i):
        fs[j] +=i

for i in range(1,1000001):
    resdata[i] = resdata[i-1]+fs[i]

for i in range(N):
    k = int(input())
    inputs.append(k)

for i in inputs:
    print(resdata[i])
