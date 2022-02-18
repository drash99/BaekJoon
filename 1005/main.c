#include <stdio.h>
#include <assert.h>

int edges[1001][1001]; // 1 1 0 -1
int time[1001] = {0};
int timereq[1001];
int watching[10000000];
int t,n,k,a,b,i,w,pt,ptcur;

int max(int a,int b){
    if (a>b) return a;
    else return b;
}

void work(){
    for (i=0;i<1001;i++){
        for(int j=0;j<1001;j++){
            edges[i][j] = 0;
        }
        time[i] = -1;
        timereq[i] = 0;
    }
    scanf("%d %d", &n, &k);
    for (i=1;i<=n;i++){
        scanf("%d", &timereq[i]);
    }
    for (i=0;i<k;i++){
        scanf("%d %d", &a, &b);
        edges[a][b] = 1;
        edges[b][a] = -1;
    }
    scanf("%d", &w);
    int cursor = 0;
    int len = 0;
    int ans;
    int tmp;
    watching[0] = w;
    len++;
    time[w] = timereq[w];
    ans = time[w];
    while( len > cursor){
        pt = watching[cursor];
        ptcur = time[pt]-timereq[pt];
        tmp = 0;
        for (i=1;i<=n;i++){
            if (edges[pt][i] != 0){
                if (edges[pt][i] == 1){
                    ptcur = max(ptcur, time[i]);
                }else if (edges[pt][i] == -1){
                    watching[len] = i;
                    len++;
                    tmp++;
                }
            }
        }
        time[pt] = timereq[pt] + ptcur;
        ans = max(time[pt], ans);
        cursor++;
    }

    printf("%d\n",ans);
}

int main(){
    scanf("%d",&t);
    for (int j=0;j<t;j++){
        work();
    }
    return 0;
}