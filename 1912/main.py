input()
inraw = input().strip().split(' ')
A = []
for r in inraw:
    A.append(int(r))

sum = 0
maxi = 0

for i in A:
    if sum + i < 0:
        sum = 0
    else:
        sum += i
        if maxi < sum:
            maxi = sum

if maxi == 0:
    maxi = max(A)
print(maxi)