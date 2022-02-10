N, M = map(int, input().split())


nums = list(set(map(int,input().split())))
nums.sort()

answ = []

def printnm(hubo, current, m):
    if m == 1:
        for i in hubo:
            if not current+str(i) in answ:
                answ.append(current+str(i))
        return
    else:
        for i in hubo:
            tmp = []
            for j in hubo:
                if i <= j:
                    tmp.append(j)
            printnm(tmp,current+str(i)+' ', m-1)
        return
        

printnm(nums,'',M)
for i in answ:
    print(i)