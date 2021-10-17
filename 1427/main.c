#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b)   
{
    char num1 = *(char *)a;   
    char num2 = *(char *)b;   

    if (num1 < num2)   
        return 1;     
    
    if (num1 > num2)   
        return -1;      
    
    return 0;  
}

int main(){
    char target[11];
    scanf("%s", target);
    qsort(target,strlen(target), sizeof(char), compare);
    printf("%s",target);
    return 0;
}