#include <stdio.h>
#include <stdlib.h>

typedef struct longnum{
    char digits[10001]; //in reverse order(like little endian)
    int length;//length of current 
} longnum;


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

void printLongnum(longnum *num){
    for(int i=num->length-1;i>=0;i--){
        printf("%d",num->digits[i]);
    }
}

longnum *addlongf(longnum *input1, longnum *input2){
    int carry=0;
    int result;
    longnum *res = input1;
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

int main(){
    char num1[10001];
    char num2[10001];
    longnum *input1;
    longnum *input2;
    
    scanf("%s", num1);
    scanf("%s", num2);
    
    input1 = CreateLongnum(num1);
    input2 = CreateLongnum(num2);
    /*printLongnum(input1);
    printf("\n");
    printLongnum(input2);
    printf("\n");*/
    printLongnum(addlongf(input1, input2));
    printf("\n");
    return 0;

}