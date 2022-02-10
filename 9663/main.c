#include <stdio.h>

int n;

int findsafe(int *status, int pos, int y){
    for (int i=0;i<y;i++){
        if (pos == status[i]) return 0;
        else if (pos - status[i] == y-i) return 0;
        else if (pos - status[i] == i-y) return 0;
    }
    return 1;
}

int placeq(int *status, int recurse){
    if (recurse == n) return 1;
    int tmp= 0;
    for(int i=0;i<n;i++){
        if (findsafe(status, i, recurse)){
            status[recurse] = i;
            tmp += placeq(status, recurse+1);
        }
    }
    return tmp;
}

int main(){
    scanf("%d", &n);
    int possible[n];
    printf("%d\n", placeq(possible,0));
    return 0;
}