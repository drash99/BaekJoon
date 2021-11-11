#include <stdio.h>
#define MAX_LENGTH 60

int totalcnt(char ** wordlist, int depth, int num){

}

int main(){
    int wordnum;
    while(scanf("%d",&wordnum)){
        char *wordlist[wordnum];
        for (int i =0; i< wordnum;i++){
            char word[MAX_LENGTH];
            scanf("%s", word);
            wordlist[i] = word;
        }
        for (int i =0; i< wordnum;i++){
            printf("%s\n", wordlist[i]);
        }
    }
}