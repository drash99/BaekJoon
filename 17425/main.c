#include <stdio.h>

int getg(int N){
    int res = 0;
    for (int i=1;i<=N;i++){
        res += i*(N/i);
    }
    return res;
}

int main(){
    int N,k;
    scanf("%d", &N);
    for(int i=0;i<N;i++){
        scanf("%d", &k);
        printf("%d\n", getg(k));
    }
    return 0;
}