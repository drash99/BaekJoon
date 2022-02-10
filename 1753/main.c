#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*macros for constants. INF indicates infinte, NC indicates Not connected*/
#define INF 0x7fffffff
#define NC -2147483648

/*macros for calculating offset so it emulates multi-dimensional array with single array*/
#define ADJMATCAL(nV,a,b) (nV+1)*a+b

/*print result string from bfmat. bfmat is the data after 
running Bellman-Ford algorithm with source vertex src.*/
void bfprinter(int *bfmat, int src, int nV, int *adjmat){
    for(int j=1;j<=nV;j++){
        if(src==j) printf("0\n");
        else if (bfmat[j] == INF){
            printf("INF\n");    
        }else{
            printf("%d\n", bfmat[j]);
        }

    }
}

/*Perform Bellman-Ford algorithm.*/
int bf(int *bfmat, int *bfmatprev, int nV, int *adjmat){
    for(int i=0; i<nV;i++){
        bfmat[0] = bfmatprev[0]+1;
        int min, weight;
        for(int v=1;v<nV+1;v++){
            min = bfmatprev[v];

            for(int w=1;w<nV+1;w++){
                if((weight = adjmat[ADJMATCAL(nV, w, v)])!=NC){
                    if(bfmatprev[w] != INF && min > weight+bfmatprev[w]) min = weight+bfmatprev[w];
                }
            }
            bfmat[v] = min;
        }
        if(memcmp(bfmat+1, bfmatprev+1,nV*sizeof(int))==0){
            //printf("early finish\n");
            break;
        }
        int *temp;
        temp = bfmat;
        bfmat = bfmatprev;
        bfmatprev = temp;
    }   
    return 0;
}



int main(int argc, char *argv[]){
    int srcV;
    int nV, nE;
    scanf("%d %d", &nV, &nE);
    scanf("%d", &srcV);
    int *adjmat = malloc((nV+1)*(nV+1)*sizeof(int));
    for (int i=0;i<nV+1;i++){
        for (int j=0;j<nV+1; j++){
            adjmat[ADJMATCAL(nV, i,j)] = NC;
        }
    }
    int a,b,w, ress;
    for(int i=0;i<nE;i++){
        scanf("%d %d %d", &a, &b, &w);
        adjmat[ADJMATCAL(nV,a,b)] = w;
    }
    int *bfmat = malloc((nV+1)*sizeof(int));
    int *bfmatprev = malloc((nV+1)*sizeof(int));
    bfmat[0] = 0;
    bfmatprev[0] = 0;
    for(int i=1;i<nV+1;i++){
        bfmat[i] = INF;
        bfmatprev[i] = INF;
    }
    bfmatprev[srcV] = 0;
    bfmat[srcV] = 0;
    bf(bfmat,bfmatprev, nV, adjmat);
    bfprinter(bfmat, srcV, nV, adjmat);
    

    
}