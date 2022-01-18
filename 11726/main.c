#include <stdio.h>

/*
ans = dict()
ans[2] = 2
ans[1] = 1

N = int(input())

def find(num):
    if num in ans.keys():
        return ans[num]
    return (find(num-2) + find(num-1))%10007

for i in range(1,N):
    find(i)
print(find(N))*/

int ans[1001];

int find(int num){
    if (ans[num])
        return ans[num];
    return (find(num-2) + find(num-1))%10007;
}

int main(){
    for(int i=0;i<1001;i++){
        ans[i] = 0;
    }
    ans[1] = 1;
    ans[2] = 2;
    int n;
    scanf("%d",&n);
    
    for(int i=0;i<1001;i++){
        find(i);
    }
    printf("%d\n", find(n));
}
