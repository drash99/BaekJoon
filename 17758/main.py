fibs = [1,2]

while(fibs[-1] < 10**100):
    fibs.append(fibs[-1]+fibs[-2])

c= int(input())
print(fibs[:100])
cn = 10**len(str(c))
print(c, cn)
def find():
    for i in fibs:
        if i%cn == c:
            print(i)
            return 
    print('NIE')
find()