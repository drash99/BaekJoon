#include <stdio.h>
#include <stdlib.h>

typedef struct longnum{
    char digits[71]; //in reverse order(like little endian)
    int length;//length of current 
} longnum;
struct Trie{
    int idx;
    struct Trie *childs[10];
};
typedef struct Trie * triep;

longnum *CreateLongnum(char *rawnum){
    longnum *p = (longnum *)calloc(1, sizeof(longnum));
    if(p==NULL){
        return NULL;
    }
    if(rawnum == NULL){
        return p;
    }
    int i = 0;
    while(rawnum&&*(rawnum+i) != '\0'){
        i++;
    }
    p->length = i;
    while(i>0){
        p->digits[p->length-i] = *(rawnum+i-1)-'0';
        i--;
    }
    return p;
}

longnum *addlong(longnum *input1, longnum *input2){
    int carry=0;
    int result;
    
    longnum *res = CreateLongnum(NULL);
    int maxlen = (input1->length < input2->length)?input2->length:input1->length;
    for(int i=0;i<maxlen;i++){
        result = input1->digits[i] + input2->digits[i]+ carry;
        if(result>=10){
            carry = 1;
            res->digits[i] = result % 10;
        }else{
            carry = 0;
            res->digits[i] = result;
        }
    }
    res->length = maxlen;
    if(carry==1){
        res->digits[maxlen]=1;
        res->length= maxlen+1;
    }
    return res;
}


longnum *decone(longnum *num){
    int i;
    for (i=1;i<num->length;i++){
        num->digits[i-1] = num->digits[i];
    }
    num->digits[num->length-1] = 0;
    num->length--;
    return num;
}

triep CreateTrie(int idx){
    triep trie = (triep)calloc(1,sizeof(struct Trie));
    trie->idx = idx;
    for (int i=0;i<10;i++){
        trie->childs[i] = NULL;
    }
    return trie;
}

char *printLongnum(char *dest, longnum *num){
    int i;
    for(i=num->length-1;i>=0 && i>=num->length-41;i--){
        dest[num->length-1-i]  = num->digits[i] + '0';
    }
    dest[num->length-1-i] = '\0';
    return dest;
}

void puttrie(triep trie, int idx, char * target){
    if (*target == '\0'){
        return;
    }
    char head = *target-'0';
    if (trie->childs[head] == NULL){
        triep child = CreateTrie(idx);
        trie->childs[head] = child;
    }
    puttrie(trie->childs[head], idx, target+1);
}

int search(triep trie, char *target){
    if (*target == '\0'){
        return trie->idx;
    }
    char head = *target-'0';
    if (trie->childs[head] == NULL){
        return -1;
    }
    return search(trie->childs[head], target+1);
}




int main(){
    int t, n, i;
    longnum *tmp1 = CreateLongnum("1");
    longnum *tmp2 = CreateLongnum("1");
    longnum *tmp3;
    struct Trie trie;
    trie.idx = 0;
    for (i=0;i<10;i++){
        trie.childs[i] = NULL;
    }
    puttrie(&trie, 0, "1");
    char temp[50];
    for (int i=2;i<100000;i++){
        tmp3 = addlong(tmp1, tmp2);
        //printLongnum(temp, tmp3);
        //printf("%d:%s(%d)\n",i,temp, tmp3->length);
        free(tmp1);
        tmp1 = tmp2;
        tmp2 = tmp3;
        if (tmp3->length >70){
            //printLongnum(temp, tmp1);
            //printf("%d:%s\n",i,temp);
            decone(tmp1);
            //printLongnum(temp, tmp1);
            //printf("%d:%s\n",i,temp);
            decone(tmp2);
        }
        puttrie(&trie, i, printLongnum(temp, tmp3));
        //if (i>=78 && i<= 400){
            //printf("%d:%s(%d)\n",i,temp, tmp3->length);    
            //printLongnum(temp, tmp1);
            //printf("%d:%s(%d)\n",i,temp, tmp1->length);
        //}

        //printf("%d:%s\n",i,temp);
    }

    scanf("%d", &t);
    for (i =0;i<t;i++){
        scanf("%s", temp);
        printf("Case #%d: %d\n", i+1, search(&trie, temp));
    }
    return 0;
}