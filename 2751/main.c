#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)   
{
    int num1 = *(int *)a;   
    int num2 = *(int *)b;   

    if (num1 < num2)   
        return -1;     
    
    if (num1 > num2)   
        return 1;      
    
    return 0;  
}

int main(){
    int N;
    scanf("%d", &N);
    int *target = (int *)calloc(N, sizeof(int));
    for(int i=0;i<N;i++){
        scanf("%d", target+i);
    }
    qsort(target,N, sizeof(int), compare);
    for(int i=0;i<N;i++){
        printf("%d\n", *(target+i));
    }
    return 0;
}