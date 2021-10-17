#include <stdio.h>
#include <stdlib.h>

struct linkedlist
{
    struct linkedlist* next;
    int value;
};

typedef struct linkedlist LinkedList;

void appendend(LinkedList **source, int value, LinkedList *target){
    if(*(source+value)){
        LinkedList *cursor = *(source+value);
        while(cursor->next){
            cursor = cursor->next;
        }
        cursor->next = target;

    }else{
        *(source+value) = target;
    }
}

void markparent(LinkedList **source, int answer[], int parent, int self){
    LinkedList *cursor = *(source+self-1);
    while(cursor){
        if(cursor->value != parent){
            answer[cursor->value-1] = self;
            markparent(source, answer, self, cursor->value);
        }
        cursor = cursor->next;
    }
}


int main(){
    int N,a,b;
    scanf("%d", &N);
    int answer[N];
    LinkedList **connected = calloc(N, sizeof(LinkedList *));
    LinkedList *anode;
    LinkedList *bnode;
    for(int i=1;i<N;i++){
        scanf("%d %d", &a,&b);
        anode = calloc(1, sizeof(LinkedList));
        anode->value = a;
        bnode = calloc(1, sizeof(LinkedList));
        bnode->value = b;
        appendend(connected,(a-1),bnode);
        appendend(connected,(b-1),anode);
    }
    markparent(connected, answer, 0, 1);
    for(int i=1;i<N;i++){
        printf("%d\n",answer[i]);
    }
}