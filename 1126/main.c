#include <stdio.h>

int dp[51][500001];

int sh[50];
int heights[50];

int findh(int j, int hd){
    if (j==-1){
        if(hd==0) return 0;
        return -987654321;
    }
    if (dp[j][hd] != -1){
        return dp[j][hd];
    }
    if (hd > sh[j]){
        return -987654321;
    }
    int a,b,c;
    a = findh(j-1, hd);
    b = findh(j-1,hd+heights[j]);
    if (hd > heights[j]){
        c = findh(j-1,hd-heights[j])+heights[j];
    }else{
        c = findh(j-1,heights[j]-hd)+hd;
    }
    int maxi = (a>b)?a:b;
    maxi = (maxi>c)?maxi:c;
    dp[j][hd] = maxi;
    return maxi;
}

int main(){
    int n, shbef;
    scanf("%d", &n);
    shbef = 0;
    for (int i=0;i<n;i++){
        scanf("%d",&heights[i]);
        sh[i] = shbef+heights[i];
        shbef = sh[i];
    }
    for(int i=0;i<51;i++){
        for(int j=0;j<500001;j++){
            dp[i][j] = -1;
        }
    }
    int ans = findh(n-1,0);
    if (ans > 0){
        printf("%d\n", ans);

    }else{
        printf("-1\n");
    }
    return 0;
}
