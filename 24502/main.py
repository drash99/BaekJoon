n, k = map(int, input().split())
a = list(map(int, input().split()))



def find(a,k):
    ans = 0
    for idx, i in enumerate(a):
        cur = i%k
        if cur > k//2:
            cursor = idx+1
            while cur%k!=0:
                if k-cur < a[cursor]:
                    a[cursor]-=k-cur
                    ans+= (k-cur) *(cursor-idx)
                    cur = k
                else:
                    cur +=a[cursor]
                    ans += a[cursor] *(cursor-idx)
                    a[cursor]=0
                    cursor+=1
            
        elif idx<len(a)-1:
            a[idx+1] +=cur
            ans+=cur
    return ans

if sum(a) % k != 0:
    print('blobsad')
else:
    print(find(a,k))