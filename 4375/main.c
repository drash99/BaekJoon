#include <stdio.h>

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        int tmp = 1;
        int res = 1;
        while(tmp%n!=0){
            tmp = (tmp*10+1)%n;
            res++;
        }
        printf("%d\n", res);
    }
    return 0;
}