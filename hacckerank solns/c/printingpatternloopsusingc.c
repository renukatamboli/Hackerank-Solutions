#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int max(int a,int b){
    if(a>b){
        return a;
    }
    else{
        return b;
    }
}
int main() 
{

    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    for(int r=0;r<n;r++){
        for(int c=0;c<n-1;c++){
            printf("%d",max(n-r,n-(c%(2*n-2))));
            printf(" ");
        }
        for(int c=n-1;c>=0;c--){
            printf("%d",max(n-r,n-(c%(2*n-2))));
            printf(" ");
        }
        
        printf("\n");
    }
     for(int r=n-2;r>=0;r--){
        for(int c=0;c<n-1;c++){
            printf("%d",max(n-r,n-(c%(2*n-2))));
            printf(" ");
        }
        for(int c=n-1;c>=0;c--){
            printf("%d",max(n-r,n-(c%(2*n-2))));
            printf(" ");
        }
        
        printf("\n");
    }
    return 0;
}

