#include <stdio.h>

long long dp[16][16400];
int n,m;

void putdp(int round, int bitmask, int nextmask, long long before){
    if (before == 0){
        return;
    }
    if (bitmask + 1 >= 1<<m){
        dp[round+1][nextmask] += before;
        return;
    }
    int fromright = 0;
    while((1<<fromright) & bitmask){
        fromright++;
    }
    if (fromright < m-1 && ((2<<fromright) & bitmask)){
        bitmask |= (1<<fromright);
        nextmask |= (1<<fromright);
        putdp(round, bitmask, nextmask, before);
        return;
    }else if (fromright < m-1){
        int bitmask2 = bitmask;
        int nextmask2 = nextmask;
        bitmask2 |= (1<<fromright);
        bitmask2 |= (2<<fromright);
        bitmask |= (1<<fromright);
        nextmask |= (1<<fromright);
        putdp(round, bitmask, nextmask, before);
        putdp(round, bitmask2, nextmask2, before);
        return;
    }else if (fromright == m-1){
        bitmask |= (1<<fromright);
        nextmask |= (1<<fromright);
        putdp(round, bitmask, nextmask, before);
        return;
    }
}


int main(){
    scanf("%d %d", &n, &m);
    while(n!=0 || m!=0){
        int i,j;
        for (i =0;i<16;i++){
            for(j=0;j<16400;j++){
                dp[i][j] = 0;
            }
        }
        dp[0][0] = 1;

        for (int i=0;i<15;i++){
            for (int j=0;j<16384;j++){
                putdp(i,j,0,dp[i][j]);
            }
        }
        printf("%lld\n", dp[n][0]);
        scanf("%d %d", &n, &m);
    }
    return 0;
}