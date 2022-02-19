#include <stdio.h>

int dp[11][1024];
int field[10][10]; // 0: . 1: x
int n,m;

int max(int a, int b){
    return (a>b)? a:b;
}

void putdp(int round, int bitmask, int nextmask, int before){
    if (bitmask+1 >= 1<<m){
        dp[round+1][nextmask] = max(dp[round+1][nextmask], before);
        return;
    }

    int fromright = 0;
    while((1<<fromright) & bitmask){
        fromright++;
    }
    bitmask |= (1<<fromright);
    if (field[round][fromright] == 1){
        putdp(round, bitmask, nextmask, before);
        return;
    }

     //2: not put 1 put
    int bitmask2 = bitmask;
    int nextmask2 = nextmask;
    
    if (fromright > 0 && fromright < m){
        nextmask |= (1<<(fromright-1));  
    }
    if (fromright < m-1 && fromright >=0){
        bitmask |= (1<<(fromright+1));
        nextmask |= (1<<(fromright+1));
    }
    putdp(round, bitmask, nextmask, before+1);
    putdp(round, bitmask2, nextmask2, before);
}


int work(){
    scanf("%d %d", &n, &m);
    int i,j;
    char tmp;
    for (i=0;i<n;i++){
        for(j=0;j<m;j++){
            scanf(" %c", &tmp);
            if (tmp == '.') field[i][j] = 0;
            else field[i][j] = 1;
        }
        //scanf("%c", &tmp);
    }
    for (i =0;i<11;i++){
        for(j=0;j<1024;j++){
            dp[i][j] = 0;
        }
    }

    for (int i=0;i<n;i++){
        for (int j=0;j<(1<<m);j++){
            putdp(i,j,0,dp[i][j]);
        }
    }
    int ans = 0;
    for(i =0;i<(1<<m);i++){
        ans = max(ans, dp[n][i]);
    }
    printf("%d\n", ans);
    return 0;
}

int main(){
    int t;
    scanf("%d",&t);
    for (int i=0;i<t;i++){
        work();
    }
    return 0;
}