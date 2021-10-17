#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b){ 
    int temp = *a;
    *a = *b;
    *b = temp;
}

long int quickA1(int *input, int start, int end){
    int length = end-start+1;
    int i = 0;
    long int count = 0;
    if(length <=1){
        return 0;
    }
    int pivot = start;
    count+=length-1;
    for(int j=start+1;j<=end;j++){
        if(input[j] < input[pivot]){
            i++;
            swap(input+j, input+start+i);
        }
    }
    swap(input+i+start, input+pivot);
    pivot = i+start;
    count += quickA1(input, start, start+i-1);
    count += quickA1(input, start+i+1, end);
    return count;
}

int main(){
    int N;
    scanf("%d", &N);
    int *target = (int *)calloc(N, sizeof(int));
    for(int i=0;i<N;i++){
        scanf("%d", target+i);
    }
    quickA1(target,0,N-1);
    for(int i=0;i<N;i++){
        printf("%d\n", *(target+i));
    }
    return 0;
}