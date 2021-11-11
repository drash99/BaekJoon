#include <stdio.h>
#include <stdlib.h>

unsigned long long chk1(unsigned long long a, int d, unsigned long long n){
    if(a==0){
        return 0;
    }
    if(a==1){
        return 1;
    }
    if(d==1){
        //printf("\nchk: %ld\n", a);
        return a;
    }
    if(d%2==1){    
        return (a*chk1((a*a)%n, d/2, n))%n;
    }else{
        return chk1((a*a)%n, d/2, n);
    }
}

unsigned long long chk2(unsigned long long a, int d, unsigned long long n){
    if(d==0){
        return a%n;
    }
    if(d==1){
        return (a*a)%n;
    }
    return (chk2(a, d-1, n)*chk2(a, d-1, n))%n;
}


int isPrime(unsigned long long area){
    unsigned long long n;
    int s;
    s = 1;
    //printf("%llu %llu\n", area,n);
    n = area*2 +1;
    while((area%2)==0){
        s++;
        area = area>>1;
    }    
    //printf("%llu %llu\n", area,n);
    unsigned long long a[5] = {2,7,61};
    int isPrime = 0;
    for(int i =0; i<3; i++){
        if(a[i]>=n){
            isPrime+=1;
            continue;
        }
        if(chk1(a[i],area,n)==1){
            isPrime+=1;
            continue;
        }
        for(int r=0;r<s;r++){
            //printf("%llu %llu %d %llu\n", a[i], area,r,n);
            if(chk1(chk2(a[i],r,n),area,n)==n-1){
                isPrime+=1;
                break;
            }
            
        }
        //printf("%d, %ld:%ld, %d\n", n,area,a[i],isPrime);
        
    }
    return (isPrime==3)?1:0;
}
void ispossible(int *ans, unsigned long long area){
    if(area<4){
        *ans+=1;
        return;
    }
    
    *ans+=isPrime(area);
    
}

int main(){
    long long N;
    
    scanf("%lld", &N);
    int ans = 4;
    for(unsigned long long i=9;i<N;i+=2){
        if(i%3==0 || i%5==0 || i%7==0){
            continue;
        }
        if(i%1000003==0){
            printf("%lld\n", i/1000003);
        }
        ispossible(&ans,i/2);
    }
    printf("%d\n",ans);
    /*
    long a;
    for(int i=0;i<N;i++){
        scanf("%ld", &a);
        ispossible(&ans,a);
    }
    printf("%d\n",ans);
    */
    return 0;
}