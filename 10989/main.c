#include <stdio.h>
#include <stdlib.h>



int main(){
    int N,a;
    scanf("%d", &N);
    int *target = (int *)calloc(10001, sizeof(int));
    for(int i=0;i<N;i++){
        scanf("%d", &a);
        *(target+a) +=1;
    }
    for(int i=1;i<=10000;i++){
        for(int j=0;j<*(target+i);j++){
            printf("%d\n", i);
        }
    }
    return 0;
}