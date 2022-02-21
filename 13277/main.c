#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

typedef struct longnum{
    char digits[600001]; //in reverse order(like little endian)
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

longnum *sublongf(longnum *input1, longnum *input2){
    int carry=0;
    longnum *res = input1;
    int maxlen = (input1->length < input2->length)?input2->length:input1->length;
    for(int i=0;i<maxlen;i++){
        res->digits[i] = input1->digits[i] - input2->digits[i]- carry;
        if(res->digits[i]<0){
            carry = 1;
            res->digits[i] += 10;
        }else{
            carry = 0;
        }
    }
    for(int i=maxlen-1;i>=0;i--){
        if(res->digits[i] != 0){
            res->length = i+1;
            return res;
        }
    }
    res->length = 0;
    return res;
}

void splitnum(longnum *input, longnum *a, longnum *b, int n){
    int sizea = 0;
    int sizeb = 0;
    for(int i=0;i<n;i++){
        b->digits[i] = input->digits[i];
        if(b->digits[i] != 0){
            sizeb = i+1;
        }
    }
    b->length = sizeb;
    for(int i=0;i< input->length - n;i++){
        a->digits[i] = input->digits[n+i];
        if(a->digits[i] != 0){
            sizea = i+1;
        }
    }
    a->length = sizea;
}

longnum *shiftleft(longnum *input, int n){
    if(n==0){
        return input;
    }
    for(int i=input->length-1;i>=0;i--){
        input->digits[i+n] = input->digits[i];
        input->digits[i] = 0;
    }
    input->length+=n;
    return input;
}

longnum *Gradeschool(longnum *input1, longnum *input2){
    longnum *res = CreateLongnum(NULL);
    longnum *tmp = CreateLongnum(NULL);
    int result = 0;
    int carry =0;
    for(int i=0;i<input2->length;i++){
        carry = 0;
        for(int j=0;j<input1->length;j++){
            result = input1->digits[j]*input2->digits[i] + carry;
            carry = result/10;
            tmp->digits[j] = result%10;
        }
        tmp->length = input1->length;
        if(carry){
            tmp->digits[input1->length] = carry;
            tmp->length++;
        }
        tmp = shiftleft(tmp, i);
        addlongf(res,tmp);
        free(tmp);
        tmp = CreateLongnum(NULL);
    }
    free(tmp);
    return res;
}


longnum *Karatsuba(longnum *input1, longnum *input2){
    longnum *res;
    if(input1->length==0||input2->length==0){
        res = CreateLongnum(NULL);
        return res;
    }
    int totallen = (input1->length < input2->length)?\
    input2->length:input1->length;
    long result;
    if(input1->length + input2->length<= 18){
        /*if the sum of the lengths of input1 and input is smaller
        than 18, which is smaller than the max value of 64 bit long, 
        perform direct multiplication.*/
        return Gradeschool(input1, input2);
    }
    longnum *a = CreateLongnum(NULL);
    longnum *b = CreateLongnum(NULL);
    longnum *c = CreateLongnum(NULL);
    longnum *d = CreateLongnum(NULL);
    splitnum(input1, a, b, totallen/2);
    splitnum(input2, c, d, totallen/2);
    longnum *apb = addlong(a,b);
    longnum *cpd = addlong(c,d);
    longnum *ac = Karatsuba(a,c);
    longnum *bd = Karatsuba(b,d);
    longnum *bcad = sublongf(sublongf(Karatsuba(apb,cpd),ac),bd);
    longnum *restmp1 = addlongf(shiftleft(ac,2*(totallen/2)),shiftleft(bcad,totallen/2));
    res = addlongf(restmp1,bd);
    free(a);
    free(b);
    free(c);
    free(d);
    free(apb);
    free(cpd);
    free(bcad);
    free(bd);
    return res;

}
int scannum(char *rawnum1, char *rawnum2){
    if(EOF==scanf("%s",rawnum1)){
            return 0;
    }
    if(EOF==scanf("%s",rawnum2)){
            return 0;
    }
    return 1;
}
int main(){
    char rawnum1[300001]; 
    char rawnum2[300001];
    double gradetime;
    double karatime;
    longnum *input1;
    longnum *input2;
    longnum *gradesch;
    longnum *karat;
    int i;
    scanf("%s", rawnum1);
    scanf("%s", rawnum2);
    //while(scannum(rawnum1,rawnum2)){
        input1 = CreateLongnum(rawnum1);
        input2 = CreateLongnum(rawnum2);


        karat = Karatsuba(input1, input2);


        printLongnum(karat);
        free(karat);
        printf("\n");
    //}
    return 1;

}