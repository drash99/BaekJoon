import random
n =10000
prev = 7
print(n)
for i in range(n):
    nxt = random.randint(1, 10000)
    print(f"{prev} {nxt}")
    prev = nxt

