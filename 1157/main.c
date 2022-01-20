#include <stdio.h>


int main(){
    int arr[26];
    char input[1000001];
    scanf("%s", input);
    for(int i=0;input[i];i++){
        if(input[i] >= 'a' && input[i] <= 'z'){
            arr[input[i]-'a'] ++;
        }else{
            arr[input[i]-'A'] ++;
        }
    }
    int max = 0;
    for(int i=0;i<26;i++)
        if (arr[i]>arr[max]) max=i;
    
    int cnt = 0;
    for(int i=0;i<26;i++)
        if (arr[i]==arr[max]) cnt++;
    if (cnt == 1)
        printf("%c\n",max+'A');
    else printf("?\n");
}