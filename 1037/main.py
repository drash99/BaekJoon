N = int(input().strip())
inputraw = input().strip().split(' ')
data = []
for i in inputraw:
    data.append(int(i))
print(max(data)*min(data))