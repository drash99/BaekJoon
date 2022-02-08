input()
inraw = input().strip().split(' ')
A = []
for r in inraw:
    A.append(int(r))

sum = 0
sum2 = 0
maxi = 0
maxi2 = 0

for i in A:
    if i < 0 and sum >= sum2+i:
        sum2 = sum
        if maxi2 < sum2:
            maxi2 = sum2
    else:
        if sum2 + i < 0:
            sum2 = sum
        else:
            sum2 += i
            if maxi2 < sum2:
                maxi2 = sum2

    if sum + i < 0:
        sum = 0
    else:
        sum += i
        if maxi < sum:
            maxi = sum

if maxi == 0 or maxi2 == 0:
    maxi2 = max(A)
    maxi = max(A)
    
print(max(maxi, maxi2))