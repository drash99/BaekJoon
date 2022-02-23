n, k = map(int, input().split())
a = list(map(int, input().split()))



def find(a,k):
    assert sum(a)>=0
    #print(a)
    if len(a) == 0:
        return 0
    if len(a) == 1:
        assert a[0]%k==0
        return 0
   
    middle = len(a)//2
    left = a[:middle]
    right = a[middle+1:]
    ls= sum(left)%k
    rs = sum(right)%k
    ms = a[middle]%k
    #assert not(sum(left) <0 and sum(right) <0)
    if sum(left) < 0:
        if sum(right) < 0:
            left[-1] += k-ls
            right[-1] += k-rs
            ans = k-rs+ k-ls
            ans += find(left,k)
            ans += find(right,k)
            return ans
        tmp  = ms+rs*2
        ls = 987654321
    elif sum(right) < 0:
        tmp = ms+ls*2
        rs = 987654321
    else:
        tmp = min(rs+ls, ms+rs*2, ms+ls*2)
    ans = tmp
    if tmp == rs+ls:
        left[-1] -= ls
        if right:
            right[0] -= rs
    elif tmp == ms+rs*2:
        left[-1] += ms+rs
        if right:
            right[0] -= rs
    else:
        left[-1] -= ls
        if right:
            right[0] += ms+ls

    
    ans += find(left,k)
    ans += find(right,k)
    return ans

if sum(a) % k != 0:
    print('blobsad')
else:
    print(find(a,k))