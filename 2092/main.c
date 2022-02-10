#include <stdio.h>
#include <stdlib.h>

int static compare (const void* first, const void* second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}


int dp[4001][4001] ={0};
int modu = 1000000;


int main(){
    int t,a,s,b;
    int last = 0;
    dp[0][0] = 1;
    scanf("%d %d %d %d", &t,&a,&s,&b);
    int nums[4002];
    for (int i=0;i<a;i++){
        scanf("%d",&nums[i]);
    }
    qsort(nums, a, 4, compare);

    for (int i=0;i<a;i++){
        if (nums[i] == last){
            dp[i+1][0] = 1;
            for (int j=0;j<((b<i+1)?b:i+1);j++){
                dp[i+1][j+1] = (dp[i][j] - dp[i-1][j] + dp[i][j+1])%modu;
            }
        }else{
            dp[i+1][0] = 1;
            for (int j=0;j<((b<i+1)?b:i+1);j++){
                dp[i+1][j+1] = (dp[i][j] + dp[i][j+1])%modu;
            }
            last = nums[i];
        }
    }

    long long ans = 0;
    for (int i=s;i<=b;i++){
        ans += dp[a][i];
        ans %= modu;
    }
    printf("%d\n", ans%modu);
}