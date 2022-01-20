input()
mraw = input().strip().split(' ')
mset = set()
for mr in mraw:
    mset.add(int(mr))
input()
cardraw = input().strip().split(' ')
ans = ""
for card in cardraw:
    if int(card) in mset:
        ans += "1 " 
    else:
        ans += "0 "

print(ans)
